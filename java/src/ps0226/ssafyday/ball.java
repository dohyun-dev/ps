package ps0226.ssafyday;

public class ball {

    public static void main(String[] args) {
        // Test Code
        // 1, 2, 3, 4분면 순서
        Point start1 = new Point(1, 1);
        Point target1 = new Point(3, 3);

        Point start2 = new Point(3, 3);
        Point target2 = new Point(5, 1);

        Point start3 = new Point(3, 3);
        Point target3 = new Point(1, 1);

        Point start4 = new Point(5, 1);
        Point target4 = new Point(3, 3);

        // 일직선상에 있을 때(목적구 기준 왼쪽, 오른쪽, 위, 아래)
        Point start5 = new Point(3, 3);
        Point target5 = new Point(1, 3);

        Point start6 = new Point(3, 3);
        Point target6 = new Point(5, 3);

        Point start7 = new Point(3, 1);
        Point target7 = new Point(3, 3);

        Point start8 = new Point(3, 3);
        Point target8 = new Point(3, 1);

        // 각도 출력
        System.out.println("1사분면" + getAngle(start1, target1));
        System.out.println("2사분면" + getAngle(start2, target2));
        System.out.println("3사분면" + getAngle(start3, target3));
        System.out.println("4사분면" + getAngle(start4, target4));
        System.out.println("목적구가 왼쪽 " + getAngle(start5, target5));
        System.out.println("목적구가 오른쪽 " + getAngle(start6, target6));
        System.out.println("목적구가 위 " + getAngle(start7, target7));
        System.out.println("목적구가 아래 " + getAngle(start8, target8));
    }

    public static double getAngle(Point start, Point target) {
        int width = Math.abs(start.x - target.x);
        int height = Math.abs(start.y - target.y);
        double angle = Math.atan2(height, width) * 180 / Math.PI;

        // 목적구가 왼쪽
        if(start.x > target.x && start.y == target.y)       angle = 270;
        // 목적구가 오른쪽
        else if(start.x < target.x && start.y == target.y)  angle = 90;
        // 목적구가 위
        else if(start.x == target.x && start.y < target.y)  angle = 0;
        // 목적구가 아래
        else if(start.x == target.x && start.y > target.y)  angle = 180;
        // 1, 2, 3, 4분면 따로 처리
        else {
            // 1사분면은 처리 안해도 됨
            // 흰공기준 2사분면에 있을때
            if(start.x < target.x && start.y > target.y)        angle += 90;
            // 3사분면
            else if(start.x > target.x && start.y > target.y)   angle += 180;
            // 4사분면
            else if(start.x > target.x && start.y < target.y)   angle += 270;
        }
        return angle;
    }

    static class Point {
        int x, y;

        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
