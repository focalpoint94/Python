
N, M = map(int, input().split())
y, x, d = map(int, input().split())

array = []
for i in range(N):
    array.append(list(map(int, input().split())))

dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def rotate_left(d):
    if d == 0:
        return 3
    elif d == 1:
        return 0
    elif d == 2:
        return 1
    else:
        return 2

def look_left():
    global y, x, d
    next_y = y + dirs[d][0]
    next_x = x + dirs[d][1]
    # 안가본 곳이며 바다가 아님
    if array[next_y][next_x] != 1:
        # 좌표 변경 및 회전
        y = next_y
        x = next_x
        d = rotate_left(d)
        # 가본 곳 표시
        array[next_y][next_x] = 1
        # 움직였음
        return 1
    # 가본 곳이거나 바다임
    else:
        # 회전
        d = rotate_left(d)
        # 안움직였음
        return 0

total_count = 1

while (True):
    temp_count = 0
    while temp_count != 4:
        moved = look_left()
        if moved == 1:
            temp_count = 0
            total_count = total_count + 1
        else:
            temp_count = temp_count + 1
    # 뒤쪽 좌표
    back_y = y + dirs[(d + 2) % 4][0]
    back_x = x + dirs[(d + 2) % 4][1]
    # 바다라면
    if array[back_y][back_x] == 1:
        break
    y = back_y
    x = back_x

print(total_count)

