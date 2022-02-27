package ps0226;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BJ_10157_자리배정 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int C = Integer.parseInt(st.nextToken()), R = Integer.parseInt(st.nextToken());
        int[][] board = new int[R][C];
        int K = Integer.parseInt(br.readLine());
        int cnt = 0;

        if(K > C * R) {
            System.out.println(0);
            System.exit(0);
        }

        for(int n = 0; n < Math.min(R, C) / 2 + 1; n++) {
            for(int i = n; i < R - n; i++) {
                board[i][n] = ++cnt;
                if(cnt == K) {
                    System.out.println((n + 1) + " " + (i + 1));
                    System.exit(0);
                }
            }
            for(int i = n+1; i < C- n; i++) {
                board[R-n-1][i] = ++cnt;
                if(cnt == K) {
                    System.out.println((i + 1) + " " + (R-n));
                    System.exit(0);
                }
            }
            for(int i = R - n - 2; i >= n; i--) {
                board[i][C-n-1] = ++cnt;
                if(cnt == K) {
                    System.out.println((C-n) + " " + (i + 1));
                    System.exit(0);
                }
            }
            for(int i = C - n - 2; i > n; i--) {
                board[n][i] = ++cnt;
                if(cnt == K) {
                    System.out.println((i + 1) + " " + (n + 1));
                    System.exit(0);
                }
            }
        }
    }
}
