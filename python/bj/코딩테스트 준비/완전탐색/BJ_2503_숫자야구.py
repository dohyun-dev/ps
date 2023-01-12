from itertools import permutations

def calc_round(b, game):
    strike, ball, game = 0, 0, [*map(int, str(game))]
    for i in range(3):
        if b[i] == game[i]:
            strike += 1
        elif b[i] in game:
            ball += 1
    return (strike, ball)

games = [[*map(int, input().split())]for _ in range(int(input()))]
answer = 0
for p in permutations(range(1, 10), 3):
    for game, strike, ball in games:
        s, b = calc_round(p, game)
        if s != strike or b != ball:
            break
    else:
        answer += 1
print(answer)
