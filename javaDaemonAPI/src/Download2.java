
import java.net.URL;
import java.io.*;
// p11-10
//2017/08/10
// multi-thread§ìÀÉ®×

public class Download2 {
	public static void main(String[] args) throws Exception {
		URL[] urls = {
				new URL("https://openhome.cc/Gossip/Encoding/"),
				new URL("https://openhome.cc/Gossip/Scala/"),
				new URL("https://openhome.cc/Gossip/JavaScript/"),
				new URL("https://openhome.cc/Gossip/Python/")
		};
		
		String[] fileNames = {
			"Encoding.html",
			"Scala.html",
			"JavaScript.html",
			"Python.html"
		};
		
		for (int i = 0; i < urls.length; i++) {
			int index = i;
			// ³o¸Ì®@~~~
			new Thread(() -> {
				try {
					dump(urls[index].openStream(), new FileOutputStream(fileNames[index]));
				} catch (IOException ex) {
					throw new RuntimeException(ex);
				}
			}).start();
		}
	}
	
	public static void dump(InputStream src, OutputStream dest) 
			throws IOException {
		try (InputStream input = src; OutputStream output = dest) {
			byte[] data = new byte[1024];
			int length;
			
			while ((length = input.read(data)) != -1) {
				output.write(data, 0, length);
			}
		}
	};
}
