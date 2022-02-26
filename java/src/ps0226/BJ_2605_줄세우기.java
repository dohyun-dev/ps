package ps0226;

import java.io.*;
import java.util.*;

public class BJ_2605_줄세우기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] data = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        List<Integer> q = new LinkedList<>();

        for(int i = 0; i < N; i++)  q.add(q.size() - data[i], i+1);

        q.forEach(x -> System.out.print(x + " "));
    }
}
