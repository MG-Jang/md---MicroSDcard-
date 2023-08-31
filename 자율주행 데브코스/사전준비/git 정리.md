# Git 정리

- git이란 왜 사용할까? 
여러 이유가 존재하지만 가장 큰 목적은 버전을 관리하기 위해서이다.

- git vs git hub
git은 위에 말한대로 버전 관리시스템,
git hub는 정리를 위한 것

만약 git을 최초로 깔았다면
username과 email을 꼭 등록해줘야 한다.

```
git config --global user.name "MG-Jang"
git config --global user.email "jang23mg@naver.com"
```

git사용순서 
1. respository 를 생성(이때 먼저 Readme 생성을 체크 해제)
2. 생성된 respository로 들어가면 (아래는 예시) 를 git bash에 입력
* 2번을 실행하지 않으면 로컬에서 생성한 내용이 원격(온라인) 으로 올라가지 않는 error가 발생
```
echo "# testing2" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/MG-Jang/testing2.git
git push -u origin main
```
1. 파일을 생성후 push
```
git pull origin main
git add .
git commit -m "제목 적기"
git push origin
```