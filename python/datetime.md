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
