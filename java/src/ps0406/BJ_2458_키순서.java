package ps0406;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BJ_2458_키순서 {
    static int[][] graph;
    static int N, M, cnt, answer;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());   M = Integer.parseInt(st.nextToken());
        graph = new int[N][N];
        for(int i = 0; i < M; i++) {
            initGraph(br, st);
        }

        for(int i = 0; i < N; i++) {
            cnt = 0;
            visited = new boolean[N];
            bigDFS(i);
            smallDFS(i);
            if(cnt == N - 1)    answer++;

        }
        System.out.println(answer);
    }

    public static void bigDFS(int node) {
        visited[node] = true;
        for(int i = 0; i < N; i++) {
            if(graph[node][i] == 1 && !visited[i]) {
                cnt++;
                bigDFS(i);
            }
        }
    }

    public static void smallDFS(int node) {
        visited[node] = true;
        for(int i = 0; i < N; i++) {
            if(graph[i][node] == 1 && !visited[i]) {
                cnt++;
                smallDFS(i);
            }
        }
    }

    private static void initGraph(BufferedReader br, StringTokenizer st) throws IOException {
        st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken()) - 1;
        int b = Integer.parseInt(st.nextToken()) - 1;
        graph[a][b] = 1;
    }
}
