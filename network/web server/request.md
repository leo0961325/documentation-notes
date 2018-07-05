# request



## multipart/form-data
- 2018/07/05
- [Example of multipart/form-data](https://stackoverflow.com/questions/4238809/example-of-multipart-form-data)

`multipart/form-data` 為 `request body` 的其中一種 `content type`, 若是這樣的話, 


## enctype
- 2018/07/05
- [form enctype=""](https://html.com/attributes/form-enctype/)
- [W3CRecommendation - Form](https://www.w3.org/TR/html5/sec-forms.html#element-attrdef-form-enctype)

前端 form 送 POST, 有下列三種方式(藉由 form 的 `enctype` 屬性) 將 data 封裝到 `request body`
- `application/x-www-form-urlencoded` : 預設, 所有無效的值都當成是這個 ; URL 最後的查詢字串
- `multipart/form-data` : 如果 user 要透過表單上傳檔案(`<input type="file">`), 必須用這個
- `text/plain` : 發送資料但不作任何編碼(純字串), 因為難以預測, 不建議使用

```html
<form action="fileupload.php" method="post" enctype="multipart/form-data"> 
    <p>
        Please select the file you would like to upload. 
        <input type="file" name="upload"> 
        <br> 
        <input type="submit" value="Upload File"> 
    </p>
</form>
```