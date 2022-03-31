package ps0330;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class BJ_1600_말이되고픈원숭이 {
    static int K, W, H;
    static int[][] board;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        K = Integer.parseInt(br.readLine());
        int[] tmp = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        W = tmp[0]; H = tmp[1];

        board = new int[H][];
        for(int i = 0; i < H; i++)  board[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        System.out.println(BFS());
    }

    public static int BFS() {
        int[][] dir1 = new int[][] {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
        int[][] dir2 = new int[][] {{-2, -1}, {-2, 1}, {-1, 2}, {1, 2}, {2, 1}, {2, -1}, {1, -2}, {-1, -2}};

        Queue<Point> q = new LinkedList<>();
        q.add(new Point(0, 0, 0));
        int[][][] dist = new int[31][H][W];

        for(int i = 0; i < H; i++) {
            for(int j = 0; j < W; j++) {
                for(int k = 0; k < 31; k++) {
                    dist[k][i][j] = -1;
                }
            }
        }
        dist[0][0][0] = 0;

        while(!q.isEmpty()) {
            Point cur = q.poll();

            if(cur.y == W-1 && cur.x == H-1) {
                return dist[cur.l][cur.x][cur.y];
            }

            // 사방 탐색
            for(int[] d : dir1) {
                int nx = cur.x + d[0];
                int ny = cur.y + d[1];
                // 같은 레벨 dist가 -1이면 방문하지 않았다는 뜻
                if(0 <= nx && nx < H && 0 <= ny && ny < W && board[nx][ny] == 0 && dist[cur.l][nx][ny] == -1) {
                    dist[cur.l][nx][ny] = dist[cur.l][cur.x][cur.y] + 1;
                    q.add(new Point(nx, ny, cur.l));
                }
            }

            // 말
            if (cur.l < K) {
                for (int[] d : dir2) {
                    int nx = cur.x + d[0];
                    int ny = cur.y + d[1];
                    // l+1이 이미 방문했다면 똑같은 경로를 다시 탐색하는 것이니까 방문 하지 않음
                    if (0 <= nx && nx < H && 0 <= ny && ny < W && board[nx][ny] == 0 && dist[cur.l+1][nx][ny] == -1) {
                        dist[cur.l+1][nx][ny] = dist[cur.l][cur.x][cur.y] + 1;
                        q.add(new Point(nx, ny, cur.l+1));
                    }
                }
            }
        }

        return -1;
    }

    static class Point {
        int x;
        int y;
        int l;

        public Point(int x, int y, int l) {
            this.x = x;
            this.y = y;
            this.l = l;
        }
    }
}
