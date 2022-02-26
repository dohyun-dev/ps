package ps0226;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class BJ_2669_직사각형네게의합집합의면적구하기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[][] board = new int[100][100];
        int cnt = 0;

        for(int n = 0; n < 4; n++) {
            int[] points = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

            for(int i = points[0]; i < points[2]; i++) {
                for(int j = points[1]; j < points[3]; j++) {
                    board[i][j] = 1;
                }
            }
        }

        for(int i = 0; i < 100; i++) {
            for(int j = 0; j < 100; j++) {
                if(board[i][j] == 1) cnt++;
            }
        }

        System.out.println(cnt);
    }
}
