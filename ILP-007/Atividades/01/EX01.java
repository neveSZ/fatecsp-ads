import java.util.Scanner;

public class EX01 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.printf("Idade: ");
        int idade = scan.nextInt();
        System.out.printf("%d dias", idade * 365);
    }
}