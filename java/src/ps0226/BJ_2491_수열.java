package ps0226;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class BJ_2491_수열 {
    static int N, answer = 1;
    static int[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        int cnt = 1;
        for(int i = 1; i < N; i++) {
            if(arr[i-1] <= arr[i]) cnt++;
            else cnt = 1;
            answer = Math.max(answer, cnt);
        }

        cnt = 1;
        for(int i = 1; i < N; i++) {
            if(arr[i-1] >= arr[i]) cnt++;
            else cnt = 1;
            answer = Math.max(answer, cnt);
        }

        System.out.println(answer);
    }
}
