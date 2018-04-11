

> modules為 js library, 可在 project中 include. node中, 所有 `事件特性` 及 `方法` 都是 `EventEmitter物件` 的實例.

```js
var ev = require('events');
var ee = new ev.EventEmitter();
```