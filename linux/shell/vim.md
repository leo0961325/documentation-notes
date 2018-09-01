# vim 指令

- 2018/08/03 update


## 我習慣的 vim操作設定

```sh
$ vi ~/.vimrc

set expandtab           # tab 以空白取代
set tabstop=4           # tab鍵=4空白
set shiftwidth=4        # 內縮設定為4個空白
set mouse=a             # 可以使用滑鼠點選
```



# Ubuntu Vim 相容模式 (Ubuntu Vim 超難用~)

```sh
$ vi ~/.vimrc

set nocompatible
```



# 基本操作

```sh
### 命令操作
:w              存檔
:w /tmp/qq      另存檔名為 /tmp/qq
:q!             不存檔離開
:x              存檔後離開





### 選取範圍
v               可逐字選取
V               一次選取整行
Ctrl+v          區塊選取 (這個猛!)


### 移動
gg              移到第 1 行
G               移動到最後一行

8G              移動到第8行
:8              移動到第8行(同8G)

0               移動到同行 行首
$               移動到同行 行尾

{               移動到同段 一開始
}               移動到同段 最末尾

%               移動到 相對應的 () [] {}


### 編輯
D               刪除 游標處 ~ 行尾
dd              刪除 整行
6,9d            刪除 6~9行
5dd             刪除 游標下面的5行

p               貼上 (Ctrl + v 的概念)
y               複製 (Ctrl + c 的概念)
x               剪下 (Ctrl + x 的概念)
u               復原 (Ctrl + z 的概念)
.               重複作上一個動作


### 搜尋
/cfg            尋找 「cfg」關鍵字
n               尋找 下一個
N               尋找 上一個


## 其他
J               合併目前行與下行
Ctrl+r          redo
```


# 操作 Vim 時的其他設定

參考: http://wiki.csie.ncku.edu.tw/vim/vimrc


```sh

:set nu                 顯示行號
:set nonu               關閉行號

:set ai                 自動內縮
:set noai               關閉內縮

:set autoindent         啟用自動縮排
:set noautoindent       取消自動縮排

:set syntax on          依照程式語言換顏色
:set syntax off         不秀顏色

:set ignorecase         搜尋不分大小寫
:set noignorecase       搜尋區分大小寫(預設)

:set tabstop=4          tab鍵=4空白

:set shiftwidth=4       內縮設定為4個空白

:set cursorline         所在行會有底線

:set mouse=a            可以使用滑鼠點選位置(這有點猛)
:set mouse=""           取消滑鼠點選位置的功能

:set expandtab          空白 取代 Tab

:retab                  將文中所有tab換成空白
:.retab                 將目前這行的tab換成空白

# Terminal底色
:set bg=dark
:set bg=light
```


# Command Mode

- `~` : 將目前所選的字, 大小寫轉換
- `x` : 剪下目前游標所在的 Character
- `r` : 
- `u` : undo
- `Ctrl+r` : redo undo

```sh
### 模式切換
a               從目前游標"之後"開始輸入
i               從目前游標"之前"開始輸入

A               從目前游標"所在行行尾"開始輸入
I               從目前游標"所在行行首"開始輸入

o               從目前游標"下一行插入一行"開始輸入
O               從目前游標"上一行插入一行"開始輸入
```


# Visual Mode

- `Ctrl+v` : 可選取區塊
- `Ctrl+V` : 可選取整行



