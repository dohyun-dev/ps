package ps0226;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class BJ_2578_빙고 {
    static int[][] board1 = new int[5][];
    static int[][] board2 = new int[5][];

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for(int t = 0; t < 2; t++) {
            for(int i = 0; i < 5; i++)  {
                if(t == 0)  board1[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
                else board2[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            }
        }

        int cnt = 0;
        loop:for(int[] a : board2) {
            for(int num : a) {
                cnt++;
                if(bingo(num)) {
                    System.out.println(cnt);
                    break loop;
                }
            }
        }
    }

    static boolean bingo(int num) {
        loop:for(int i = 0; i < 5; i++) {
            for(int j = 0; j < 5; j++) {
                if(board1[i][j] == num) {
                    board1[i][j] = -1;
                    break loop;
                }
            }
        }
        int answer = 0;

        for(int i = 0; i < 5; i++) {
            int cnt1 = 0;
            int cnt2 = 0;

            for(int j = 0; j < 5; j++) {
                if(board1[i][j] == -1)   cnt1++; // 가로
                if(board1[j][i] == -1)   cnt2++; // 세로
            }
            if(cnt1 == 5)   answer++;
            if(cnt2 == 5)   answer++;
        }

        int cnt1 = 0;
        int cnt2 = 0;

        for(int i = 0; i < 5; i++) {
            if(board1[i][i] == -1) cnt1++;
            if(board1[i][5-i-1] == -1) cnt2++;
        }

        if(cnt1 == 5)   answer++;
        if(cnt2 == 5)   answer++;

        if(answer >= 3) return true;
        return false;
    }
}
