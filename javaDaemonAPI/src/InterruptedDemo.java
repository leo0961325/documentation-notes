
// p11-11
// 2017/08/10
public class InterruptedDemo {
	public static void main(String[] args) {
		Thread thread = new Thread() {
			@Override
			public void run() {
				try {
					System.out.println("我打算睡 99999毫秒");
					Thread.sleep(99999);
				} catch (InterruptedException ex) {
					System.out.println("阿... 我被interrupt... 醒了");
				}
			}
		};
		thread.start();
		thread.interrupt();	// 主執行緒呼叫thread的interrupt()
	}
}
