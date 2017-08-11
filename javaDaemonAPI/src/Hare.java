

public class Hare implements Runnable {
	private boolean[] flags = {true, false};
	private int totalStep;
	private int step;
	
	public Hare(int totalStep) {
		this.totalStep = totalStep;
	}
	
	@Override
	public void run() {
		while (step < totalStep) {
			boolean isHareSleep = flags[((int)(Math.random() * 2)) % 2];
			if (isHareSleep) {
				System.out.println("Hare sleep");
			} else {
				step+=2;
				System.out.printf("Hare ran %d step\n", totalStep);
			}
		}
	}
}
