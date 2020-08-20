using System;

namespace StrategyMode
{
    class Program
    {
        static void Main(string[] args)
        {
            // Adventure tony = new Adventure();
            // System.Console.WriteLine("---壞人出現---");
            // tony.Attack();

            // System.Console.WriteLine("---川普出現---");
            // tony.ChangeStrategy(new SkillAttack());
            // tony.Attack();

            // System.Console.WriteLine("---習包子出現---");
            // tony.ChangeStrategy(new MagicAttack());
            // tony.Attack();
            SampleClassB b = new SampleClassB();
            b.Call();
            b.Call0();
        }
    }

    
    class SampleClassA
    {
        public virtual void Call()
        {
            Console.WriteLine("Call1");
        }

        public void Call0()
        {
            Console.WriteLine("Call0");
        }
    }
    class SampleClassB: SampleClassA
    {
        public void Call0()
        {
            Console.WriteLine("Call2");
        }
        
    }
}
