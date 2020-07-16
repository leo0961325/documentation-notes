
namespace StrategyMode
{
    public class Adventure
    {
        private IFightStrategy fightStrategy;

        public void Attack()
        {
            if (fightStrategy == null)
            {
                fightStrategy = new NormalAttack();
            }
            fightStrategy.Execute();
        }

        public void ChangeStrategy(IFightStrategy strategy)
        {
            this.fightStrategy = strategy;
        }
    }
}
