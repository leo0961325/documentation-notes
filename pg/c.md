# C

- 2019/01/25
- [Windows 安裝 Gcc 編譯器 - MinGW](http://blog.jex.tw/blog/2013/12/17/windows-install-gcc-compiler-mingw/)

(這邊是讀 Redhat 6.2 版的老書... 無意間喵到的, 老書要丟, 有點捨不得, 所以筆記下來...)

現今多數 Linux 都是用 C 語言來撰寫, Linux 的 `GUNC compiler` 可用 `gcc` 來驅動

Windows 10 要寫 C 的話, 我自己選擇安裝 `MinGW`

底下是個 **hello.c** 的檔案

```c
#include <stdio.h>
main()
{
    printf ("Hello, World!\n");
}
```

要執行它的話

```sh
# 請 gunc 編譯 hello.c, 產生 hello 可執行檔
$# gcc -o hello hello.c

# run it!
$# ./hello
Hello, World!
```

Fuck! I know how to program C language now!!
