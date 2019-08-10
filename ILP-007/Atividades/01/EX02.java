import java.util.Scanner;

public class EX02 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.printf("P1: ");
        float p1 = scan.nextFloat();
        System.out.printf("P2: ");
        float p2 = scan.nextFloat();
        System.out.printf("T: ");
        float t = scan.nextFloat();
        System.out.printf("Nota final: %.2f", p1 * 0.40 + p2 * 0.40 + t * 0.20);
    }
}