# Snippets (程式碼片段)

- 2019/01/14

ex: C# 鍵盤輸入 `prop` + <code>tab</code>


# 建立客製化 Snippets

- [Creating Code Snippets in Visual Studio Code](https://scotch.io/bar-talk/write-less-code-by-creating-snippets-in-visual-studio-code)

> File > Preferences > User Snippets > 

```js
// Example:
{
    "Print to console": {
        "prefix": "mm",
        "body": [
            "public ${1:static} ${2:void} ${3:method} (${4:type} ${5:name}) {",
                "${0}",
            "}"
        ],
        "description": "Quick start to build methods"
    },
}
```

將來 c# 使用 "mm", 就可以享有下面那包~

```cs
//         $1     $2   $3      $4   $5
    public static void method (type name) {
//      $0
    }

// $0 為最後定位位置
// 其餘依照順序用 tab 切換
```



## C#

Snippets | Description
-------- | ---------------
ctor     | Default Constructor
prop     | Property
propg    | ro Property
sim      | static int Main Method
svm      | static void Main Method


