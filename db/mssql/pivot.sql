--SQL Server 開發技巧
--將資料庫的字串分解後,直接轉換成欄位
--PIVOT 與 SPLIT
-- 開發技巧-將資料庫的字串分解後_直接轉換成欄位

/*
myString
--------------------------
AAA_BBBB_CC
DDD_EEEE_FF

--結果
1		2		3
AAA		BBBB	CC
DDD		EEEE	FF
*/


--解法,利用傳統函數將字串分解,並搭配newid()讓每一個字串都有獨立代號
--Create Function---------------------------------------------------------------------
USE [tempdb]
GO

Create Function [dbo].[fnSplitString]
(	
	@uid 		uniqueidentifier,
	@string		NVARCHAR(MAX),
	@delimiter	CHAR(1)
)
RETURNS @output TABLE(uid uniqueidentifier, id int identity, splitdata NVARCHAR(MAX))
BEGIN
	declare @start int, @end int
	select @start = 1, @end = charindex(@delimiter, @string)
	while @start < len(@string) + 1 begin
		IF @end = 0
			set @end = len(@string) + 1
		
		INSERT INTO @output (uid, splitdata) VALUES(
			@uid,
			substring(@string, @start, @end - @start)
		)
		
		SET @start = @end + 1
		
		SET @end = CHARINDEX(@delimiter, @string, @start)
		
		delete from @output where splitdata = ''
		
	end
	RETURN
END
GO
--Create Function---------------------------------------------------------------------

--驗證
SELECT * FROM [dbo].[fnSplitString](newid(), 'AAA_BBBB_CC','_')

/*
uid										id		splitdata
------------------------------------------------------------
CDEFB7A2-F7C4-4795-93CE-52B909C834BB	1		AAA
CDEFB7A2-F7C4-4795-93CE-52B909C834BB	2		BBBB
CDEFB7A2-F7C4-4795-93CE-52B909C834BB	3		CC
*/

-- 測試資料表
USE [tempdb]
GO

CREATE TABLE tblString(myString Varchar(1024))
GO

--新增驗證資料
INSERT INTO tblString(myString) VALUES('AAA_BBBB_CC'),('DDD_EEEE_FF')
GO

--查詢資料
SELECT * FROM tblString
GO

--結果
/*
myString
AAA_BBBB_CC
DDD_EEEE_FF
*/

--使用函數分解
SELECT uid, id, splitdata FROM tblString
CROSS APPLY [dbo].[fnSplitString](newid(), myString, '_')
GO

--結果
/*
uid										id	splitdata
D4A2885D-16FD-4F6E-934E-7E945EB2B236	1	AAA
D4A2885D-16FD-4F6E-934E-7E945EB2B236	2	BBBB
D4A2885D-16FD-4F6E-934E-7E945EB2B236	3	CC
18EA0508-634F-4235-90D5-2FC85139047D	1	DDD
18EA0508-634F-4235-90D5-2FC85139047D	2	EEEE
18EA0508-634F-4235-90D5-2FC85139047D	3	FF
*/

--使用樞紐
SELECT t.[1], t.[2], t.[3]
FROM (Select uid, id, splitdata From tblString Cross Apply [dbo].[fnSplitString](newid(), myString, '_')) As SftSales
PIVOT(Max(splitdata) 					--使用彙總函數
		For id In ([1], [2], [3])) t	--資料集別名

--結果
/*
1		2		3
AAA		BBBB	CC
DDD		EEEE	FF
*/