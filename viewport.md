# Document coordinate && Viewport coordinate(Window coordinate)
- 2018/01/03
- JavaScript 6E, Ch 15.8筆記

---

## 表1
window        | document
------------- | ---
w.pageXOffset | d.`documentElement.scrollLeft` <br />d.`body.scrollLeft`
w.pageYOffset | d.`documentElement.scrollTop` <br /> d.`body.scrollTop`

查詢視窗的捲動軸位置

---

## 表2
window        | document
------------- | ---
w.innerWidth  | d.`documentElement.clientWidth` <br />d.`body.clientWidth`
w.innerHeight | d.`documentElement.clientHeight` <br /> d.`body.clientHeight`

查詢視窗的 viewport大小

> 表1、表2, 左右方法互為替代 <br />
> document.compatMode == 'CSS1Compat'者, 使用 document前者 <br />
> document.compatMode == 'BackCompat'者, 使用 document後者, 怪異模式(quirks mode)