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


# 怎麼在 Windows 10 設定環境變數

- 使用者環境變數
- 系統環境變數 -> 右鍵 以系統管理員身分執行


```sh
# 一般使用者的 Command Line
# 設定 環境變數
$ set uu=tony

$ echo %uu%
tony

# 設定 共用環境變數
$ setx uu "Tony"
成功: 已經儲存指定的值。

# 開其他的 Command Line
$ echo %uu%
Tony
# 前往 環境變數>編輯您的帳戶的環境變數>使用者變數 裏頭, 就找得到 uu 這東西了
```
