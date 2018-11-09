# [VSCode 套件 - Live Sass Compiler](https://marketplace.visualstudio.com/items?itemName=ritwickdey.live-sass)
- 2018/08/13
- VSCode版本 1.25.0
- 套件版本 3.0.0
- 會自動安裝的相依套件 [Live Server v5.1.1](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)
- [What's the difference between SCSS and Sass?](https://stackoverflow.com/questions/5654447/whats-the-difference-between-scss-and-sass)


# Sass Compiler 及 Live Server 簡易用法

## 1. 安裝上述的 2 個套件
    - Live sass compiler
    - Live Server


## 2. 建立 scss 資料夾, 裡面放 test.scss, 專案架構如下:

```
/scss
    test.scss
test.html
```

test.scss 如下:
```scss
$c1 : rgb(100, 100, 50);
$c2 : rgb(50, 100, 100);

html {
    background-color: $c1;
}

div {
    background-color: $c2;
    height: 200px;
    width: 200px;
}
```


## 3. 寫好 test.html

```html
<head>
    <link href="scss/test.css" rel="stylesheet">
</head>
<body>
    <div></div>
</body>
```


## 4. 開始使用~

### 4-1. 點選 VSCode 右下角的 `Watch Sass`

假設都沒有動過設定檔, 則專案架構會變成

```
/scss
    test.css
    test.css.map        ← 多出來的
    test.scss           ← 多出來的
test.html
```


### 4-2. 點選 VSCode 右下角的 `Go Live`

瀏覽器會開啟專案, 點選 `test.html`, 日後改寫 css 的話, 只要去動 `test.scss`, 存檔後, 便可立即套用到瀏覽器上.


### 4-3. 結束

點選 `Watching...`

點選 `Port:5500`



# 自訂設定檔的玩法

初始專案架構:
```
/scss
    test.scss
test.html
```

settings.json
```js
{
    "liveSassCompile.settings.formats": [
        {
            "format": "expanded",       // 未經壓縮的css
            "extensionName": ".css",
            "savePath": "/style"
        },
        {
            "format": "compressed",     // .min.css (取消空白及換行)
            "extensionName": ".css",
            "savePath": "/dist"
        }
    ]
}
```

`Watch Sass` 之後, 專案架構變成這樣:
```
/scss
    test.scss
/dist
    test.css
    test.css.map
/style
    test.css
    test.css.map
test.html
```

`test.html` 使用 compressed 版的 css 吧
```html
<head>
    <link href="dist/test.css" rel="stylesheet">
</head>
<body>
    <div></div>
</body>
```
