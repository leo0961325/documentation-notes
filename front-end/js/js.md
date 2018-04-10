

```js
var a;

if (!a) {   // 只有6種情況, a = false
    // undefined
    // null
    // 0
    // -0
    // NaN
    // "" (空字串)
}
```


```js
function say(word) {
    console.log(1);
    log(word);
    console.log(2);
}

function exec(some, value) {
    console.log(3);
    some(value);
    console.log(4);
}

exec(say, 'QQ');

3
1
QQ
2
4
```


> 每個 HTML Element都有 `id`

> 每個 Element都有 `style` 及 `className`


```
DOM
 |- Elements
 |- Text Nodes
```