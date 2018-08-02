# moment.js
- [moment.js documentation](https://momentjs.com/docs)
- 2018/07/12


# 時間解析 Parse

## Now

```js
var d = new Date();
// Thu Jul 12 2018 14:57:59 GMT+0800 (台北標準時間)

var m = moment(d);
m.toString();
// "Thu Jul 12 2018 14:57:59 GMT+0800"

// 驗證時間格式是否正確
m.isValid();
// return true/false


```

## String

從 `時間字串` 建立 `moment物件`, 依照下面先後順序判斷
1. `ISO8601`
2. `RFC2822 Date time`
3. `new Date(string)` : 瀏覽器們 對於 時間解析的實作並未統一, 所以最好要指定 `format`

### 1. [ISO8601](https://en.wikipedia.org/wiki/ISO_8601)

```js
// 2013-02-08  # A calendar date part
// 2013-W06-5  # A week date part
// 2013-039    # An ordinal date part

// 20130208    # Basic (short) full date
// 2013W065    # Basic (short) week, weekday
// 2013W06     # Basic (short) week only
// 2013050     # Basic (short) ordinal date

// 2013-02-08T09            # An hour time part separated by a T
// 2013-02-08 09            # An hour time part separated by a space
// 2013-02-08 09:30         # An hour and minute time part
// 2013-02-08 09:30:26      # An hour, minute, and second time part
// 2013-02-08 09:30:26.123  # An hour, minute, second, and millisecond time part
// 2013-02-08 24:00:00.000  # hour 24, minute, second, millisecond equal 0 means next day at midnight

// 20130208T080910,123      # Short date and time up to ms, separated by comma
// 20130208T080910.123      # Short date and time up to ms
// 20130208T080910          # Short date and time up to seconds
// 20130208T0809            # Short date and time up to minutes
// 20130208T08              # Short date and time, hours only

// 2013-02-08 09  # A calendar date part and hour time part
// 2013-W06-5 09  # A week date part and hour time part
// 2013-039 09    # An ordinal date part and hour time part

// 2013-02-08 09+07:00            # +-HH:mm
// 2013-02-08 09-0100             # +-HHmm
// 2013-02-08 09Z                 # Z
// 2013-02-08 09:30:26.123+07:00  # +-HH:mm
// 2013-02-08 09:30:26.123+07     # +-HH
```


### 2. [RFC2822](https://tools.ietf.org/html/rfc2822#section-3.3)

```js
// 6 Mar 17 21:22 UT
// 6 Mar 17 21:22:23 UT
// 6 Mar 2017 21:22:23 GMT
// 06 Mar 2017 21:22:23 Z
// Mon 06 Mar 2017 21:22:23 z
// Mon, 06 Mar 2017 21:22:23 +0000
```

### 3. String + Format

```js
// moment(String, String);
// moment(String, String, String);
// moment(String, String, Boolean);
// moment(String, String, String, Boolean);

moment("12-25-1995", "MM-DD-YYYY");
```

Format 格式如下:

Input    | Example        | Description
-------- | -------------- | -------------------
YYYY     | 2014           | 4 or 2 digit year
YY       | 14             | 2 digit year
Q        | 1..4           | Quarter of year. Sets month to first month in quarter.
M MM     | 1..12          | Month number
MMM MMMM | Jan..December  | Month name in locale set by moment.locale()
D DD     | 1..31          | Day of month
Do       | 1st..31st      | Day of month with ordinal
X        | 1410715640.579 | Unix timestamp
x        | 1410715640579  | Unix ms timestamp
H HH     | 0..23          | Hours (24 hour time)
h hh     | 1..12          | Hours (12 hour time used with a A.)
m mm     | 0..59          | Minutes
s ss     | 0..59          | Seconds
Z ZZ     | +12:00         | Offset from UTC as +-HH:mm, +-HHmm, or Z
(↑僅節錄部分)

