# Strategy Mode

- 2019/01/21

`冒險者` 打怪, 打怪時可用 `普通攻擊`, `技能攻擊`, `魔法攻擊`

如果一開始, 單純的想說

```cs
Adventure tony = new Adventure();
tony.NormalAttack();    // 用拳頭
tony.SkillAttack();     // 拿刀砍
tony.MagicAttack();     // 超強蒼蠅拍電擊
```

那將來會出現說, 如果冒險者有分為: 人類冒險者, 精靈冒險者 ...

而且每個冒險者, 他們攻擊的方式都不一樣, 那將來冒險者勢必得分成:

```cs
class Adventure {
    abstract void NormalAttack();
    abstract void SkillAttack();
    abstract void MagicAttack();
}

class Human : Adventure {
    void NormalAttack();    // 用拳頭
    void SkillAttack();     // 拿刀砍
    void MagicAttack();     // 超強蒼蠅拍電擊
}

class Elf : Adventure {
    void NormalAttack();    // 用腳踹
    void SkillAttack();     // 射弓箭
    void MagicAttack();     // 放火球
}
```

恩~ 看起來會有幾個缺點

1. 如果將來每增加一個種族, ex: 矮人, 那就得在來一包 `class Draft : Adventure { ... }`, 直接宣判了新增的種族都會 SkillAttack 以及 MagicAttack...@@!?
2. 如果要來個祭司冒險者, 但是他只會 Cure, Armor, SpeedAttack 等方法, 那 Adventure 就又得增加新的虛方法來因應變化, 從而導致 Human, Elf 都得在實作這些根本不存在的方法

所以不如把這種 `會 SkillAttack`, `會 MagicAttack` 的人物, 提出到介面

```cs
interface INormalAttack {
    void NormalAttack();
}

interface ISkillAttack {
    void SkillAttack();
}

interface IMagicAttack {
    void MagicAttack();
}
```