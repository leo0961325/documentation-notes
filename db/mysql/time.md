# 關於時間

- [adding 30 minutes to datetime php/mysql
](https://stackoverflow.com/questions/1436827/adding-30-minutes-to-datetime-php-mysql?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa)


```sql

SELECT CURRENT_TIMESTAMP;
SELECT CURRENT_TIMESTAMP + INTERVAL 10 SECOND;  # +10 seconds
SELECT CURRENT_TIMESTAMP + INTERVAL 10 MINUTE;  # +10 minutes
SELECT CURRENT_TIMESTAMP + INTERVAL 10 HOUR;
SELECT CURRENT_TIMESTAMP + INTERVAL 10 DAY;
SELECT CURRENT_TIMESTAMP + INTERVAL 10 MONTH;
SELECT CURRENT_TIMESTAMP + INTERVAL 10 YEAR;

```