package ps0418;

import java.io.File;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;

public class TC {

    private static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) {
        for(int tc = 0; tc < 10; tc++) {
            int N = (int) ((Math.random() * 100) + 2);
            int M = (int) ((Math.random() * 100) + 2);
            int[][] arr = new int[N][M];
            int ran = (int) ((Math.random() * 200)+1);
            int ran2 = (int) ((Math.random() * 200)+1);

            sb.append(M).append(" ").append(N).append("\n");

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    arr[i][j] = 0;
                }
            }

            for(int i = 0; i < ran; i++) {
                int x = (int) (Math.random() * N);
                int y = (int) (Math.random() * M);
                arr[x][y] = 1;
            }

            for(int i = 0; i < ran2; i++) {
                int x = (int) (Math.random() * N);
                int y = (int) (Math.random() * M);
                arr[x][y] = -1;
            }

            for(int i = 0; i < N; i++) {
                for(int j =0; j < M; j++) {
                    sb.append(arr[i][j]).append(" ");
                }
                sb.setLength(sb.length() - 1);
                sb.append("\n");
            }
        }

        String fileName = "/Users/kwon/Desktop/ps/java/src/ps0418/tc/testcase1.txt";

        try {
            // 파일 객체 생성
            File file = new File(fileName);

            // true 지정시 파일의 기존 내용에 이어서 작성
            FileWriter fw = new FileWriter(file, true);

            // 파일안에 문자열 쓰기
            fw.write(sb.toString());
            fw.flush();

            // 객체 닫기
            fw.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}