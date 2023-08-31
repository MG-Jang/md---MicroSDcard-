# Opencv 설치 및 버전 확인

- opencv 버전 확인
```
$ pkg-config --modversion opencv

# cmd터미널에서 확인하는 경우
$ opencv_version
```

- 참고사이트: https://velog.io/@mouse0429/openCVVisual-Studio-OpenCV-%EC%84%A4%EC%B9%98

주의 사항: 위 명령어로 opencv 버전 확인 후 마지막
``` opencv_world460.lib``` 에서 버전에 맞게 작성해줄것 (안하면 error발생)