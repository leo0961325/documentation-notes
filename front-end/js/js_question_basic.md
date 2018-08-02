# javascript 基本題

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


