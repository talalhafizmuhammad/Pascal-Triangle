using System;

class PascalTriangle
{
    static int Fact(int n)
    {
        int f = 1;
        for (int i = 1; i <= n; i++) f *= i;
        return f;
    }

    static int Ncr(int n, int r)
    {
        return Fact(n) / (Fact(r) * Fact(n - r));
    }

    static void Main()
    {
        Console.Write("Enter number of rows: ");
        int n = int.Parse(Console.ReadLine());

        for (int i = 0; i < n; i++)
        {
            Console.Write(new string(' ', n - i));
            for (int j = 0; j <= i; j++)
            {
                Console.Write(Ncr(i, j) + " ");
            }
            Console.WriteLine();
        }
    }
}
