package ps0226;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BJ_2527_직사각형 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < 4; i++) {
            int[] t = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            sb.append(solve(new Square(t[0], t[1], t[2], t[3]), new Square(t[4], t[5], t[6], t[7])) + "\n");
        }
        System.out.println(sb);
    }

    static String solve(Square s1, Square s2) {
        // 공통부분이 없는 경우
        if(s1.x2 < s2.x1 || s1.x1 > s2.x2 || s1.y2 < s2.y1 || s1.y1 > s2.y2) {
            return "d";
        }
        // 점 일때
        else if ((s1.x1 == s2.x2 && s1.y2 == s2.y1) || (s1.x2 == s2.x1 && s1.y2 == s2.y1) || (s1.x2 == s2.x1 && s1.y1 == s2.y2) ||
                (s1.x1 == s2.x2 && s1.y1 == s2.y2)) {
            return "c";
        }
        // 선분
        else if (s1.x1 == s2.x2 || s1.x2 == s2.x1 || s1.y1 == s2.y2 || s1.y2 == s2.y1) {
            return "b";
        }
        // 직사각형
        else {
            return "a";
        }
    }

    static class Square {
        int x1, y1, x2, y2;

        Square(int x1, int y1, int x2, int y2) {
            this.x1 = x1;
            this.y1 = y1;
            this.x2 = x2;
            this.y2 = y2;
        }
    }
}
