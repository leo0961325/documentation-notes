-- 樞紐分析表 ******************************
-- https://www.postgresql.org/docs/11/tablefunc.html


DROP TABLE IF EXISTS demo_pivot;

CREATE TABLE IF NOT EXISTS demo_pivot (
    deptno INT,
    job VARCHAR(64),
    sal DECIMAL(12, 2)
);

INSERT INTO demo_pivot VALUES (10, 'CLERK'     ,2031.25);
INSERT INTO demo_pivot VALUES (10, 'MANAGER'   ,3828.13);
INSERT INTO demo_pivot VALUES (10, 'PRESIDENT' ,7812.50);
INSERT INTO demo_pivot VALUES (20, 'ANALYST'   ,4687.50);
INSERT INTO demo_pivot VALUES (20, 'MANAGER'   ,4648.44);
INSERT INTO demo_pivot VALUES (20, 'CLERK'     ,1250.00);
INSERT INTO demo_pivot VALUES (20, 'CLERK'     ,1718.75);
INSERT INTO demo_pivot VALUES (20, 'ANALYST'   ,4687.50);
INSERT INTO demo_pivot VALUES (30, 'SALESMAN'  ,1953.13);
INSERT INTO demo_pivot VALUES (30, 'SALESMAN'  ,2343.75);
INSERT INTO demo_pivot VALUES (30, 'SALESMAN'  ,2500.00);
INSERT INTO demo_pivot VALUES (30, 'MANAGER'   ,4453.13);
INSERT INTO demo_pivot VALUES (30, 'SALESMAN'  ,1953.13);
INSERT INTO demo_pivot VALUES (30, 'CLERK'     ,1484.38);

-- 上面都在建資料 **********************************


-- 資料庫 需先啟用 tablefunc 模組, 才可使用 crosstab()
CREATE EXTENSION tablefunc;


-- 查詢
SELECT * FROM crosstab(
  $$select deptno, job,
    count(job) AS "# of workers" 
    from demo_pivot group by deptno, job
             order by deptno,job$$ , 
  $$select distinct job from demo_pivot
    order by job$$)
AS ("dept No." int, 
    "ANALYST" text, "CLERK" text, "MANAGER" text, 
    "PRESIDENT" text, "SALESMAN" text);
