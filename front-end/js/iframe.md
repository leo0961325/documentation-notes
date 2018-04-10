# IFrame

> 遠古時代的遺跡

```html
<iframe id="myframe"></frame>
```

```js
var x = document.getElementById('myframe');
var y = (x.contentWindow || x.contentDocument);
if (y.document) {
    y = y.document; // or y = x.contentDocument;
}
y.body.style.backgroundColor = 'red';
```


-------------------------------------


```html




<iframe id="f1" name="ff1">
```
```js
f1 === ff1.frameElement
    === frames[0].frameElement
    === frames['f1']
    === frames.f1

//
iframe.contentWindow === window.frame.Element
```