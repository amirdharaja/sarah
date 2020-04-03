public class PrimeNumber
{
    public static void main (String[] myArguments)
    {
        String  primeNumbers = "";

        for (int range = 20; range <= 100; range++)
        {
            int counter = 0;
            for(int number = 1; number <= range; number++)
            {
                if(range % number == 0)
                {
                    counter = counter + 1;
                }
            }
            if (counter == 2)
                {
                    primeNumbers = primeNumbers + range + ", ";
                }
        }
        System.out.println("Prime numbers between 20 & 100 is :\n" + primeNumbers);
    }
}
