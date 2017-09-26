# 改變Windows command的預設字碼頁

因為cmd預設為MS950來顯示, 常常顯示utf-8編碼的文件會呈現亂碼

所以以下列方式來改變code page

[模式編碼切換](https://viajamos.wordpress.com/2010/03/22/command-line-%E6%A8%A1%E5%BC%8F%E7%B7%A8%E7%A2%BC%E5%88%87%E6%8F%9B/)

c:\> chcp /?

- 改變code page至Big5
c:\> chcp 950

- 改變code page至utf-8
	1. 改變編碼頁
	c:\> chcp 65001

	2.更改字形為True Type console

