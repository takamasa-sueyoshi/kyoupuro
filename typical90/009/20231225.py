from math import atan2, degrees
from bisect import bisect_left

N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0

for current in range(N):
    # その他点とで出来上がる偏角を格納する配列
    angles = []
    for target in range(N):
        if current == target: continue
        X = XY[target][0] - XY[current][0]
        Y = XY[target][1] - XY[current][1]
        angle = degrees(atan2(Y, X)) % 360
        angles.append(angle)

    angles.sort()

    for index in range(len(angles)):
        target_angle = angles[index]

        need_angle = (target_angle + 180) % 360

        need_index = min(bisect_left(angles, need_angle), N-2)

        angle_a = min(abs(target_angle - angles[need_index]), 360 - abs(target_angle - angles[need_index]))
        angle_b = min(abs(target_angle - angles[need_index - 1]), 360 - abs(target_angle - angles[need_index - 1]))

        ans = max(ans, angle_a, angle_b)

print(ans)
