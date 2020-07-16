namespace StrategyMode
{
    public class NormalAttack : IFightStrategy
    {
        public void Execute()
        {
            System.Console.WriteLine("用拳頭揍");
        }
    }

    class SkillAttack : IFightStrategy
    {
        public void Execute()
        {
            System.Console.WriteLine("用刀連砍");
        }
    }

    class MagicAttack : IFightStrategy
    {
        public void Execute()
        {
            System.Console.WriteLine("放火燒~~");
        }
    }
}