"""
## 문제
https://leetcode.com/problems/unique-paths-iii/

## 문제 재정의
- 내 말로 정리:
    [문제 요약]
        - m x n 격자에서 시작점(1)에서 도착점(2)까지 4방향(상하좌우)으로 이동할 수 있다.
        - 장애물(-1)이 아닌 모든 빈 칸(0)을 정확히 한 번씩 방문하는 경로의 수를 구하는 문제이다.
        - 격자 값: 1=시작점, 2=도착점, 0=빈 칸, -1=장애물
    [문제 재정의]
        - 백트래킹(DFS)으로 시작점에서 출발하여 4방향 탐색한다.
        - 방문한 칸을 체크하며, 도착점에 도달했을 때 모든 빈 칸을 방문했는지 확인한다.
        - 모든 빈 칸을 방문한 상태로 도착점에 도달하면 유효한 경로 +1
- 입력 / 출력 / 제약:
    - 입력: 2D 정수 배열 grid (m x n 격자)
    - 출력: 모든 빈 칸을 정확히 한 번 방문하며 시작→도착하는 경로의 수 (정수)
    - 제약:
        - 1 <= m, n <= 20
        - 1 <= m * n <= 20
        - -1 <= grid[i][j] <= 2
        - 시작점(1)과 도착점(2)은 정확히 하나씩 존재

## 수도코드
1. 격자를 순회하며:
    1-1. 시작점(1)의 좌표 (sr, sc)를 기록
    1-2. 방문해야 할 칸 수(empty) 세기 (빈 칸(0) + 시작점(1) + 도착점(2))
2. DFS 백트래킹 함수 정의 (i, j, remain):
    2-1. 범위 밖이거나 장애물(-1)이거나 이미 방문했으면 → return
    2-2. 도착점(2)에 도달하면:
        - remain == 1이면 (마지막 남은 칸이 도착점) → 경로 수 +1
        - 아니면 → return (아직 빈 칸이 남아있음)
    2-3. 현재 칸을 방문 처리 (장애물로 표시)
    2-4. 4방향(상하좌우)으로 재귀 호출 (remain - 1)
    2-5. 현재 칸을 원복 (백트래킹)
3. DFS(sr, sc, empty) 호출
4. 경로 수 반환

## 프롬프트
m x n 격자에서 시작점(1) → 도착점(2)까지 4방향 이동하며 장애물(-1)을 제외한 모든 빈 칸(0)을 정확히 한 번씩 방문하는 경로의 수를 구해.
DFS 백트래킹으로 풀어. 방문 처리는 별도 배열(visited로 이름 붙여)에 저장하는 방법이 먼저 떠오르지만 더 효율적인 방법 있으면 제안해.
먼저 격자를 순회해서 시작점 좌표와 방문해야 할 칸 수(빈 칸 + 시작점, 도착점 제외)를 세고, DFS에서 remain이 0인 상태로 도착점에 도달하면 유효한 경로로 카운트.
현재 경로 내 utils.py에서 자료구조 import한 거 있으면 그거 활용해서 풀어.

## 최종 코드
하단 참조

## 회고
격자 자체에 방문 표시(-1로 장애물처럼 임시로 만듦)하는 방법이 별도의 visited 배열보다 공간 효율적이면서도 코드가 간결해짐.
"""

from utils import List


def uniquePathsIII(self, grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])

    remain = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                start = [r, c]
                remain += 1
            if grid[r][c] == 0:
                remain += 1

    def dfs(r, c, remain):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == -1:
            return 0
        if grid[r][c] == 2:
            return 1 if remain == 0 else 0

        anchor = grid[r][c]
        grid[r][c] = -1
        remain -= 1

        total = 0
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            total += dfs(r + dr, c + dc, remain)

        grid[r][c] = anchor
        remain += 1

        return total

    return dfs(start[0], start[1], remain)
