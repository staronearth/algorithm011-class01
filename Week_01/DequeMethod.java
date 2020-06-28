import java.util.Deque;
import java.util.LinkedList;

public class DequeMethod {
    public static void main(String[] args) {
        Deque<String> deque = new LinkedList<String>();
        deque.offerFirst("a");
        deque.addFirst("b");
        deque.addLast("c");
        System.out.println(deque);
        String str = deque.peek();
        System.out.println(str);
        System.out.println(deque);
        while (deque.size() > 0) {
            //System.out.println(deque.pollFirst());
            System.out.println(deque.pollLast());
        }
        System.out.println(deque);
    }
}
