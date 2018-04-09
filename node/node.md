

### import/export

---
movies.js
```js
function printA() {
	console.log("A");
}

function printB() {
	console.log("B");
}

// printA 匯出, 為public function
module.exports.ppA = printA;

// printB 未匯出, 為private function
```

main.js
```js
movie = require('./movies');
movie.ppA();
```

```sh
A
```
---


