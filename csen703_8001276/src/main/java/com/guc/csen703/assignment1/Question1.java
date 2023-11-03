package com.guc.csen703.assignment1;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.math.BigDecimal;

/*
Write two program segments to implement the computation of powering a number, a^n ,
where n is a natural number, in two different ways:
    i. Naive iterative method through multiplication by n times in a loop.
    ii. Repeat the same problem using a divide-and-conquer approach.
*/


public class Question1 {

    public static void main(String[] args) {
        int a = 2;

        File csvFile = new File("question1.csv");
        try {
            FileWriter fileWriter = new FileWriter(csvFile);
            String row = "n,Iterative,Recursive\n";
            fileWriter.append(row);
            
            for (long n = 1; n <= 10E+5; n *= 10) {
                long resultIterative = timePowerIterative(a, n);
                long resultRecursive = timePowerRecursive(a, n);
                
                row = String.format("%d,%d,%d\n", n, resultIterative, resultRecursive);
                System.out.println(n);
                fileWriter.append(row);
            }
            
            fileWriter.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static long timePowerIterative(int base, long n) {
        long startTime = System.nanoTime();
        powerIterative(base, n);
        long endTime = System.nanoTime();

        return endTime - startTime;
    }

    public static long timePowerRecursive(int base, long n) {
        long startTime = System.nanoTime();
        powerRecursive(base, n);
        long endTime = System.nanoTime();

        return endTime - startTime;
    }

    public static BigDecimal powerIterative(int base, long n) {
        BigDecimal result = new BigDecimal(1);

        // Iterate n times
        for (long i = 0; i < n; i++) {
            result = result.multiply(BigDecimal.valueOf(base));
        }

        return result;
    }

    public static BigDecimal powerRecursive(int base, long n) {
        if (n < 1) return BigDecimal.valueOf(1);
        if (n < 2) return BigDecimal.valueOf(base);

        BigDecimal powerHalf = powerRecursive(base, n/2);
        BigDecimal result = powerHalf.multiply(powerHalf);

        if (n % 2 == 1) result = result.multiply(BigDecimal.valueOf(base));

        return result;
    }
}
