package ps0226;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class BJ_2309_일곱난쟁이 {
    static int[] heights = new int[9];
    static int[] result = new int[7];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < 9; i++) heights[i] = Integer.parseInt(br.readLine());
        Arrays.sort(heights);
        DFS(0, 0, 0);
    }

    public static void DFS(int l, int start, int sum) {
        if(sum > 100)   return;
        if(l == 7) {
            if(sum == 100) {
                for(int n : result) System.out.println(n);
                System.exit(0);
            }
            return;
        }
        for(int i = start; i < 9; i++) {
            result[l] = heights[i];
            DFS(l+1, i+1, sum + heights[i]);
        }
    }
}
