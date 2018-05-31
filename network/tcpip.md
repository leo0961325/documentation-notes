# TCP/IP
- 2018/05/17

> Internet Society(ISOC)底下有3個組織, 分別是 `IETF`, 發布RFC草案、RFC標準文件; `IRTF`, 用來做未來的研究; `IANA`, 發布位置...


## 私有 IP位址
Class | Definition     | Range
----- | -------------- | --------
A     | 10.0.0.0/8     | 10.0.0.1 ~ 10.255.255.254
B     | 172.16.0.0/12  | 172.16.0.1 ~ 172.31.255.254
C     | 192.168.0.0/16 | 192.168.0.1 ~ 192.168.255.254



## 零星片段 && 名詞
- 應用程式協定的標準(Application Protocol Standards) `Socket API`
- 非連結式封包傳遞服務(Connectionless Packet Delivery Service), ex: IP協定、UDP協定
- 端對端確認(End-to-End Acknowledgements), `TCP (three-way handshake)` (建立 Session)
- Network: 網路 網段
- Network Segment 網段 網路區段
- Automatic Private IP Addressing (APIPA) : 自動私人IP定址



## Network Segment

以不同層面來看, 
- Network Layer : Network ID相同; 通常稱為 `Subnet` or `Sub Network`
- DataLink Layer : 
- Physical Layer : 共用相同傳輸媒介的話, 都算同 network segment

### Network ID 、 Host ID
依照 class 決定 or Subnet Mask 指示




# Broadcast 廣播

```
  router                D    E    F
    |                   |    |    |    
----●----O----O----O----O----O----O----●----
         |    |    |                   |
         A    B    C                 router

A: 192.168.1.1
B: 192.168.1.2
C: 192.168.1.3
D: 192.168.2.1
E: 192.168.2.2
F: 192.168.2.3
```
- 沒有被 `router` 隔開的 Network, "建議"只規畫一個 `IP Network`
- 被 `router`隔開的 Network, 必須有不同的 `IP Network`
- 若 `192.168.1.1` 送出 ip封包 -> `255.255.255.255`, 則 **B~F** 都會收 `Limited broadcast`
- 若 `192.168.1.1` 送出 ip封包 -> `192.168.2.255`  , 則 **D~F** 都會收 `Subnet broadcast`


# 計算 `網段位址`
1. `IP Address` 轉成 2進制
2. `Subnet Mask` 轉成 2進制
3. 以上2者作 **AND** 運算

```
ex1: 138.239.149.238/255.255.224.0
喵一眼可發現, 一定是 255.255 開頭
149 -> 10010101
224 -> 11100000
AND    --------
       10000000 -> 128

所以 Network Number 為 255.255.128.0
```

ip subnetting
- 等量(長)切割法)(RFC 1812) -> 切割後的每個 subnet 可用IP數量相同 -> subnet mask值相同

步驟
1. 把 `Network Number` 與 `原 Subnet Mask` 轉二進位, 找出 `原Network ID` 與 `原 Host ID` 各用那些 bits
2. 將原 `Host ID` 用的 bits, 由左而右, 取 **n個 bit(s)** 作為 `Subnet ID` 使用的 bit(s) -> 得到新的 `Host ID` 用那些 bits

    **2^n >= 所需的 Subnet數**. 若 n 取 *符合條件的最小值*, 可讓切出的 Subnet 擁有最多可用 `Host IP`

3. 將 `Subnet ID` 所用的 bits 的各種組合寫出(會有多個), 前方串上 `原 Network ID`, 即得到每個 `Subnet` 的新 `Network ID`.
4. `Host ID`全為 2進位的 0即為 `Network Number`; 1即為 `Subnet 的 Subnet Broadcast`.

```
----- Question -----
把 131.210.0.0 劃分成 6個子網路, 求
A. 子網路遮罩
B. 各個子望路可分配的主機數量
C. 各個子網路的範圍

----- Answer -----
沒多說的話, 就是屬於 class B, Default Mask就是 255.255.0.0

切個成6個子網路, 那就得借用 2^n >= 6, n >= 3 bits
即為 11100000 => 224
所以, 切割後的 子網路遮罩 為 255.255.224.0

剩餘的 5+8個位元, 可用來分配給 Host ID, 則可配置 2^13 - 2 = 8190台


```

## Supernetting(速算)
- 合併後的 `Network Number`, 就是`原 Network`值最小的那個
- 合併後的 `Subnet Mask`, 就是`原 Subnet Mask` 的個數 - n, 其中, 「2^n >= Network 數量」

### 是否可 supernetting(速算)
以「10進制」表示, 最小的 `Network Number`最右方不為 0 的值, 是否可被 Network們 的數量整除, 若是, 則可 supernetting
```
# 1. 可subnetting (6/2組subnet個數整除)
192.168.6.0/24
192.168.7.0/24

# 2. 不可subnetting (6110, 2個1, 無法被底下4組subnet個數整除)
192.168.6.0/24
192.168.7.0/24
192.168.8.0/24
192.168.9.0/24
```

#### 範例1 (傻傻的算):
```
# 有4個子網段, 打算把它合併起來, 來滿足 「能把 800 台電腦串在一起(同網段), 卻又不造成大量浪費(用 Class B啦)的作法」, 網路編號(Network Number)如下:
192.168.4.0/24
192.168.5.0/24
192.168.6.0/24
192.168.7.0/24

# 轉成 2進位 逐bit 對齊
11000000 10101000 00000100 00000000
11000000 10101000 00000101 00000000
11000000 10101000 00000110 00000000
11000000 10101000 00000111 00000000
________ ________ ______xx

# 逐 bit 觀察, 是不是所有的值都相同, 以上相同的標 _ , 不同的標 x, 
假如「xx」的部分, 各種排列組合都有 => 可以做 supernetting
假如「xx」的部分, "並非"各種排列組合都有, 要看缺乏的排列組合的那些網段, 是不是「未分配」, 若是 => 可以做 supernetting
所以, 此範例可以做 Supernetting!!  來開始 Super 了~~

把「_」部分, 當成「合併後的 Network ID」
把「x」部分, 當成「合併後的 Host ID」
11000000 10101000 000001|00 00000000
11000000 10101000 000001|01 00000000
11000000 10101000 000001|10 00000000
11000000 10101000 000001|11 00000000
 NEW Network ID         | NEW Host ID

# 合併後的 Subnet Mask 為 255.255.252.0
11111111 11111111 11111100 00000000

# 合併後的 Network Number 為 192.168.4.0
11000000 10101000 00000100 00000000
```

#### 範例2 (傻傻的算):
```
200.12.12.64/28
200.12.12.80/28
200.12.12.96/28
200.12.12.112/28

11001000 00001100 00001100 01000000/28
11001000 00001100 00001100 01010000/28
11001000 00001100 00001100 01100000/28
11001000 00001100 00001100 01110000/28
________ ________ ________ __xxxxxx

# 當然, 上述的其餘網段「x」部分 如果沒被分配的話, 才適合做 Supernetting

Net Network ID: 200.12.12.64/26
11001000 00001100 00001100 01000000

New Subnet Mask: 255.255.255.192/26
11111111 11111111 11111111 11000000
```