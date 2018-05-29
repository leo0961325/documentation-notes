# TCP/IP
- 2018/05/17

> Internet Society(ISOC)底下有3個組織, 分別是 `IETF`, 發布RFC草案、RFC標準文件; `IRTF`, 用來做未來的研究; `IANA`, 發布位置...


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