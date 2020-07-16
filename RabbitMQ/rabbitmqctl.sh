
### 查詢特定 vhost 的所有 consumers
$# rabbitmqctl list_consumers -p '/gb/out'
Listing consumers on vhost /gb/out ...
app1 <mq1@mq1.2.1554.0>      ctag2.972fffd4fe23049ad361db299b1834dc  true    10  []
app1 <mq1@mq1.2.1419.0>      ctag2.241b42bc13a43921be019d2ddf3f5302  true    10  []
gb.out  <mq1@mq1.2.1560.0>      ctag3.f7f58a3d7b4e932dbeae2354f9aa3cef  true    10  []
gb.out  <mq1@mq1.2.1425.0>      ctag3.adbb4ba2d2325b1844d697a7e4daee26  true    10  []
app1.daemon  <mq1@mq1.2.1548.0>      ctag1.0e2932e01eae88ff1843395cb6e956ae  true10       []
app1.daemon  <mq1@mq1.2.1413.0>      ctag1.4756e3ee9e6c6b6ed9e9330e7ce998d1  true10       []

### 刪除上述的 consumer connection
$# rabbitmqctl close_connection "<mq1@mq1.2.1413.0>" "(delete reason)"
# 但實測發現會有些問題(有待驗證)

