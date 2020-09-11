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
x, y = map(int, input("map_size: ").split())
char = map(int, input("(x,y) dt : ").split())
maps = [list(map(int, input().split())) for i in range(y) ]

# set data
# 바라보는 방향 - 북:0 동:1 남:2 서:3
dt = [0, 1, 2, 3]

# 1
def trun_left_mv():
   char[2] = (char[2] + 1) % 4
   if char[2] == 0 :
       char[1] -= 1
   if char[2] == 1 :
       char[0] -= 1
   if char[2] == 2 :
       char[1] += 1
   if char[2] == 3 :
       char[0] += 1


