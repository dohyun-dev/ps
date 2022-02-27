package ps0226;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Stack;
import java.util.StringTokenizer;

public class BJ_2304_창고다각형 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        int answer = 0;
        ArrayList<Pillar> arr = new ArrayList<>();

        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            arr.add(new Pillar(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
        }
        arr.sort((p1, p2) -> p1.x - p2.x);

        Stack<Pillar> stack = new Stack<>();
        for(Pillar p : arr) {
            if(stack.isEmpty()) stack.push(p);
            else if(stack.peek().y < p.y) {
                Pillar pre = stack.pop();
                answer += (p.x - pre.x) * pre.y;
                stack.push(p);
            }
        }

        Stack<Pillar> stack2 = new Stack<>();
        for(int i = arr.size()-1; i >= 0; i--) {
            Pillar p = arr.get(i);
            if(stack2.isEmpty()) stack2.push(p);
            else if(stack2.peek().y < p.y) {
                Pillar pre = stack2.pop();
                answer += (pre.x - p.x) * pre.y;
                stack2.push(p);
            }
        }
        Pillar p1 = stack2.pop(), p2 = stack.pop();
        answer += (p1.x - p2.x + 1) * p1.y;

        System.out.println(answer);
    }

    static class Pillar {
        int x, y;   // 위치 높이

        public Pillar(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public String toString() {
            return "Pillar{" +
                    "x=" + x +
                    ", y=" + y +
                    '}';
        }
    }
}
