
import static java.lang.System.out;
// p11-12
// 2017/08/10
//
public class JoinDemo {
	public static void main(String[] args) 
		throws InterruptedException {
		System.out.println("Thread Main 開始");
		
		Thread threadB = new Thread(() -> {
			System.out.println("Thread B 開始");
			for (int i = 0; i < 5; i++) {
				System.out.println("Thread B 插隊執行第 " + Integer.toString(i) + " 次");
			}
			System.out.println("Thread B 結束...");
		});
		
		threadB.start();
		threadB.join(); //Thread B 加入Main thread流程
		
		System.out.println("Main thread將結束");
	}
}
