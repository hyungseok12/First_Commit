# First_Commit

## 1. Remote 연결 및 브랜치 생성

### 원격 저장소 연결
```bash
# 디렉토리로 이동
cd /Users/f2407ln0001/Desktop/lim/First_Commit

# Git 저장소 초기화 (아직 안 했다면)
git init

# 원격 저장소 연결
git remote add origin https://github.com/hyungseok12/First_Commit.git

# 원격 저장소 연결 확인
git remote -v

# 파일 추가 및 커밋
git add .
git commit -m "first commit"

# 원격 저장소에 푸시
git branch -M main
git push -u origin main
```

### 이미 origin이 존재하는 경우
```bash
# 기존 원격 저장소 URL 변경
git remote set-url origin https://github.com/hyungseok12/First_Commit.git

# 변경 확인
git remote -v

# 푸시
git push -u origin main
```

### 새 브랜치 생성 및 Push (브랜치명 lim.h에 대한 예시)
```bash
# 새 브랜치 생성 및 전환
git checkout -b lim.h

# 변경사항 커밋 (필요시)
git add .
git commit -m "lim.h 브랜치 생성"

# 원격 저장소에 브랜치 push
git push -u origin lim.h

# 브랜치 확인
git branch -a
```

## 2. 커밋 템플릿

### 문제
(문제 링크)

### 문제 재정의
- 재정의한 문제 설명 또는 의사코드
- I/O 및 Constraint

### 프롬프트
- AI에게 준 지시문

### 최종 코드
(AI 결과물 및 내 수정)

### 회고 (optional)
- 배운 점 등등
