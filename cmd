Linux指令
--------------------------------------------------
ps相關

$ ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head
印出程序使用狀況
pid:行程
ppid:父行程
-e:所有行程資訊
-o:指定輸出欄位
%mem, %cpu: 用量百分比
--------------------------------------------------
find相關
https://blog.gtwang.org/linux/unix-linux-find-command-examples/

$find . -iname xx.txt
在目前dir底下,忽略大小寫找出所有xx.txt

$ find . -type f ! -perm 777
-perm:指定檔案權限

$ find . -perm /u=r
列出唯獨的檔案

$ find . -perm /a=x
列出可執行的檔案

$ find . -type d -name xx
d:目錄
p:具名的pipe(FIFO)
f:一般檔案
l:連結檔
s:socket檔案


