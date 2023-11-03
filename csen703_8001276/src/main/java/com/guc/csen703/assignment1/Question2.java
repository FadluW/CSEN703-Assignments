package com.guc.csen703.assignment1;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.Vector;

import org.jgrapht.alg.util.Pair;

public class Question2 {

    public static void main(String[] args) {
        File csvFile = new File("question2.csv");

        try {
            FileWriter fileWriter = new FileWriter(csvFile);
            for (Integer i = 10; i <= 10E+4; i *= 10) {
                // Populate set from 0 - i
                Set<Integer> S = new HashSet<>();
                for (Integer x = 0; x <= i; x++) {
                    S.add(x);
                }
                mergeSortSet(S, 0, i);

                long time = timeGetSumPairs(S, i);
                String row = String.format("%d\n", time);
                System.out.println(i);
                fileWriter.append(row);
            }

            fileWriter.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

        // System.err.println(getSumPairs(S, Integer.valueOf(6)));
    }

    public static long timeGetSumPairs(Set<Integer> list, Integer x) {
        long startTime = System.nanoTime();
        getSumPairs(list, x);
        long endTime = System.nanoTime();

        return endTime - startTime;
    }

    public static Vector<Pair<Integer, Integer>> getSumPairs(Set<Integer> list, Integer x) {
        // Merge sort the list
        mergeSortSet(list, 0, list.size() - 1);

        // Iterate through half of the list, look for pairs
        Vector<Pair<Integer, Integer>> pairs = new Vector<>();
        int halfSize = list.size() / 2;
        Integer[] arr = list.toArray(new Integer[1]);
        for (Integer i = 0; i <= halfSize; i++) {
            Integer current = arr[i];
            int pairIndex = binarySearchList(arr, x - current, i + 1, arr.length);

            if (pairIndex != -1) {
                pairs.add(new Pair<Integer,Integer>(current, x - current));
            }
        }

        return pairs;
    }
    
    public static void merge(Integer arr[], int left, int mid, int right) {
        // Size of subarrays
        int size1 = mid - left + 1;
        int size2 = right - mid;
 
        // Create temp arrays to store in data
        int arrLeft[] = new int[size1];
        int arrRight[] = new int[size2];
 
        for (int i = 0; i < size1; i++) {
            arrLeft[i] = arr[left + i];
        }
        for (int j = 0; j < size2; j++) {
            arrRight[j] = arr[mid + j + 1];
        }
 
        // Merge the temp arrays
        int i = 0;
        int j = 0;

        // Initial index of merged subarray array
        int k = left;
        while (i < size1 && j < size2) {
            if (arrLeft[i] <= arrRight[j]) {
                arr[k] = arrLeft[i];
                i++;
            }
            else {
                arr[k] = arrRight[j];
                j++;
            }
            k++;
        }
 
        // Copy remaining elements of arrLeft[] if any
        while (i < size1) {
            arr[k] = arrLeft[i];
            i++;
            k++;
        }
 
        // Copy remaining elements of arrRight[] if any
        while (j < size2) {
            arr[k] = arrRight[j];
            j++;
            k++;
        }
    }
    
    /**
     * 
     * @param list
     */
    public static void mergeSortSet(Set<Integer> list, int l, int r) {
        if (l < r) {
 
            // Find the middle point
            int m = l + (r - l) / 2;
 
            // Sort first and second halves
            mergeSortSet(list, l, m);
            mergeSortSet(list, m + 1, r);
 
            // Merge the sorted halves
            merge(list.toArray(new Integer[0]), l, m, r);
        }
    }

    /**
     * Perform binary search on a List of {@code Integer}.
     * @param list input list with all values
     * @param x value to look for
     * @return  index of the search value, or {@code null} if not found
     */
    public static int binarySearchList(Integer[] list, Integer x, int i, int j) {
        if (j < i) return -1;
        
        int mid = (i + j) / 2;

        if (list[mid].equals(x)) {
            return mid;
        }

        if (list[mid] > x) {
            return binarySearchList(list, x, i, mid - 1);
        } else {
            return binarySearchList(list, x, mid + 1, j);
        }
    }
}
