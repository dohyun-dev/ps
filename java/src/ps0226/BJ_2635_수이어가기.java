package ps0226;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class BJ_2635_수이어가기 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        ArrayList<Integer> answer = new ArrayList();

        for(int i = 1; i <= N; i++) {
            ArrayList<Integer> arr = new ArrayList<>();
            arr.add(N); arr.add(i);
            while(arr.get(arr.size() - 2) - arr.get(arr.size() - 1) >= 0) {
                arr.add(arr.get(arr.size() - 2) - arr.get(arr.size() - 1));
            }
            if(answer.size() < arr.size())  answer = arr;
        }
        System.out.println(answer.size());
        answer.forEach(x -> System.out.printf("%d ", x));

    }
}
