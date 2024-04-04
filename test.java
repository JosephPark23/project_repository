import java.util.Scanner;

public class test {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("""
                welcome to JosephChecker. we will be checking two things:
                1) if you have a strong password
                2) if you're a moron or not.
                """);
            System.out.print("What is your password?: ");
            String x = input.nextLine();
            PasswordGame test = new PasswordGame();
            test.passwordChecker(x);
    }
}
