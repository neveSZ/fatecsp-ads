import java.util.Scanner;

public class EX04 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.printf("Base: ");
        float base = scan.nextFloat();
        System.out.printf("Altura: ");
        float altura = scan.nextFloat();
        System.out.printf("Area: %.2f\nPerimetro: %.2f", altura * base, altura * 2 + base * 2);
    }
}