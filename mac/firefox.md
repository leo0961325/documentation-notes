# Firefox

- [](https://support.mozilla.org/bm/questions/799046)


touchpad 無法在 firefox 上頭正常使用的解法:

- new tab `about:config`
- 搜尋 `browser.gesture`
- 設定 browser.gesture.pinch.in Value = cmd_fullZoomReduce
- 設定 browser.gesture.pinch.in.shift Value = cmd_fullZoomReset
- 設定 browser.gesture.pinch.latched Value = false
- 設定 browser.gesture.pinch.out Value = cmd_fullZoomEnlarge
- 設定 browser.gesture.pinch.out.shift Value = cmd_fullZoomReset
