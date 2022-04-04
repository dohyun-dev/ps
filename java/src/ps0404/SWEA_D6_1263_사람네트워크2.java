package ps0404;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;

public class SWEA_D6_1263_사람네트워크2 {
    static StringBuilder sb = new StringBuilder();
    static Scanner sc = new Scanner(System.in);
    static int T, N;
    static int[][] graph, dist;
    public static void main(String[] args) {
        T = sc.nextInt();

        for(int t = 1; t < T + 1; t++) {
            N = sc.nextInt();
            graph = new int[N][N];
            dist = new int[N][N];

            for(int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    graph[i][j] = sc.nextInt();
                }
            }

            for(int i = 0; i < N; i++) {
                for(int j = 0; j < N; j++) {
                    if(i == j)  dist[i][j] = 0;
                    else if(graph[i][j] == 0)   dist[i][j] = 10000;
                    else    dist[i][j] = graph[i][j];
                }
            }

            for(int k = 0; k < N; k++) {
                for(int i = 0; i < N; i++) {
                    for(int j = 0; j < N; j++) {
                        dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
                    }
                }
            }

            int[] result = new int[N];

            Arrays.fill(result, 0);

            for(int i = 0; i < N; i++) {
                for(int j = 0; j < N; j++) {
                    if(dist[i][j] != 10000) result[i] += dist[i][j];
                }
            }

            int answer = Integer.MAX_VALUE;
            for(int i = 0; i < N; i++) {
                if(answer > result[i])  answer = result[i];
            }

            sb.append(String.format("#%d %d\n", t, answer));
        }
        System.out.print(sb.toString());
    }
}
