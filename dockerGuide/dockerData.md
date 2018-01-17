# [Manage application Data](https://docs.docker.com/v17.09/engine/admin/volumes/)
- 2018/01/12

## 概述
Docker Container內, 如果儲存東西, Container經過重新啟動後, 內部資料都會消失, 因而衍生把資料拋出 Container外

### 拋出資料的3種方式:
1. volumes (最佳方式)
2. bind mounts
3. tmpfs volumes

