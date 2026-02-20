"""
## 문제
https://leetcode.com/problems/unique-paths-ii/

## 문제 재정의
- 내 말로 정리:
    [문제 요약]
        - m x n 격자에서 시작점에서 도착점까지 이동할 수 있는 유일한 경로의 수를 구하는 문제이다.
        - 격자에는 장애물이 있을 수 있으며 장애물이 있는 칸은 지나갈 수 없다.
        - 좌상단에서 오른쪽 또는 아래쪽으로만 이동할 수 있다.
    [문제 재정의]
        - DP 테이블을 만들어서 각 칸까지 도달할 수 있는 경로의 수를 저장한다.
        - DP 테이블의 초기값(좌상단)은 시작점이 장애물이 아니면 1, 장애물이면 0으로 설정한다.
        - DP 테이블을 채울 때, 각 칸이 장애물이 아니면, 위쪽과 왼쪽에서 오는 경로의 수를 더해서 저장한다.
        - 최종적으로 도착점에 저장된 값이 답
- 입력 / 출력 / 제약:
    - 입력: 2D 정수 배열 obstacleGrid (m x n 격자, 0은 빈 칸, 1은 장애물)
    - 출력: 시작점에서 도착점까지 이동할 수 있는 유일한 경로의 수 (정수)
    - 제약:
        - 1 <= m, n <= 100
        - obstacleGrid[i][j] is 0 or 1.

## 수도코드
1. rows, cols = 격자의 행/열 수
2. dp[rows][cols]을 0으로 초기화
3. 시작점이 장애물이면 → 0 반환
4. dp[0][0] = 1
5. 모든 셀 (i, j)를 순회:
    5-1. 장애물이면 → dp[i][j] = 0
    5-2. 아니면:
        - i > 0이면 → dp[i][j] += dp[i-1][j]
        - j > 0이면 → dp[i][j] += dp[i][j-1]
6. dp[rows-1][cols-1] 반환

## 프롬프트
없음

## 최종 코드
하단 참조

## 회고
시작점이 장애물인 경우 즉시 0을 반환하는 것을 잊지 말자.
"""

from utils import List


def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    rows = len(obstacleGrid)
    cols = len(obstacleGrid[0])
    dp = [[0] * cols for _ in range(rows)]
    if obstacleGrid[0][0] == 1:
        return 0
    else:
        dp[0][0] = 1
        for i in range(rows):
            for j in range(cols):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] += dp[i - 1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j - 1]
    return dp[-1][-1]
