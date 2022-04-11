package ps0411;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class D4_8458_원점으로집합 {

    private static int T;
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final StringBuilder sb = new StringBuilder();
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(br.readLine());

        for(int t = 1; t <= T; t++) {
            int n = Integer.parseInt(br.readLine());
            int[][] arr = new int[n][2];
            int[] dist = new int[n];

            for(int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                arr[i][0] = Integer.parseInt(st.nextToken());
                arr[i][1] = Integer.parseInt(st.nextToken());
                dist[i] = Math.abs(arr[i][0] - 0) + Math.abs(arr[i][1] - 0);
            }

            boolean flag = dist[0] % 2 == 0;
            boolean flagResult = false;
            for(int d : dist) {
                if(flag == (d % 2 == 0)) {
                    flagResult = true;
                } else {
                    flagResult = false;
                    break;
                }
            }

            if(flagResult) {
                int answer = 0;
                int temp = 0;
                int i = 1;

                for(int d : dist) {
                    temp = Math.max(temp, d);
                }

                while(true) {
                    if(temp <= 0 && temp % 2 == 0)  break;
                    answer++;
                    temp -= i;
                    i++;
                }
                sb.append("#" + t + " " + answer + "\n");
            } else {
                sb.append("#" + t + " -1\n");
            }
        }
        System.out.println(sb.toString());
    }
}
