package ps0226;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class BJ_2628_종이자르기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        ArrayList<Integer> width = new ArrayList<>();
        ArrayList<Integer> height = new ArrayList<>();
        int answer = 0;
        width.add(0);   height.add(0); width.add(Integer.parseInt(st.nextToken())); height.add(Integer.parseInt(st.nextToken()));

        int n = Integer.parseInt(br.readLine());

        for(int i = 0; i < n; i++) {
            int[] temp = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            if(temp[0] == 1) width.add(temp[1]);
            else height.add(temp[1]);
        }

        Collections.sort(width);
        Collections.sort(height);

        for(int i = 1; i < width.size(); i++) {
            int x = width.get(i) - width.get(i-1);
            for(int j = 1; j < height.size(); j++) {
                int y = height.get(j) - height.get(j-1);
                answer = Math.max(answer, x * y);
            }
        }
        System.out.println(answer);
    }
}
