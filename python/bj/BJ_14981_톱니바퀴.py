from operator import ge
import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import deque

def turn_left_gear(turn_gear_num, dir, pre):
    if turn_gear_num == -1:
        return
    
    dir = -dir
    if gear[turn_gear_num][2] != pre:
        pre_turn_left = gear[turn_gear_num][6]
        gear[turn_gear_num].rotate(dir)
        turn_left_gear(turn_gear_num-1, dir, pre_turn_left)
    else:
        return
        
def turn_right_gear(turn_gear_num, dir, pre):
    if turn_gear_num == 4:
        return
    
    dir = -dir
    if gear[turn_gear_num][6] != pre:
        pre_turn_right = gear[turn_gear_num][2]
        gear[turn_gear_num].rotate(dir)
        turn_right_gear(turn_gear_num+1, dir, pre_turn_right)
    else:
        return
    
# 0: 12시, 3: 3시 , 9: 9시
gear = [deque(list(input())) for _ in range(4)]
answer = 0

for i in range(int(input())):
    turn_gear_num, dir = map(int, input().split())
    turn_gear_num -= 1
    cur_gear = gear[turn_gear_num]
    
    # 기어 회전
    pre_turn_left = cur_gear[6]
    pre_turn_right = cur_gear[2]
    
    cur_gear.rotate(dir)
    turn_left_gear(turn_gear_num-1, dir, pre_turn_left)
    turn_right_gear(turn_gear_num+1, dir, pre_turn_right)

s = 1
for i in range(4):
    answer += s if gear[i][0] == "1" else 0
    s *= 2

print(answer)