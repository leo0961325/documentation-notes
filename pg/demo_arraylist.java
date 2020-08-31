import java.util.*;

public class demo_arraylist {
    public static void main(String[] args) {
        // Scanner scanner = new Scanner(System.in);
        List aa = new ArrayList<String>();
        aa.add("A");
        aa.add("B");
        aa.add("C");
        aa.add("D");
        
        ListIterator scanner = aa.listIterator();
        
        List<String> list = new ArrayList<String>();
        
        System.out.println("輸入名稱(quit結束)");
        String input;
        while(true) { 
            System.out.print("# ");
            try {
              input = (String)scanner.next(); 
 
              if(input.equals("quit"))
                   break; 
              list.add(input); 
            } catch (Exception ex){
              break;
            }
        }
        
        System.out.print("print: "); 
        for(int i = 0; i < list.size(); i++) 
            System.out.print(list.get(i) + " "); 
        System.out.println(list); 
        list.remove(2);
        System.out.println(list);
    }
}
