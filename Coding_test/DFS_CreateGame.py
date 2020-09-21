#
# 게임 개발
# 1, 현재 바라보는 뱡향에서 왼쪽 방향부터 진행
# 2. 가보지 않으 왼쪽 방향으로 1칸 이동, 간 곳이면 왼쪽 회전만 실행 후, 1번으로 돌아감
# 3. 네 방향이 간곳이나 바다이면, 바라보는 방향의 유치한 채 뒤로 1칸 이동 후, 1번으로 돌아감(이 때 뒤로 가는 칸이 바다이면 움직임 종료)
# 바라보는 방향 - 북:0 동:1 남:2 서:3
# 육지:0 바다:1 (맵의 외각은 항상 바다로 되어 있음)
# 캐릭터가 방문한 칸의 수를 출력하라
#

# input data
#x, y = map(int, input("map_size: ").split())
x, y = 4, 4
#char = list(map(int, input("(x,y) dt : ").split()))
char = [1, 1, 0]
#maps = [list(map(int, input().split())) for i in range(y) ]
maps = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
d = [[0] * y for _ in range(x)]
d[char[0]][char[1]] = 1

# set data
# 바라보는 방향 - 북:0 동:1 남:2 서:3
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

# 1
def turn_left_mv():
    global char
    char[2] -= 1
    if char[2] == -1:
        char[2] = 3

for i in maps:
    print(i)

# start move
count = 1
turn_time = 0
while True:
    turn_left_mv()
    nx = char[0] + dx[char[2]]
    ny = char[1] + dy[char[2]]
    # check land
    if maps[nx][ny] == 0 and d[nx][ny] == 0:
        char[0] = nx
        char[1] = ny
        d[nx][ny] = 1
        count += 1
        turn_time = 0
        continue
    # if sea and went land
    else:
        turn_time += 1
    # Not Forward
    if turn_time == 4:
        nx = char[0] - dx[char[2]]
        ny = char[2] - dy[char[2]]
        if d[nx][ny] == 0:
            x = nx
            y = ny
            turn_time = 0
        else:
            break

print(count)
