# 核心 javascript



# if 內, false 的所有情況

```js
var a;
if (!a) {   // 只有 6 種情況, a = false
    // undefined
    // null
    // 0
    // -0
    // NaN
    // "" (空字串)
}
```



# 物件屬性

```js
// "物件屬性" 一般具有下列特性
// value
// writable
// enumerable
// configurable

// or

// getter
// setter
// enumerable
// configurable
```



# Prototype

每個js物件, 都有2個物件與之關聯
1. 原型繼承特性
2. 原型

使用 Object literal 建立的物件都有同一個`原型物件`, 我們用 `Object.prototype` 來參考這個 `原型物件`.

使用 `new Object()創建的物件` 繼承自 `Object.prototype`

ex: 使用 `new Array()建立的物件` 原型為 `Array.prototype` ; `new Date()建立的物件` 原型為 `Date.prototype`

而 `Object.prototype` 沒有原型物件



# Closure 閉包

```js
var oo = function() {
    var x = 0;
    var ii = function() {
        x = x + 1;
        return x;
        }
    return ii;
}

var q = oo()
// q 為 [Function: ii]

q();
1
q();
2
q();
3
```



```js
// 插入元素
    javascript: beforebegin     afterbegin          beforeend       afterend
                            <h1>             HI                </h1>
    jquery:     before          prepend             append          after
```