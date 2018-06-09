# 磁碟分割
- 2018/04/21
- 硬梆梆...


## 專有名詞: 

Sector: 磁區

Track: 磁軌

Cylinder: 磁柱

MBR(Master Boot Record): 主要開機紀錄區

GPT: GUID Partition Table

LBA(Logical Block Address): 邏輯區塊位址


## 說明

磁區(Sector)是儲存資料的最小物理單位, 整顆硬碟裡頭, 最重要的磁區為 `第1個磁區`, 此磁區記錄著 `整個硬碟的重要資訊`.

分割, 主要以 `磁柱(Cylinder)` 為單位.

作磁區分割, 有 2種方式
1. 早期的 `MsDOS MBR` (512 bytes)
2. 現代支援大容量硬碟的 `GPT` (4K bytes)

### 1. MsDOS MBR
Linux當初規劃, 就是為了能兼容 Windows的磁碟. 裏頭塞了2個重要的東西:

1. 主要開機紀錄區(Master Boot Record)
    裡面有開機管理程式. 占了 446 bytes

2. 分割表(Partition Table)
    紀錄`整顆磁碟分割的狀態`. 占了 64 bytes. `只能記錄4組紀錄區`(為啥... 我也不懂orz). 這4組紀錄區, 即為 1個 `主要分割區(Primary Partition)` 及 最多3個 `邏輯分割區(Extended Partition)`. 在作磁區劃分時, 可以切割超過4個分割區又是怎麼回事? 簡單的說, 就是用 `邏輯分割區(Logical Partition)` 的概念啦@@... 所以, 1顆硬碟, 可以在 Windows上面, 分為 C, D, E, F, ...一堆. 

每個分割表, 只有 16bytes, 影響著磁碟大小限制(2.2TB)

其餘細節, [去看鳥哥](http://linux.vbird.org/linux_basic/0130designlinux.php#partition_table), 並搜尋關鍵字「所以邏輯分割槽的裝置名稱號碼就由5號開始了」, 有個不錯的範例. 重點在於, 為什麼「/dev/sda2」之後就跳成「/dev/sda5」了...

這邊的重點節錄:
- MBR底下, `Primary Partition` 與 `Extended Partition` 最多可以有 4個(硬碟限制)
- `Extended Partition` 最多只能有 1個(作業系統限制)
- `Logical Partition` 是由 `Extended Partition` 持續切割出來的分割槽.
- 能夠被格式化後, 拿來存資料的是 `Primary Partition` 及 `Logical Partition`. (`Extended Partition` 無法格式化)
- `Logical Partition` 數量, 依作業系統而不同. Linux系統, SATA硬碟可以突破 63個以上了~
- 把 `Extended Partition` 想像成他只是個指向 `Logical Partition`的空殼. 裏頭還會指向 **尚未被分割的分割槽**.


### 2. GPT
將磁碟所有區塊以 LBA區塊來記錄分割資訊. 第一個 LBA稱為 `LBA0`. GPT使用了 34個 LBA區塊來記錄分割資訊(相較於 MBR, 只使用一個), GPT除了前面 34個 LBA之外, 整個磁碟的最後 33個 LBA也拿來做為另一個備份. 

部分磁碟為了與 MBA兼容, 會將 LBA預設為 512bytes.

![鳥哥 - GPT分割表](http://linux.vbird.org/linux_basic/0130designlinux/gpt_partition_1.jpg)

上圖, 分為3個部分說明:

1. LBA0 (MBR相容區塊)

    基本上同MBR, 存了 `開機管理程式` 及 特殊標誌的分割(單純用來表示此磁碟為 GPT格式).
    此磁區是受到保護的.

2. LBA1 (GPT表頭紀錄)
    
    記錄了`分割表本身的位置與大小`, 同時也記錄 備份用的 GPT分割放置的位置, 以及 檢驗機制碼(CRC32).

3. LBA2-33 (實際紀錄分割資訊處)

    這些區塊, 每個 LBA都可以記錄 4筆分割紀錄, 預設可以有 4*32=128筆 分割紀錄. 而每筆紀錄用到 128bytes的空間, 扣除其他必要紀錄的欄位, **GPT在每筆紀錄中分別提供了 64 bits來記載 開始/結束 的磁區號碼**, 經過一般人看不懂的計算後, 最終作業系統可以認識 *8ZB* 的磁碟.


## 後續

- 磁碟管理工具, 老牌的 `fdisk` 不認識 GPT, 需要用 `gdisk` 或 `parted`
- 開機管理程式, `grub` 不認識 GPT, 需要用 `grub2`
- 並非所有作業系統都認識 GPT, 也並非所有硬體都認識 GPT.

是否能讀寫 GPT 與 `開機的檢測程式(BIOS 與 UEFI)` 有關.
