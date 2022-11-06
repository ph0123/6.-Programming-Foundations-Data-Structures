import java.util.ArrayList;
class Main {
    public static void main(String[] args) {
     
      ArrayList<Integer> a = new ArrayList<>();
      for(int i =0; i<10; i++){
        a.add(i);
      }
      a.add(2,10);
      System.out.print(a);
    }
   }