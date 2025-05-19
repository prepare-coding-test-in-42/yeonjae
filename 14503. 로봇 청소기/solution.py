import sys

def solution():
    # 입력 받기
    N, M = map(int, input().split())        # 방 크기
    r, c, d = map(int, input().split())     # 초기 위치, 방향

    # 방 상태 저장
    room = [list(map(int, input().split())) for _ in range(N)]

    # 방향 벡터 (N, E, S, W)
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    # 청소한 칸 수
    cleaned = 0

    while True:
        # 1. 현재 칸 청소
        if room[r][c] == 0:
            # 청소 표시
            room[r][c] = 2
            cleaned += 1
        
        # 2. 주변 네 칸 탐색
        found = False
        for _ in range(4):
            # 반시계 방향으로 회전 0 -> 3 -> 2 -> 1 -> 0
            d = (d + 3) % 4
            nr, nc = r + dr[d], c + dc[d]

            # 빈 칸 발견 시
            if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0:
                # 이동
                r, c = nr, nc
                found = True
                break
        
        # 3. 청소할 곳을 못 찾은 경우 후진
        if not found:
            # 바라보는 방향의 반대 방향, 180도 회전 0 <-> 2, 1 <-> 3
            back_d = (d + 2) % 4
            nr, nc = r + dr[back_d], c + dc[back_d]

            # 후진한 위치가 벽인지 확인
            if 0 <= nr < N and 0 <= nc < M and room[nr][nc] != 1:
                # 후진
                r, c = nr, nc
            else:
                # 뒤가 벽이면 작동 중지
                break
            
    print(cleaned)


if __name__ == "__main__":
    solution()
