# HTML - form
- 2018/07/05



# method 屬性
- GET (default)
- POST

```html
<form method="GET">
    xxx
</form>
```


# enctype 屬性

- [Example of multipart/form-data](https://stackoverflow.com/questions/4238809/example-of-multipart-form-data)
- [What should a Multipart HTTP request with multiple files look like?](https://stackoverflow.com/questions/913626/what-should-a-multipart-http-request-with-multiple-files-look-like)
- [What does enctype='multipart/form-data' mean?](https://stackoverflow.com/questions/4526273/what-does-enctype-multipart-form-data-mean/28380690#28380690)
- [form enctype=""](https://html.com/attributes/form-enctype/)
- [W3CRecommendation - Form](https://www.w3.org/TR/html5/sec-forms.html#element-attrdef-form-enctype)


```html
<form enctype="application/x-www-form-urlencoded">
    xxx
</form>
```

前端 form 送 POST, 有下列三種方式(藉由 form 的 `enctype` 屬性) 將 data 封裝到 `request body`
1. `application/x-www-form-urlencoded` (default)
2. `multipart/form-data`
3. `text/plain`


## 1. application/x-www-form-urlencoded

所有無效的值都當成是這個 ; URL 最後的查詢字串


## 2. multipart/form-data

如果要 `透過表單上傳檔案` 必須用這個. ex:

```html
<form method="POST" enctype="multipart/form-data">
    <input type="file" name="upload"> <br> 
    <input type="submit" value="Upload File"> 
</form>
```


## 3. text/plain

發送資料但不作任何編碼(純字串), 因為難以預測, 不建議使用