
```css
/* 畫腮紅 */
div {
    margin: 5px;
    padding: 5px;
    border: 1px solid;
    border-radius: 10px;
    height: 100px;
    width: 100px;

    box-shadow: rgb(255, 0, 0) 10px 10px 50px;
}
```

```css
.hidden {
    /* 完全消失 */
    display: none;
    display: block;

    /* 隱藏(留空間) */
    visibility: hidden;
    visibility: visible;
}
```

# 位置
1. position
    1. static (default)
    2. absolute(頁面移動以後, 一直處於一樣的位置) -> 要給TRLB
    3. relative (抓取TRLB)
    4. fixed (下拉不變,其餘同absolute)

2. top, right, left, button
    1. 長度
    2. %
    3. auto

3. overflow
    1. visible(default)  就讓它超過...
    2. hidden            隱藏超過部分
    3. scroll            右&下出現卷軸(無論有無超過)
    4. auto              右出現卷軸(無論有無超過)
    5. inherit           繼承自上層 or body

4. zindex
    重疊順序 (1~10), 預設為5 (10最大), 子元素會繼承自父元素, 要設定position才會有效果!
