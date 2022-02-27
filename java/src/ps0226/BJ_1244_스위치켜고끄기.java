package ps0226;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class BJ_1244_스위치켜고끄기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int size = Integer.parseInt(br.readLine());
        int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int N = Integer.parseInt(br.readLine());
        for(int i = 0; i < N; i++) {
            int[] temp = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            solve(temp[0], temp[1]-1, arr);
        }
        int cnt = 0;
        for(int i = 0; i < size; i++) {
            System.out.print(arr[i] + " ");
            if(++cnt % 20 == 0) System.out.println();
        }
    }

    static void solve(int gender, int num, int[] arr) {
        switch (gender) {
            case 1:
                for(int i = num; i < arr.length; i += num+1)  arr[i] = arr[i] == 1 ? 0 : 1;
                break;
            default:
                int i = 1;
                while (num - i >= 0 && num + i < arr.length && arr[num-i] == arr[num+i]) {
                    arr[num-i] = arr[num-i] == 1 ? 0 : 1;
                    arr[num+i] = arr[num-i];
                    i++;
                }
                arr[num] = arr[num] == 1 ? 0 : 1;
        }
    }
}
