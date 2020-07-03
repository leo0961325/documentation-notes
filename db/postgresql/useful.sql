-- 以每分鐘為群組, 計算每個時間片段的筆數
SELECT
	date_trunc( 'minute', check_time ) as dt,
	COUNT(1) AS cnt
FROM
	jkb_check_data
group by 1
order by dt DESC;
-- dt                  | cnt
-- ------------------- | -------
-- 2020-07-03 11:44:00 | 60
-- 2020-07-03 11:43:00 | 49
-- 2020-07-03 11:42:00 | 46
-- 2020-07-03 11:41:00 | 50

--------------------------------------------------------

-- 產生 uuid 的 function, named `gen_random_uuid`
CREATE OR REPLACE FUNCTION "public"."gen_random_uuid"()
  RETURNS "pg_catalog"."uuid" AS '$libdir/pgcrypto', 'pg_random_uuid'
  LANGUAGE c VOLATILE
  COST 1

