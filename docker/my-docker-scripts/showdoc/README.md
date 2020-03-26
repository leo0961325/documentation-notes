# 透過 Docker 安裝 showdoc

- 2020/03/26
- [Docker安裝方式](https://www.showdoc.cc/help?page_id=65610)

```bash
docker pull star7th/showdoc

### 環境 (權限若要控制的話, 後續再來開必要的就好...)
mkdir -p ./showdoc_data/html
chmod -R 777 ./showdoc_data

### 測試用
docker run --rm \
    -p 4999:80 \
    --name myshowdoc \
    star7th/showdoc

### 用久執行用 (無有 SELinux 問題的話, 再把底下的 「:Z」拿掉)
docker run -d \
    -p 4999:80 \
    -v ./showdoc_data/html:/var/www/html:Z \
    --name myshowdoc \
    star7th/showdoc
```
