package ps0418;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class solution2 {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static int T;

    public static void main(String[] args) throws NumberFormatException, IOException {
        System.out.println((Math.pow(1009, 3) - 1008) % 6);
    }
}
