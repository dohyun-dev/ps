from collections import defaultdict

def calc_seconds(d, t):
    return ((month_arr[int(d[5:7])] + int(d[8:10])) * 24 * 60) + (int(t[:2]) * 60) + int(t[3:])

month_arr = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
part_dict, fine_dict = defaultdict(dict), defaultdict(int)
N, L, F = input().split()
N, F = int(N), int(F)
L = (int(L[:3]) * 24 * 60) + (int(L[4:6]) * 60) + int(L[7:9])

for _ in range(N):
    d, t, product, name = input().split()
    if product in part_dict[name]:
        time = calc_seconds(d, t) - part_dict[name][product]
        if time > L:
            fine_dict[name] += (time - L) * F
        del part_dict[name][product]
    else:
        part_dict[name][product] = calc_seconds(d, t)

print("\n".join(f'{k} {fine_dict[k]}' for k in sorted(fine_dict.keys())) if fine_dict else -1)