package ps0226;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BJ_13300_방배정 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()), K = Integer.parseInt(st.nextToken());
        int answer = 0;
        int[] male = new int[7];
        int[] female = new int[7];

        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int S = Integer.parseInt(st.nextToken()), Y = Integer.parseInt(st.nextToken());

            if(S == 0) {
                if(female[Y] + 1 <= K) {
                    if(female[Y] == 0)  answer += 1;
                    female[Y]++;

                }
                else {
                    answer++;
                    female[Y] = 1;
                }
            } else {
                if(male[Y] + 1 <= K) {
                    if(male[Y] == 0)  answer += 1;
                    male[Y]++;

                }
                else {
                    answer++;
                    male[Y] = 1;
                }
            }
        }

        System.out.println(answer);
    }
}
