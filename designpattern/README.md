# 設計模式相關

- [23種設計模式的趣味解釋](http://jimmy0222.pixnet.net/blog/post/37216962-%5B%E8%BD%89%E8%B2%BC%5D-23%E7%A8%AE%E8%A8%AD%E8%A8%88%E6%A8%A1%E5%BC%8F%E7%9A%84%E8%B6%A3%E5%91%B3%E8%A7%A3%E9%87%8B)



## OO 基本原則 - SOLID

### 1. SRP, Single Responsibility Principle, 單一職責原則
- A class should have only one reason to change
- 適時拆分 `職責(變化發生的原因)`
- 需求改變時, 只在一個面向影響類別(而非多面向) <-> 一個類別, 應該只有一個變化發生的原因
- 軟體設計的核心工作之一: 發現職責, 分離他們(在必要的時候)
- 如果需求變動, 必然使得類別多個面向跟著變動, 那拆分他們就比較沒意義了(就讓他們耦合在一起吧~)
- 一個物件所屬 "職責盡量單一", ex: 汽車就是汽車, 不應該也能在天上飛


### 2. OCP, Open/Close Principle, 開閉/開放原則
- Software entities(classes, modules, functions, etc.) should be open for extension but closed for modification.
- 封閉修改 開放新增
- 應對程式中頻繁變化的變化的部份做出抽象, 拒絕不成熟的抽象.
- 面對 OCP 應有的態度: 對於系統需求做出適當的提問, 做適當的思考, 用常識去認知, 直到變化發生時, 才採取行動. (別過分未雨綢繆)
- 實作 OCP 的常用設計模式為 策略模式(strategy mode) && 範本方法模式(template method mode)
- 模組化, 可插拔. ex: 汽車想提升馬力, 換引擎就好, 不應該要求連輪胎, 傳動軸等等都得換才行 


### 3. LSP, Liskov Substitution Principle, Liskov替換原則
- `子類別可在不影響 程序正確性 的原則下替換父類別`. 
- ex: 兒子幫爸爸賣車, 跟爸爸自己賣車, 對買車的人來說都是一樣的


### 4. ISP, Interface Segregation Principle, 介面隔離
- A subclass should not be forced to depend on methods that it doesnot use.
- 把各種不同功能的功能, 分離到介面.


### 5. DIP, Dependency Inversion Principle, 依賴倒轉原則
- 高階模組 不應該依賴 低階模組, 兩者都應該依賴在抽象之上. 
- ex: 精品商店說他們賣精品, 但卻不會說死他們是在賣鑽石或是高檔包包
- ex: 使用 `Shape s = new Circle();`, 但別用 `Circle c = new Clrcle();`
- 一個類別越可能改變, 依賴它越可能出現問題!!!
- DIP 可應用在任何「一個類別 向 另一個類別 發送訊息」的地方
- 之所以稱作 倒轉 是因為 傳統軟體開發時, 總是傾向建立 高層模組依賴於低層模組/策略依賴於細節. 然後把前面所述的實作細節包成 function, 其它程式再來使用

ex: 開關(Button) 與 電燈(Lamp)

一般會認為是: Button depends on Lamp
Button 有個 turn() 來操作 Lamp

```py
class Lamp:
    def on(self): pass  # 實作
    def off(self): pass  # 實作

class Button:
    def turn(self, lamp: Lamp):
        if condition:
            lamp.on()
        else:
            lamp.off()
```

上面就把 開關燈策略 依賴於 開關燈的操作細節了
但其實, 開關燈是個策略, 將來也有可能透過 遠端操作開關燈/語音操作開關燈/AI判斷開關燈
所以概念上需要把 能夠開關燈的實體東西(Button) 與 可以作開關燈動作的東西 分離出來
需要有個 IButton 的介面, 裡面有 turnOn() 及 turnOff()
然後 Button 依賴於此介面

```py
class IButton:  # 這是個介面
    def on(): pass  # 虛方法
    def off(): pass  # 虛方法

class Lamp(IButton):
    def on(self): pass  # 實作
    def off(self): pass  # 實作

class Button:
    def turn(self, item: IButton):
        if condition:
            item.on()
        else:
            item.off()
```

# 設計模式

- 簡單工廠模式
- 策略模式



# 其他

```bash
### 增加到環境變數
$# export PYTHONPATH=src
```

