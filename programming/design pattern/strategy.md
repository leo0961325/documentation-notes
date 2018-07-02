# Strategy Mode 策略模式
- 2018/07/02

- [[Design Pattern] 策略模式 (Strategy Pattern) 把跑車行為裝箱吧](https://dotblogs.com.tw/joysdw12/archive/2013/03/07/95769.aspx)

## 定義

> **`策略模式(Strategy)`** : 定義了`演算法家族`, `分別封裝`起來, 讓他們之間可以`相互替換`, 此模式讓`演算法的變化, 不會影響到使用演算法的客戶`. (from DP 聖經)



## 範例

阿利博士 成立了 智慧機器人股份有限公司, 裏頭專門研發機器人, 機器人可以幫忙做很多事情~  而機器人研發, 以`主菜`為主

所有機器人, 需要來時做 IMachine
```cs
interface IMachine
{
    void SpeedUp();     // 加速
    void SpeedDown();   // 減速
    void UseItem();     // 用工具
}
```

考量到所有機器人, 加速減速的方式都不同, 所以又開了另一批的介面...
```cs
interface ISpeedUp      // 加速介面
{
    void SpeedUp();
}

interface ISpeedDown    // 減速介面
{
    void SpeedDown();
}

interface IUseItem      // 用工具介面
{
    void UseItem();
}
```

```cs
class BigFire : ISpeedUp        // 實作 加速
{
    public void SpeedUp()
    {
        Console.WriteLine("大火快炒~~");
    }
}

class MultiHands : ISpeedUp        // 實作 加速
{
    public void SpeedUp()
    {
        Console.WriteLine("使用四隻手, 開多線呈煮飯");
    }
}

class SmallFire : ISpeedDown        // 實作 減速
{
    public void SpeedDown()
    {
        Console.WriteLine("小火慢慢來");
    }
}

class CutVegetables : IUseItem        // 實作 用工具
{
    public void UseItem()
    {
        Console.WriteLine("用刀切菜~~ 切切切切...");
    }
}
```

煮飯機器人類別
```cs
class CookingMachine : IMachine     // 煮飯機器人, 但因為是機器人, 都得實作 IMachine
{
    private ISpeedUp _speedUp;
    private ISpeedDown _speedDown;
    private IUseItem _useItem;

    public CookingMachine(ISpeedUp speedUp, ISpeedDown speedDown, IUseItem useItem)
    {
        this._speedUp = speedUp;
        this._speedDown = speedDown;
        this._useItem = useItem;
    }

    public void SpeedDown()         // 實作 IMachine 加速
    {
        this._speedDown.SpeedDown();
    }

    public void SpeedUp()           // 實作 IMachine 減速
    {
        this._speedUp.SpeedUp();
    }

    public void UseItem()           // 實作 IMachine 用工具
    {
        this._useItem.UseItem();
    }
}
```

主程式~ 開始煮飯囉
```cs
class Program
{
    static void Main(string[] args)
    {
        ISpeedUp u1 = new BigFire();        // 大火快炒的加速實作類別
        ISpeedDown d = new SmallFire();     // 小火慢煮的減速實作類別
        IUseItem i = new CutVegetables();   // 用刀切菜的用工具實作類別

        IMachine cookingMachine1 = new CookingMachine(u1, d, i);    // 實作 IMachine的 煮飯機器人類別: cookingMachine1
        cookingMachine1.SpeedUp();

        ISpeedUp u2 = new MultiHands();     // 使用很多手的加速實作類別
        IMachine cookingMachine2 = new CookingMachine(u2, d, i);    // 實作 IMachine的 煮飯機器人類別: cookingMachine2
        // cookingMachine1 && cookingMachine2 使用了不同的 演算法家族(ISpeedUp)
        cookingMachine2.SpeedUp();

        Console.Read();
    }
}
```

以上完工~

如果哪天阿利博士發現柯南被欺負了, 它在發明一個

打架機器人

```cs
// 這包, 只有把上面的 CookingMachine 換成 AttackingMachine
class AttackingMachine : IMachine     // 打架機器人, 但因為是機器人, 都得實作 IMachine
{
    private ISpeedUp _speedUp;
    private ISpeedDown _speedDown;
    private IUseItem _useItem;

    // 建構式也得買名字...
    public AttackingMachine(ISpeedUp speedUp, ISpeedDown speedDown, IUseItem useItem)
    {
        this._speedUp = speedUp;
        this._speedDown = speedDown;
        this._useItem = useItem;
    }

    public void SpeedDown()         // 實作 IMachine 加速
    {
        this._speedDown.SpeedDown();
    }

    public void SpeedUp()           // 實作 IMachine 減速
    {
        this._speedUp.SpeedUp();
    }

    public void UseItem()           // 實作 IMachine 用工具
    {
        this._useItem.UseItem();
    }
}
```

然後來實作各種打架時候的動作
```cs
class SuperPower : ISpeedUp        // 實作 加速
{
    public void SpeedUp()
    {
        Console.WriteLine("超頻打人~~");
    }
}

class EnergySaving : ISpeedDown        // 實作 減速
{
    public void SpeedDown()
    {
        Console.WriteLine("我在省電, 輕輕打你就好");
    }
}

class TakeFire : IUseItem        // 實作 用工具
{
    public void UseItem()
    {
        Console.WriteLine("機器人內建阿姆斯特朗砲轟炸~~~");
    }
}
```

主程式~~  然後就可以打架了
```cs
class Program
    {
        static void Main(string[] args)
        {
            ISpeedUp u1 = new BigFire();        // 大火快炒的加速實作類別
            ISpeedDown d = new SmallFire();     // 小火慢煮的減速實作類別
            IUseItem i = new CutVegetables();   // 用刀切菜的用工具實作類別

            IMachine cookingMachine1 = new CookingMachine(u1, d, i);    // 實作 IMachine的 煮飯機器人類別: cookingMachine1
            cookingMachine1.SpeedUp();

            ISpeedUp u2 = new MultiHands();     // 使用很多手的加速實作類別
            IMachine cookingMachine2 = new CookingMachine(u2, d, i);    // 實作 IMachine的 煮飯機器人類別: cookingMachine2
            cookingMachine2.SpeedUp();

            // 底下是 打架機器人
            ISpeedUp uu = new SuperPower();
            ISpeedDown dd = new EnergySaving();
            IUseItem ii = new TakeFire();
            IMachine attackMachine1 = new AttackingMachine(uu, dd, ii);
            attackMachine1.SpeedUp();
            attackMachine1.UseItem();

            Console.Read();
        }
    }
```