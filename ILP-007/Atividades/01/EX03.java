import java.util.Scanner;

public class EX03 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.printf("RS: ");
        float reais = scan.nextFloat();
        System.out.printf("%.2f USD", reais * 3.94);
    }
}