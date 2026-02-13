"""
## 문제
https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/

## 문제 재정의
- 내 말로 정리:
    [문제 요약]
        - Mountain Triplet이란 i < j < k 이고 arr[i] < arr[j] > arr[k]를 만족하는 (i, j, k) 쌍을 의미한다.
        - 주어진 배열에서 Mountain Triplet의 최소합을 반환.
    [문제 재정의]
        - 전체 배열 양 끝을 제외한 모든 원소는 Mountain Triplet의 중점 후보가 된다.
        - 중점 후보를 기준으로 왼쪽과 오른쪽에서 중점보다 작은 원소 중 최소값을 찾아 합산에서 저장하고, 저장된 값들 중 최소값을 반환.
- 입력 / 출력 / 제약:
    - 입력: 정수 배열 arr (3 <= arr.length <= 1000, 1 <= arr[i] <= 10^6)
    - 출력: Mountain Triplet의 최소합 (정수)
    - 제약: 시간 복잡도 O(n^2) 이하, 없으면 -1 반환

## 수도코드
1. min_sum = ∞으로 초기화
2. j를 1부터 n-2까지 반복 (중점 후보):
    2-1. peak = arr[j]
    2-2. 왼쪽(0~j-1)에서 peak보다 작은 최솟값 찾기 → left_min
    2-3. 오른쪽(j+1~n-1)에서 peak보다 작은 최솟값 찾기 → right_min
    2-4. 둘 다 존재하면: min_sum = min(min_sum, left_min + peak + right_min)
3. min_sum이 ∞이면 -1 반환, 아니면 min_sum 반환

## 프롬프트
없음

## 최종 코드
1. 시간 복잡도 O(n^2) 풀이: 수도코드를 그대로 구현
    - 문제점: 왼쪽 오른쪽 중복 리스트 탐색으로 O(n) * 중점 후보 O(n) = O(n^2)
    - 개선점: 왼쪽과 오른쪽의 최소값을 미리 저장하여 탐색 시간을 줄일 수 있음
2. 시간 복잡도 O(n) 풀이: 왼쪽과 오른쪽의 최소값을 미리 저장
    - 왼쪽 최소값 배열과 오른쪽 최소값 배열을 각각 생성
    - 중점 후보를 기준으로 왼쪽과 오른쪽의 최소값을 바로 참조하여 합산
    - O(n) 탐색 3번만 반복

## 회고
- 리스트는 효율적이지 못한 자료구조 중 하나이므로 신중히 사용하자.
- 시간복잡도를 염두에 두고 풀이하는 연습이 필요하다.
"""

from typing import List
from math import inf


# 1. 시간 복잡도 O(n^2) 풀이
def minimumSum(self, nums: List[int]) -> int:
    min_sum = float(inf)
    for i in range(1, len(nums) - 1):
        peak = nums[i]
        left_ls = [l for l in nums[:i] if l < peak]
        right_ls = [r for r in nums[(i + 1) :] if r < peak]
        if len(left_ls) > 0 and len(right_ls) > 0:
            min_sum = min(min_sum, min(left_ls) + peak + min(right_ls))
    if min_sum == float(inf):
        return -1
    else:
        return min_sum


# 2. 시간 복잡도 O(n) 풀이
def minimumSum(self, nums: List[int]) -> int:
    n = len(nums)

    left_min = [float(inf)] * n
    right_min = [float(inf)] * n

    for i in range(1, n):
        left_min[i] = min(left_min[i - 1], nums[i - 1])

    for i in range(n - 2, -1, -1):
        right_min[i] = min(right_min[i + 1], nums[i + 1])

    min_sum = float(inf)
    for j in range(1, n - 1):
        if left_min[j] < nums[j] and right_min[j] < nums[j]:
            min_sum = min(min_sum, left_min[j] + nums[j] + right_min[j])

    return -1 if min_sum == float(inf) else min_sum
