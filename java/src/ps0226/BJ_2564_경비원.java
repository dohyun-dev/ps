package ps0226;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BJ_2564_경비원 {
    static int width, height;
    static int answer;
    static Point[] stores;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        width = Integer.parseInt(st.nextToken());   height = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(br.readLine());
        stores = new Point[N+1];

        for(int i = 0; i < N+1; i++) {
            st = new StringTokenizer(br.readLine());
            stores[i] = new Point(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }

        for(int i = 0; i < N; i++) answer += solve(stores[N], stores[i]);

        System.out.println(answer);
    }

    // 북, 남, 서, 동(1, 2, 3, 4)
    static int solve(Point cur, Point store) {
        switch (cur.dir) {
            case 1: // 동근이가 북쪽
                return calc1(cur, store);
            case 2: // 동근이가 남쪽
                return calc2(cur, store);
            case 3: // 동근이가 서쪽
                return calc3(cur, store);
            default: // 동근이가 동쪽
                return calc4(cur, store);
        }
    }

    static int calc1(Point cur, Point store) {
        switch (store.dir) {
            case 1:     // 상점이 북쪽
                return Math.abs(cur.distance - store.distance);
            case 2:     // 상점이 남쪽
                int r1 = cur.distance + height + store.distance;    // 반시계 방향
                int r2 = (width - cur.distance) + height + (width - store.distance);    // 시계 방향
                return Math.min(r1, r2);
            case 3:     // 상점이 서쪽
                return cur.distance + store.distance;
            default:    // 상점이 동쪽
                return (width - cur.distance) + store.distance;
        }
    }

    static int calc2(Point cur, Point store) {
        switch (store.dir) {
            case 1:     // 상점이 북쪽
                int r1 = cur.distance + height + store.distance;    // 시계 방향
                int r2 = (width - cur.distance) + height + (width - store.distance);    // 반시계 방향
                return Math.min(r1, r2);
            case 2:     // 상점이 남쪽
                return Math.abs(cur.distance - store.distance);
            case 3:     // 상점이 서쪽
                return cur.distance + (height - store.distance);
            default:    // 상점이 동쪽
                return (width - cur.distance) + (height - store.distance);
        }
    }

    static int calc3(Point cur, Point store) {
        switch (store.dir) {
            case 1:     // 상점이 북쪽
                return cur.distance + store.distance;
            case 2:     // 상점이 남쪽
                return (height - cur.distance) + store.distance;
            case 3:     // 상점이 서쪽
                return Math.abs(cur.distance - store.distance);
            default:    // 상점이 동쪽
                int r1 = cur.distance + width + store.distance;    // 시계 방향
                int r2 = (height - cur.distance) + width + (height - store.distance);    // 반시계 방향
                return Math.min(r1, r2);
        }
    }

    static int calc4(Point cur, Point store) {
        switch (store.dir) {
            case 1:     // 상점이 북쪽
                return cur.distance + (width - store.distance);
            case 2:     // 상점이 남쪽
                return (height - cur.distance) + (width - store.distance);
            case 3:     // 상점이 서쪽
                int r1 = (height - cur.distance) + width + (height - store.distance);    // 시계 방향
                int r2 = cur.distance + width + store.distance;    // 반시계 방향
                return Math.min(r1, r2);
            default:    // 상점이 동쪽
                return Math.abs(cur.distance - store.distance);
        }
    }

    static class Point {
        int dir, distance;

        Point(int dir, int distance) {
            this.dir = dir;
            this.distance = distance;
        }
    }
}
