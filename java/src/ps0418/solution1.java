package ps0418;

import java.io.IOException;
import java.util.Scanner;

public class solution1 {
    static Scanner sc = new Scanner(System.in);
    static int  M, N;
    static int answer;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    static int[][] board;
    static boolean[][] visited;

    public static void main(String[] args) throws NumberFormatException, IOException {
        M = sc.nextInt();
        N = sc.nextInt();
        board = new int[M][N];
        visited = new boolean[M][N];
        answer = 0;

        for(int i = 0; i < M; i++) {
            for(int j = 0; j < N; j++) {
                board[i][j] = sc.nextInt();
            }
        }
        // DFS를 돌린다.
        DFS(0, 0);

        System.out.println(answer);
    }

    private static void DFS(int x, int y) {
        visited[x][y] = true;
        // 현재 좌표가 도착지의 좌표라면 -> answer++
        if(x == M-1 && y == N-1) {
            answer++;
            return;
        }
        // 4방향을 탐색하면서 현재 갈수있는 방향인지 확인
        for(int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            // 범위체크 + 방문체크
            if(0 <= nx && nx < M && 0 <= ny && ny < N && !visited[nx][ny]) {
                // 갈 수 있는지 체크 내리막길 이어야만 됨
                if(board[x][y] > board[nx][ny]) {
                    visited[nx][ny] = true;
                    DFS(nx, ny);
                    visited[nx][ny] = false;    // 다른 경로도 탐색해야 되기 때문에 DFS를 수행하고 나면 visited를 false로 바꿔줌
                }
            }
        }
    }
}
