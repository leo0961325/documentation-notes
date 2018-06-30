# 代理模式 Proxy Pattern
- 2018/06/30
- [Proxy Pattern-最易懂的設計模式解析](https://blog.csdn.net/carson_ho/article/details/54910472)

# 範例一
## 1. 故事
> `Jack` 喜歡 `Mary`, 但是他太害羞不敢表達, 所以請了 `Andy` 幫他 *送花, 送巧克力, 說我愛妳*, 但是 `Mary` 不知道(也無從得知) 原來幕後是 `Jack` 在主導. ~~最後 `Andy` 就跟 `Mary` 在一起了~~



## 2. 腳色釐清
- Jack : `被代理對象 ; 被代理人`
- Andy : `代理對象 ; 代理人`
- Mary : `代理目標`



## 3. 故事分析

從上面故事得知, `代理人` 需要幫忙從事一些行為 : *送花, 送巧克力, 說我愛妳*. 

`代理人` 是誰無所謂, `代理人` 只要幫 `被代理人` *送花, 送巧克力, 說我愛妳* 給 `代理目標` 就可以了. 

所以需要把 *送花, 送巧克力, 說我愛妳* 這些行為抽象出來, 然後讓 `代理人` 來實作這些行為.


## 4. C# 實作
- 介面規範  \<\<interface>>
- 代理目標  Mary
- 被代理人  Jack
- 代理人    Andy
- 主程式

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

代理目標 Mary
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
    Pursuit sula;

    public Proxy(BeautifulGirl mm)
    {
        this.sula = new Pursuit(mm);
    }

    public void GiveFlower()
    {
        Console.WriteLine("送花");
    }

    public void GiveChocoloat()
    {
        Console.WriteLine("送巧克力");
    }

    public void SayILoveYou()
    {
        Console.WriteLine("說我愛妳");
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



```
              --------------------
              |   <<interface>   |
              |                  |
              |                  |
              --------------------
                   ^        ^
                  /          \
                 /            \
                /              \
               /                \
--------------------        --------------------
|   Jack           |       |   Andy            |
|                  |  ---> |                   |
|                  |       |                   |
--------------------       ---------------------
```

------------------------------------------------------------------