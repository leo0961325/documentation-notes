# Document coordinate && Viewport coordinate(Window coordinate)
- 2018/01/03
- JavaScript 6E, Ch 15.8筆記

---

> document.compatMode == 'CSS1Compat'者, 使用 document前者 <br />
> document.compatMode == 'BackCompat'者, 使用 document後者, 怪異模式(quirks mode)

## Window 與 Document

window |  document | 說明
--- | --- | --- 
w.pageXOffset<br>w.pageYOffset | d.documentElement.scrollLeft<br>d.documentElement.scrollTop<br>(非怪異模式) `'CSS1Compat'`<br><br>d.body.scrollLeft<br>d.body.scrollTop<br>(怪異模式) `'Backcompat'` | 向右下捲動多少
w.innerWidth<br>w.innerHeight | d.documentElement.clientWidth<br>d.documentElement.clientHeight<br>(非怪異模式) `'CSS1Compat'`<br><br>d.body.scrollWidth<br>d.body.scrollHeight<br>(怪異模式) `'Backcompat'` | viewport大小
 - | d.documentElement.offsetWidth<br>d.documentElement.offsetHeight | (與上列作比較)
 - | d.documentElement.offsetLeft<br>d.documentElement.offsetTop | -
w.scrollLeft<br>w.scrollTop | - | IE Only 
w.screenX<br>w.screenY | - | Monitor左上角座標
w.outerWidth<br>w.outerHeight | - | viewport + 工具列 + 邊框等等的大小

## Element
> 分為 offset, client, scroll系列的特性...

### 特性
特性 | 回傳值 | 說明
--- | --- | ---
e.clientLeft<br>e.clientTop |  | (不是非常有, 別理它)
e.scrollLeft<br>e.scrollTop |  | -
e.offsetWidth<br>e.offsetHeight |  | Element大小 + padding+border
e.clientWidth<br>e.clientHeight |  | Element大小 + padding (不含捲動軸)
e.scrollWidth<br>e.scrollHeight | Element大小 + padding + 任何溢位內容大小

### 方法
 e.getBoundingClientRect() : *{top:t, left:l, right:r, bottom:b}*

 方法 | 說明
--- | ---
e.getBoundingClientRect()<br>return `DOMRect`<br><br>e.getClientRects()<br> return `DOMRectList` | 得到 (left, right, top, bottom)的物件 (viewport 座標)<br><br>行內的個別矩形
e.offsetLeft<br>e.offsetTop | 回傳 Element的 X, Y座標<br>對多數 Element, 取得的是 `文件座標`<br>對某些Element(ex: td、已經定位的元素), 取得的是 `相對於 parent的文件座標`