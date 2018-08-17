# RFC 文件

這篇的知識, 熟了之後得整合到 `Network infrastructure.md` 這篇

<details>
    <summary> RFC List... </summary>

- [rfc1122](#rfc1122) - Requirements for Internet Hosts -- Communication Layers
- [rfc2119](#rfc2119) - Key words for use in RFCs to Indicate Requirement Levels
- [rfc2616](#rfc2616) - Hypertext Transfer Protocol -- HTTP/1.1
- [rfc7540](#rfc7540) - Hypertext Transfer Protocol Version 2 (HTTP/2)
</details>



# [rfc1122](https://tools.ietf.org/html/rfc1122) - TCP/IP standard

## 術語

### * Frame : 資料訊框 (L2 資料連結層)

> A frame is the unit of transmission in a link layer protocol, and consists of a link-layer header followed by a packet.


### * Packet : 封包 (L3 網路層)

> A packet is the unit of data passed across the interface between the internet layer and the link layer.  It includes an IP header and data.  A packet may be a complete IP datagram or a fragment of an IP datagram.

`一個 Packet` 可能為 `一個 IP datagram` ; 或者也可能為 `一個 IP datagram 的片段`


### * IP Datagram : 封包 (L3 網路層)

> An IP datagram is the unit of end-to-end transmission in the IP protocol.  An IP datagram consists of an IP header followed by transport layer data, i.e., of an IP header followed by a message.
> In the description of the internet layer (Section 3), the unqualified term "datagram" should be understood to refer to an IP datagram.

`IP Datagram` = `IP header` + `傳輸層 data`(ex: message).


### * Segment : 資料段 (L4 傳輸層)

> A segment is the unit of end-to-end transmission in the TCP protocol.  A segment consists of a TCP header followed by application data.  A segment is transmitted by encapsulation inside an IP datagram.

`segment` = `TCP header` + `application data`

* Message

> In this description of the lower-layer protocols, a message is the unit of transmission in a transport layer protocol.  In particular, a TCP segment is a message.  A message consists of a transport protocol header followed by application protocol data.  To be transmitted end-to-end through the Internet, a message must be encapsulated inside a datagram.



    Connected Network
        A network to which a host is interfaced is often known as
        the "local network" or the "subnetwork" relative to that
        host.  However, these terms can cause confusion, and
        therefore we use the term "connected network" in this
        document.

    Multihomed
        A host is said to be multihomed if it has multiple IP
        addresses.  For a discussion of multihoming, see Section
        3.3.4 below.

    Physical network interface
        This is a physical interface to a connected network and
        has a (possibly unique) link-layer address.  Multiple
        physical network interfaces on a single host may share the
        same link-layer address, but the address must be unique
        for different hosts on the same physical network.

    Logical [network] interface
        We define a logical [network] interface to be a logical
        path, distinguished by a unique IP address, to a connected
        network.  See Section 3.3.4.
    Specific-destination address
        This is the effective destination address of a datagram,
        even if it is broadcast or multicast; see Section 3.2.1.3.

    Path
        At a given moment, all the IP datagrams from a particular
        source host to a particular destination host will
        typically traverse the same sequence of gateways.  We use
        the term "path" for this sequence.  Note that a path is
        uni-directional; it is not unusual to have different paths
        in the two directions between a given host pair.

    MTU
        The maximum transmission unit, i.e., the size of the
        largest packet that can be transmitted.
    The terms frame, packet, datagram, message, and segment are
    illustrated by the following schematic diagrams:

    A. Transmission on connected network:
    _______________________________________________
    | LL hdr | IP hdr |         (data)              |
    |________|________|_____________________________|

    <---------- Frame ----------------------------->
            <----------Packet -------------------->


    B. Before IP fragmentation or after IP reassembly:
            ______________________________________
            | IP hdr | transport| Application Data |
            |________|____hdr___|__________________|

            <--------  Datagram ------------------>
                        <-------- Message ----------->
    or, for TCP:
            ______________________________________
            | IP hdr |  TCP hdr | Application Data |
            |________|__________|__________________|

            <--------  Datagram ------------------>
                        <-------- Segment ----------->


# [rfc2119](https://www.ietf.org/rfc/rfc2119.txt)

## Key words for use in RFCs to Indicate Requirement Levels

- 2018/08/10

> 這篇只是在定義 `RFC 文件們` 用詞的定義

term        | Description
----------- | ---------------------------
MUST        | absolute requirement
SHOULD      | 建議應該怎麼做
MAY         | 可有可無
REQUIRED    | (同 MUST)
SHALL       | (同 MUST)
RECOMMENDED | (同 SHOULD)
OPTIONAL    | (同 MAY)



# [rfc2616](https://www.ietf.org/rfc/rfc2616.txt)

## Hypertext Transfer Protocol -- HTTP/1.1

> HTTP/1.1 的第一篇創始文章, 由 (1997) 發表至今 (2018/08), 仍是 internet 主流協定.



## status code

Code                       | Description
-------------------------- | ---------------------------------
403 Forbidden              | 請求被 Server 拒絕, Server 應回傳拒絕原因 or 導向 404
405 Method Not Allowed     | Request Line 不支援此方法
415 Unsupported Media Type | 要給 `Content-Type`

# [rfc7540](https://www.ietf.org/rfc/rfc7540.txt)

## Hypertext Transfer Protocol Version 2 (HTTP/2)

> 

- `HTTP/2` 為 `HTTP/1.1` 的 替代方案
- `HTTP/2` 藉由引入 「header field compression(表頭壓縮)」 及 「allow multiple concurrent exchange on the same(允許共時)」來提升網路傳輸效能, 減少前端網路延遲的知覺.
- `HTTP/1.0` && `HTTP/1.1` 過大的 `http header` 容易造成 `TCP congestion`, 因而 `HTTP/2` 允許 相同連線上 交錯 `request` 與 `response message`, 並允許對 `request` 作優先級別的排序
    - `HTTP/1.0` : 相同時間內, 只能有一個 `TCP connection`
    - `HTTP/1.1` : 相較於 `1.0`, 增加了 `request pipeline`, 部份解決 `addressed request concurrency`


