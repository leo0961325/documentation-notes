# 工廠模式
- 以 C#實作, 以 Java風格撰寫
- 2018/02/18

> 用一個 `單獨類別的靜態方法` 來作創造實體, 分離 **業務邏輯** 與 **介面邏輯**

> Note: 違背了開放封閉原則

> 

靜態工廠
```cs
public class OperationFactory {
    public status Operation createOperate(string ii) {
        Operation oper = null;
        switch (ii) {
            case "+":
                oper = new OperationAdd();
            case "-":
                oper = new OperationSub();
            case "*":
                oper = new OperationMul();
            case "/":
                oper = new OperationDiv();
        }
        return oper;
    }
}
```

類別工廠
```cs
public class Operation {
    private double _numberA = 0;
    private double _numberB = 0;
    private double result = 0;

    public double numberA {
        get { return _numberA; }
        set { _numberA = value; }
    }

    public double numberB {
        get { return _numberB; }
        set { _numberB = value; }
    }

    public virtual double getResult() {
        return result;
    }
}


class OperationAdd : Operation {
    public override double getResult() {
        result = NumberA + NumberB;
        return result;
    }
}


class OperationSub : Operation {
    public override double getResult() {
        result = NumberA - NumberB;
        return result;
    }
}


class OperationMul : Operation {
    public override double getResult() {
        result = NumberA * NumberB;
        return result;
    }
}


class OperationDiv : Operation {
    public override double getResult() {
        if (NumberB == 0) {
            torow new Exception("除數不能為0");
        }
        result = NumberA / NumberB;
        return result;
    }
}

// ********** 擴展 ********** //
class OperationSqr : Operation {
    public override double getResult() {
        result = Math.sqrt(NumberA, NumberB);
    }
}
```

客戶端
```cs
Operation oper;
oper = OperationFactory.createOperate("+");
oper.NumberA = 2;
oper.NumberB = 3;
double result = oper.getResult();
```