# webpack

- 2019/03/26
- [webpack](https://webpack.js.org/)

> 前端框架東西很多很亂, 就讓他亂吧~ 然後可以透過某個組織檔案 (`index.js` 程式進入點), 然後透過他把關聯的東西自動連線~~~


## 安裝

```sh
### 安裝
$# mkdir webpack-demo && cd webpack-demo
$# npm init -y
$# npm install webpack webpack-cli --save-dev
```


## project

```sh
  webpack-demo
  |- package.json
+ |- index.html
+ |- /src
+   |- index.js
```

## file

### src/index.js
```js
// 這是 js 的主要檔案, index.js

import _ from 'lodash';
function component() {
  let element = document.createElement('div');
  element.innerHTML = _.join(['Hello', 'webpack'], ' ');
  return element;
}
document.body.appendChild(component());
```

### index.html
```html
<!doctype html>
<html>
  <head>
    <title>Getting Started</title>
    <script src="https://unpkg.com/lodash@4.16.6"></script>
    <!-- ↑ 到時候這行可以拿掉 -->
  </head>
  <body>
    <script src="./src/index.js"></script>
    <!-- ↑ 到時候這行可以拿掉 -->

    <script src="main.js"></script>
    <!-- ↑ 改用這個 -->
  </body>
</html>
```

### package.json

```js
  {
    "name": "webpack-demo",
    "version": "1.0.0",
    "description": "",
    "private": true,
    // "main": "index.js",
    "scripts": {
      "test": "echo \"Error: no test specified\" && exit 1"
    },
    "keywords": [],
    "author": "",
    "license": "ISC",
    "devDependencies": {
      "webpack": "^4.20.2",
      "webpack-cli": "^3.1.2"
    },
    "dependencies": {}
  }
```

###

```js
const path = require('path');

module.exports = {
    entry: './src/index.js',
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'bundle.js'
    }
}
```

```sh
### 使用 webpack 打包 index.js -> index.html
$ npm install --save lodash

###
$ npx webpack
```