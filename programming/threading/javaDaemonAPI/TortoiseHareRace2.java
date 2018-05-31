
public class TortoiseHareRace2 {
	public static void main(String[] args) {
		Tortoise t1 = new Tortoise(10);
		Hare t2 = new Hare(10);
		
		Thread t1Thread = new Thread(t1);
		Thread t2Thread = new Thread(t2);
		
		t1Thread.start();
		t2Thread.start();
	}
}
