package ps0226;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

// https://www.acmicpc.net/problem/2116

public class BJ_2116_주사위쌓기 {
    static int N, answer = 0;
    static int[][] dices;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        dices = new int[N][];

        // 주사위 목록 초기화
        for(int i = 0; i < N; i++) {
            dices[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }

        for(int bottom = 0; bottom < 6; bottom++) {
            boolean[] check = new boolean[7];
            int top = 0;

            switch (bottom) {
                case 0: top = 5;    break;
                case 1: top = 3;    break;
                case 2: top = 4;    break;
                case 3: top = 1;    break;
                case 4: top = 2;    break;
                case 5: top = 0;    break;
            }

            check[dices[0][bottom]] = true;
            check[dices[0][top]] = true;

            int cur_max = findMaxValue(check);

            if(N == 1){
                answer = Math.max(answer, cur_max);
            } else {
                DFS(1, dices[0][top], cur_max);
            }

        }
        System.out.println(answer);
    }

    static void DFS(int l, int bottom, int sum) {
        if(l == N) {    // 종료 조건
            answer = Math.max(answer, sum);
        } else {
            boolean[] check = new boolean[7];
            int top_idx = 0;
            int bottom_idx = 0;

            // 주사위 바닥 설정
            for(int i = 0; i < 6; i++) {
                if(dices[l][i] == bottom) {
                    bottom_idx = i;
                    break;
                }
            }
            // 주사위 위 설정
            switch (bottom_idx) {
                case 0: top_idx = 5;    break;
                case 1: top_idx = 3;    break;
                case 2: top_idx = 4;    break;
                case 3: top_idx = 1;    break;
                case 4: top_idx = 2;    break;
                case 5: top_idx = 0;    break;
            }

            check[dices[l][bottom_idx]] = true;
            check[dices[l][top_idx]] = true;

            int cur_max = findMaxValue( check);   // 위 아래 빼고 최고값 찾음
            DFS(l+1, dices[l][top_idx], sum + cur_max); // 주사위 위에 값을 전달
        }
    }

    static int findMaxValue(boolean[] check) {
        int max = 0;
        for(int i = 1; i < 7; i++) {
            if(!check[i]) max = Math.max(max, i);
        }
        return max;
    }
}
