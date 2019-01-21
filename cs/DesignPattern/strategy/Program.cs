using System;

namespace StrategyMode
{
    class Program
    {
        static void Main(string[] args)
        {
            Adventure tony = new Adventure();
            System.Console.WriteLine("---壞人出現---");
            tony.Attack();

            System.Console.WriteLine("---川普出現---");
            tony.ChangeStrategy(new SkillAttack());
            tony.Attack();

            System.Console.WriteLine("---習包子出現---");
            tony.ChangeStrategy(new MagicAttack());
            tony.Attack();
        }
    }
}
