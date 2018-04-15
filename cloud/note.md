
## 名詞
- cascade: 串連
- VPC: Virtual Private Cloud
- DHCP: Dynamic Host Configuration Protocol
- NAT: Network Address Translation
- IP Masquerade: IP掩蔽
- Elastic IP(aws)/Floating IP(openstack): 


### Virtual Private Cloud - VPC 虛擬網路



### 虛擬交換器
連接`'虛擬機器實體'的虛擬 NIC的位置`, 一個 `虛擬交換器`, 會被指派一個`子網路`(具有私有ip範圍)

#### 1. openstack
1. 一開始定義好「虛擬交換器」, 之後重新指派「子網路」
2. `虛擬交換器`會自動跨多個服務區

#### 2. aws
1. (無此概念), 可理解成「虛擬交換器 + 子網路」的方式
2. `虛擬交換器`只屬於單一服務區域

之後~~, `虛擬交換器` 與 `虛擬路由器` 連線, 就可以與外部網路傳輸資料了.