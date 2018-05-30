# 時間作業
- 2018/05/28


## 不是很重要又有點重要的名詞
- Coordinated Universal Time (UTC) : 層一度被稱為 GMT
- Greenwich Mean Time (GMT)
- Daylight Saving Time (DST) : 日光節約時間
- epoch : 從 某個參考時間點(1970/1/1 00:00:00) 到 現在 的時間間隔(秒) 經過的秒數
- a tuple of nine integers : 九個整數的一個元組


## Python關於時間的模組
- 底層 C Library : time
- Python標準程式庫 : datetime, sched, calendar 
- 第三方模組 : dateutil, pytz



# time
- 支援 本地時間 及 日光節約時間, 但受限於底層 C library


## time 這東西的計算, 有兩種方式
1. 從 epoch起算的秒數
2. 用 9個整數的一個元組, 稱之為一個 `timetuple` , 此為 `struct_time`. 

Defination | attribute | range
---------- | --------- | -----------
Year       | tm_year   | [1970, 2038]
Month      | tm_mon    | [1, 12]
Day        | tm_mday   | [1, 31]
Hour       | tm_hour   | [0, 23]
Minute     | tm_min    | [0, 59]
Second     | tm_sec    | [0, 61] (60, 61 用於潤秒)
Weekday    | tm_wday   | [0, 6] (0為週一)
Year day   | tm_yday   | [1, 366] (年中的日編號)
DST        | tm_isdst  | [-1, 1] (-1代表程式庫決定 DST)



