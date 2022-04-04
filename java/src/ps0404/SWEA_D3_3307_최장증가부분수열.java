package ps0404;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class SWEA_D3_3307_최장증가부분수열 {
    static int T, N;
    static int[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        T = Integer.parseInt(br.readLine());


        for(int t = 1; t < T + 1; t++) {
            N = Integer.parseInt(br.readLine());
            arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            int[] dp = new int[N];
            dp[0] = 1;
            for(int i = 1; i < N; i++) {
                int max_length = 0;
                for(int j = 0; j < i; j++) {
                    if(arr[i] > arr[j]) {
                        max_length = Math.max(max_length, dp[j]);
                    }
                    dp[i] = max_length + 1;
                }
            }

            int answer = 0;
            for(int i = 0; i < N; i++) {
                answer = Math.max(answer, dp[i]);
            }
            sb.append(String.format("#%d %d\n", t, answer));
        }

        System.out.print(sb.toString());
    }
}
