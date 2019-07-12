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



# 日期與時間

格林威治標準時間(GMT) ~= UTC時間


## ISO8601標準

較新的日期API, 統一`日期時間的交換格式`, ex: `yyyy-mm-ddTHH:MM:SS.SSS`...等. **T**為 *日期*, *時間* 的分隔


## datetime模組

```py
>>> from datetime import datetime
>>> from datetime import date
>>> from datetime import time

# 以上 3者都有 isoformat()將之轉換成字串(採用ISO8601標準)
>>> now = datetime.now()
>>> now.isoformat()
'2018-04-08T15:05:57.668757'

>>> now.isoformat('@')
'2018-04-08@15:05:57.668757'

```

### 日期or時間的運算(+-計算): datetime.timedelta 方法

可以建立的時間單位有: days, seconds, hours, ...一堆

```py
>>> from datetime import datetime, timedelta
>>> datetime.now()
datetime.datetime(2018, 4, 8, 15, 14, 33, 433222)

>>> datetime.now() + timedelta(days = 5)	# 5天後
datetime.datetime(2018, 4, 13, 15, 14, 33, 576380)
```

### datetime時區, datetime.tzinfo 類別

datetime實例預設`沒有時區資訊`, 單純表示`本地時間`

```py
>>> from datetime import datetime, timezone
>>> qq = datetime(2018, 4, 8, tzinfo = timezone.utc) # qq代表 UTC時間
>>> qq
datetime.datetime(2018, 4, 8, 0, 0, tzinfo=datetime.timezone.utc)

>>> q2 = timezone(offset = timedelta(hours = 8), name = 'Asia/Taipei') # 讓 qq轉換為台灣時區
>>> q2
datetime.timezone(datetime.timedelta(0, 28800), 'Asia/Taipei')

>>> tpe = qq.astimezone(q2)
>>> tpe
datetime.datetime(2018, 4, 8, 8, 0, tzinfo=datetime.timezone(datetime.timedelta(0, 28800), 'Asia/Taipei'))
```
