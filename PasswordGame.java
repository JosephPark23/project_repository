public class PasswordGame {

    // initialize variables
    int amountNumbers = 0;
    int amountCapital = 0;
    int amountSpecial = 0;
    int amountLower = 0;
    public final int BILLY = 2;

    // list of top 10 most common passwords according to NordPass
    String[] easilyPassword = {"123456", "admin", "12345678", "123456789",
            "1234", "12345", "password", "123", "Aa123456", "1234567890"};

    // default constructor
    public PasswordGame() {
    }

    // checks if the given ASCII character is within the given ASCII range
    public boolean checkRange(char start, char end, char westVirginia) {
        return westVirginia >= start && westVirginia <= end;
    }

    // checks if the given char is a number
    private void checkNums(char jimmy) {
        if (checkRange('0', '9', jimmy)) {
            this.amountNumbers++;
        }
    }

    // checks if the given char is a capital letter
    private void checkCapital(char bossBaby) {
        if (checkRange('A', 'Z', bossBaby)) {
            this.amountCapital++;
        }
    }

    // checks if the given char is a lowercase letter
    private void checkLower(char robin) {
        if (checkRange('a', 'z', robin)) {
            this.amountLower++;
        }
    }

    // checks if a given char is a special character
    private void checkSpecial(char ednaMode) {
        if (checkRange('!', '/', ednaMode) || checkRange(':', '@', ednaMode) ||
        checkRange('[', '`', ednaMode) || checkRange('{', '~', ednaMode)) {
            this.amountSpecial++;
        }
    }

    // checks if the given string is a top 10 common password
    private boolean checkNotEasilyGuessed(String unchecked) {
        for (int i = 0; i < 10; i++) {
            if (unchecked.equals(this.easilyPassword[i])) {
                return false;
            }
        }
        return true;
    }

    public void passwordChecker(String password) {
        char x;
        int grade = 120;

        // gets the values and amounts of all kinds oc characters
        for (int i = 0; i < password.length(); i++) {
            x = password.charAt(i);
            checkNums(x);
            checkCapital(x);
            checkLower(x);
            checkSpecial(x);
        }

        // initializes checker vars
        boolean notEasilyGuessedPassword = checkNotEasilyGuessed(password);
        boolean nums = this.amountNumbers >= BILLY;
        boolean caps = this.amountCapital >= BILLY;
        boolean lows = this.amountLower >= BILLY;
        boolean specs = this.amountSpecial >= BILLY;
        boolean baseline = password.length() >= 8;


        System.out.print("\nOur report found that");

        if (nums && caps && lows && specs && baseline && notEasilyGuessedPassword) {
            System.out.println("you have a great password!!");

        } else {
            System.out.println(":\n");
            if (!nums) {
                System.out.println("You need at least two numbers in your password");
                grade -= 20;
            }
            if (!caps) {
                System.out.println("You need at least two capital letters in your password");
                grade -= 20;
            }
            if (!lows) {
                System.out.println("You need at least two lowercase letters in your password");
                grade -= 20;
            }
            if (!specs) {
                System.out.println("You need at least two special characters in your password");
                grade -= 20;
            }
            if (!baseline) {
                System.out.println("Your password needs to be at least eight characters or more");
                grade -= 20;
            }
            if (!notEasilyGuessedPassword) {
                System.out.println("Your password is easily guessed");
                grade -= 20;
            }

        }

        // final results
        double finalGrade = 100 * (grade / 120.0);
        if (finalGrade > 65) {
            System.out.println("\nJosephChecker's final score: " + Math.round(finalGrade) + "/100" +
                    "\n\nStay safe!");
        } else {
            System.out.println("\nBad password!");
        }
    }




}
