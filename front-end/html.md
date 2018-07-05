# HTML
[HTML Head](https://www.w3schools.com/html/html_head.asp)


-------------------------------

[jQuery CDN](https://www.w3schools.com/JQuery/jquery_get_started.asp)

```html
<script
  src="https://code.jquery.com/jquery-3.3.1.min.js"
  integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8="
  crossorigin="anonymous">
</script>
```

----------------------------

meta的妙用: 每隔30秒頁面重新刷新
```html
<meta http-equiv="refresh" content="30">
```

---------------------------

設定可視區為設備寬度, 初始大小為1.0
手機瀏覽時, 假設有圖片, 圖片可以以較佳的寬度呈現
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

-----------------------

[歷史包袱-與IE的相容模式](http://blog.darkthread.net/post-2016-05-26-x-ua-compatible-setting.aspx)
讓網頁與IE Edge相容
```html
<meta http-equiv="X-UA-Compatible" content="IE=edge">
```

----------------

JS 聖經 - 15.10.4 可編輯的內容

html5 屬性: `contenteditable` 可作拼字檢查
```html
<div id="editor" contenteditable>
    Click to edit
</div>

----------------------