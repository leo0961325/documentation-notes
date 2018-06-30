# 代理模式 Proxy Pattern
- 2018/06/30
- [Proxy Pattern-最易懂的設計模式解析](https://blog.csdn.net/carson_ho/article/details/54910472)
- [Runoob - 代理模式](http://www.runoob.com/design-pattern/proxy-pattern.html)

# Why? 為啥不能自己來, 而是要透過代理?

在許多情況下, 可能得訪問遠端機器, 或是存取大型檔案, 或是為了隱藏自己(安全性疑慮)...等等, 如果自己來, 可能會讓系統設計的結構變得意外的複雜. 

簡單的說, 台灣沒有 Apple專賣店, 但有 Apple代理商, 那... 妳還要飛出國去買 Apple產品嗎?

# 代理模式分類
1. 遠端代理
2. 虛擬代理 - 載入網頁時, 圖片都還沒出來, 但是圖片的空間會先被一個代理物件先預留下來, 然後再異步載入, 加速存取
3. 安全代理
4. 智慧參考


# 範例一

`Jack` 喜歡 `Mary`, 但是他太害羞不敢表達, 所以請了 `Andy` 幫他 *送花, 送巧克力, 說我愛妳*, 但是 `Mary` 不知道(也無從得知) 原來幕後是 `Jack` 在主導. ~~最後 `Andy` 就跟 `Mary` 在一起了~~



## 1. 腳色釐清
- Jack : `被代理對象` ; `被代理人` ; `真實對象` ; `最終引用的對象` ; `目標對象`
- Andy : `代理對象` ; `代理人`
- Mary : (好像沒有個特定的名詞..., 就暫時稱為 `漂亮女孩` 吧!!)



## 2. 故事分析

從上面故事得知, `代理人` 需要幫忙從事一些行為 : *送花, 送巧克力, 說我愛妳*. 

`代理人` 是誰無所謂, `代理人` 只要幫 `被代理人` *送花, 送巧克力, 說我愛妳* 給 `漂亮女孩` 就可以了. 

所以需要把 *送花, 送巧克力, 說我愛妳* 這些行為抽象出來, 然後讓 `代理人` 來實作這些行為.


## 3. C# 實作
- 介面規範  \<\<interface>>
- 漂亮女孩  Mary
- 被代理人  Jack
- 代理人    Andy
- 主程式 (客戶端)

介面(IGive) 規範:
```cs
// 抽象行為  *送花, 送巧克力, 說我愛妳* 的介面
interface IGive
{
    void GiveFlower();
    void GiveChocoloat();
    void SayILoveYou();
}
```

漂亮女孩 Mary
```cs
class BeautifulGirl
{
    public string name;
}
```

被代理人 Jack
```cs
// 被代理人 Jack (他才是真正的追求者) 只是他是 sula 不敢自己來
class Pursuit : IGive
{
    BeautifulGirl mm;

    public Pursuit(BeautifulGirl mm)
    {
        this.mm = mm;
    }

    public void GiveFlower()
    {
        Console.WriteLine("不敢送花");
    }

    public void GiveChocoloat()
    {
        Console.WriteLine("不敢送巧克力");
    }

    public void SayILoveYou()
    {
        Console.WriteLine("不敢說我愛妳");
    }
}
```

代理人 Andy
```cs
// 代理人 Andy 要幫忙實作這些介面行為
class Proxy : IGive
{
    Pursuit sula;   // 代理對象 對 真實對象 進行封裝

    public Proxy(BeautifulGirl mm)
    {
        this.sula = new Pursuit(mm);
    }

    public void GiveFlower()
    {
        // 代理對象 可以在執行 真實對象 操作時, 附加其他操作(封裝起來操作)
        Console.WriteLine("送花");
        // 代理人還可以幫忙做其他事情~~
    }

    public void GiveChocoloat()
    {
        Console.WriteLine("送巧克力");
        // 代理人還可以幫忙做其他事情~~
    }

    public void SayILoveYou()
    {
        Console.WriteLine("說我愛妳");
        // 代理人還可以幫忙做其他事情~~
    }
}
```

主程式
```cs
class Program
{
    static void Main(string[] args)
    {
        // 有一個美麗的小女孩~ 她的名字叫做 Mary
        BeautifulGirl mm = new BeautifulGirl();
        mm.name = "Mary";

        Proxy bb = new Proxy(mm);           // 代理人 Andy
        //Pursuit bb = new Pursuit(mm);     // 被代理人 Jack

        // 帥哥 Andy 努力的 幫忙做代理
        bb.GiveFlower();
        bb.GiveChocoloat();
        bb.SayILoveYou();

        Console.Read();
    }
}
```

# 範例二

網頁載入時, 不會一開始就傻傻的載入圖片或影片, 而是會把網頁框架 && 圖片先整體載入, 之後圖片, 影片, 聲音, 等等大型檔案 先透過 `代理物件` 幫他們先把空間預留, 之後再慢慢載入即可

## C# 實作
- 介面規範      \<\<interface>>
- 真實物件      RealImage
- 代理物件      ProxyImage
- 主程式 (客戶端)

介面規範(ILoadImage)
```cs
interface ILoadImage
{
    void DisplayImage();
}
```

真實物件
```cs
class RealImage : ILoadImage
{
    private String fileName;

    public RealImage(String fileName)
    {
        this.fileName = fileName;
        LoadingImageFromDisk(fileName);
    }

    public void DisplayImage()
    {
        Console.WriteLine("把圖片秀出來");
    }

    private void LoadingImageFromDisk(String fileName)
    {
        Console.WriteLine("從磁碟慢慢載入圖片");
    }
}
```

代理物件
```cs
class ProxyImage : ILoadImage
{
    private String fileName;
    RealImage realImage;

    public ProxyImage(String fileName)
    {
        this.fileName = fileName;
    }

    public void DisplayImage()
    {
        if (realImage == null)
        {
            realImage = new RealImage(fileName);
        }
        realImage.DisplayImage();
    }
}
```

主程式
```cs
class Program
{
    static void Main(string[] args)
    {
        ILoadImage pp = new ProxyImage("abc.png");
        pp.DisplayImage();

        Console.Read();
    }
}
```

# 範例三

台灣沒賣 Mac產品, 台灣沒有直營店, 但有代購業者代買~  所以直接找代購

## C# 實作
- 介面規範
- 真實物件(我)
- 代理物件
- 主程式 (客戶端)

介面
```cs
interface Subject
{
    void BuyMac();
}
```

真實物件(我)
```cs
class RealSubject : ISubject
{
    public void BuyMac()
    {
        Console.WriteLine("去買Mac");
    }
}
```

代理物件
```cs
class ProxySubject : ISubject
{
    public void BuyMac()
    {
        RealSubject r = new RealSubject();
        r.BuyMac();
        this.WrapMac();     // 封裝真實物件後, 額外幫忙做其他事情
    }

    private void WrapMac()
    {
        Console.WriteLine("把 Mac 包裝起來");
    }
}
```

主程式
```cs
class Program
{
    static void Main(string[] args)
    {
        ProxySubject p = new ProxySubject();
        p.BuyMac();

        Console.Read();
    }
}
```
