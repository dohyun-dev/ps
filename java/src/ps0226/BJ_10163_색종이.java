package ps0226;

import java.io.*;
import java.util.*;

public class BJ_10163_색종이 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int[][] board = new int[1001][1001];
        int N = Integer.parseInt(br.readLine());
        int[][] points = new int[N+1][];

        for(int n = 1; n <= N; n++) {
            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken()), y1 = Integer.parseInt(st.nextToken()), width = Integer.parseInt(st.nextToken()), height = Integer.parseInt(st.nextToken());
            points[n] = new int[]{x1, width, y1, height};
            for(int i = x1; i < x1 + width; i++) {
                for(int j = y1; j < y1 + height; j++) {
                    board[i][j] = n;
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for(int p = 1; p <= N; p++) {
            int x1 = points[p][0], width = points[p][1], y1 = points[p][2], height = points[p][3];
            int cnt = 0;
            for(int i = x1; i < x1 + width; i++) {
                for(int j = y1; j < y1 + height; j++) {
                    if(board[i][j] == p) cnt++;
                }
            }
            sb.append(cnt + "\n");
        }
        System.out.println(sb);
    }
}