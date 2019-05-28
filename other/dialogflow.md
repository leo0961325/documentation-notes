# [Dialogflow 語意分析](https://console.dialogflow.com/api-client/)

- 2019/05/20


## 基本名詞

* Agent : 一個 Agent 為 一個 `語意分析模組`
* Intent : 一個 Agent 下可有多個 Intent; 預想可能發生的對話; 若符合, 則進入此 Intent
* Entity : 每個 Intent 可包含多個 Entity
    - 系統預設 Entity : date, time, 數字
    - 自定義 Entity : 例如 男生, 女人, 台中市, 滿級分, 發大財, 國防布....
* Actions & Parameters : 每個 Intent 可設定這兩個; 作為後續 回傳 && 識別 使用
* Contexts : Parameters 可用 Contexts 保存; 紀錄對話過那些內容
* Fulfillment : 如果符合所有的 Parameters 則觸發 Fulfillment, 由後端作客製化 Response

---

綜上, 一個 Agent(語意分析模組) 會有很多個 Intent(不同的對話情境), 每個 Intent 會有多個 Entity(有點專有名詞 or 特定動作 之類的概念)

