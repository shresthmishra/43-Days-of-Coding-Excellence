import java.util.*;

public class August_23 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        sc.close();
        int yearsTaken = 0;
        while (a <= b) {
            a *= 3;
            b *= 2;
            yearsTaken += 1;
        }
        System.out.println(yearsTaken);
    }
}