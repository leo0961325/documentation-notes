# EC2 使用 IPv6

- 2018/11/22

## 1. VPC

Action > Edit CIDRs > Add IPv6 CIDR > Close

- IPv4 CIDR : `172.31.0.0/16`
- IPv6 CIDR : `2406:da14:b3f:b900::/56`

## 2. Subnets

Actions > Edit IPv6 CIDRs > Add IPv6 CIDR > `01` > Save > Close

- IPv4 CIDR : `172.31.32.0/20`
- IPv6 CIDR : **2406:da14:b3f:b9`01`::/64**

## 3. Route Table

Actions > Edit routes > Edit routes > `::/128` > Save routes Close

Destination                | Target             | Status
-------------------------- | ------------------ | ----------------------
172.31.0.0/16              | local              | active
2406:da14:b3f:b900::/56    | local              | active
::/128                     | igw-b6xxxxd2       | active

## 4. EC2

Actions > Networking > Manage IP Addresses > Assign new IP > `2406:da14:b3f:b901:9:8:7:6` > Yes, Update > Cancel

IPv6 : **2406:da14:b3f:b901:9:8:7:6**

# 測試

```sh
ssh -i <YOUR_KEY> ID@IPv6
```

結果無法連線, 估計是 Route Table 那邊有錯