

- 泛化(Generalization)
- 實現(Realization)
- 組合(Composition)
- 聚合(Aggregation)
- 關聯(Association)
- 依賴(Dependency)

強弱順序: Generalization = Realization > Composition > Aggregation > Association > Dependency


## Generalization

繼承關係, 子類別特化父類別的特徵和行為


## Realization

類別實作介面的關係


## Composition

整體與部分的關係, "部分"離開整體後, `無法`單獨存在. 

ex: 「手 + 腳 + 身體 + 頭 = 人」, 把左邊的東西拆出去後, 無法單獨工作


## Aggregation

整體與部分的關係, "部分"離開整體後, `可以`單獨存在. 

ex: 員工 與 公司


## Association

擁有的關係. Class A 知道 Class B 的屬性和方法.

關聯可以是雙向, 也可以是單向

ex: 讀者 && 書 && 作者 之間的關係


## Dependency

使用的關係. 一個類別的實現, 需要另一個類別的協助.

盡量不要讓他們變成雙向的關係!!