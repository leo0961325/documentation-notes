# 統計分配 Distribution
- 2018/06/30
- [markdown-math](https://blog.csdn.net/u013698770/article/details/55210693)
- [VSCode - Math in MarkDown](https://github.com/cben/mathdown/wiki/math-in-markdown)
- [numpy - exponential](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.exponential.html)
- [Writing Mathematic Formulars in Markdown](http://csrgxtu.github.io/2015/03/20/Writing-Mathematic-Fomulars-in-Markdown/)
- [Cmd Markdown 公式指导手册](https://www.zybuluo.com/codeep/note/163962#14%E5%A4%A7%E6%8B%AC%E5%8F%B7%E5%92%8C%E8%A1%8C%E6%A0%87%E7%9A%84%E4%BD%BF%E7%94%A8)

# 相依套件
> 採用 `VSCode + Markdown+Math 2.2.1` 來撰寫, 沒裝這個的人底下看起來會亂糟糟 @_@

# [Binomial distribution](https://zh.wikipedia.org/wiki/%E4%BA%8C%E9%A0%85%E5%88%86%E4%BD%88)

若 x 為嘗試 n 次獨立實驗, 發生偶發事件(成功機率p, 失敗機率q) 的 `成功次數`. 如此可寫成 : `x~B(n,x)`

pdf:

$$f_ {x} (x) = {n\choose x} \cdot p^x \cdot q^{n-x} , x=0, 1, ..., n$$

cdf: 

$$F_ {x} (x) = \sum_{i=0}^x {n\choose x} \cdot p^x \cdot q^{n-x} , x=0, 1, ..., n$$

Mean:

$$E(x) = np$$

Variance:

$$V(x) = npq$$



# [Exponential distribution](https://zh.wikipedia.org/wiki/%E6%8C%87%E6%95%B0%E5%88%86%E5%B8%83)

若 x 為發生偶發事件的次數, 偶發事件之前的 `時間間隔期望值為 Lambda(L)`,可表示成 : `x~exp(B)` 或 `x~exp(1/L)`

其中, `Lambda(L) = 1 / Beta(B)`

pdf:

$$f_{x} (x) = {1/\beta} \cdot e ^{-x/ \beta }, x \ge 0$$
$$f_{x} (x) = \lambda \cdot e ^{-\lambda}, x \ge 0$$

cdf: 

(暫略)

Mean:

$$E(x) = 1/\beta$$
$$E(x) = \lambda$$


Variance:

$$V(x) = 1/\beta^2$$
$$V(x) = 1/\lambda^2$$





# [Beta Distribution](https://zh.wikipedia.org/wiki/%CE%92%E5%88%86%E5%B8%83)


# [Gamma Distribution](https://zh.wikipedia.org/wiki/%E4%BC%BD%E7%8E%9B%E5%88%86%E5%B8%83)

隨機變數 x 為 等到第 alpha 件事件發生所需等候的時間

alpha: 形狀參數 ; beta: 尺度參數




# [Normal Distribution](https://zh.wikipedia.org/wiki/%E6%AD%A3%E6%80%81%E5%88%86%E5%B8%83)

隨機變數 x 服從平均數 mu, 標準差 sigma, 則可表示成 `x~N(mu, sigma^2)`

pdf:

$$f_{x} (x) = \frac{1}{\sqrt {2 \pi} \sigma } \exp({-\frac{{(x-\mu)}^2}{2\sigma^2}}), -\infty \le x \le \infty$$

cdf:

印象中這好像不是很重要, 所以 Pass

Mean:

$$E(x) = \mu$$

Variance:

$$V(x) = \sigma^2$$