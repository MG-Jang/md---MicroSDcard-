# ROS 정리

1. 노드에서 노드로 topic을 전송
2. 이때 전송노드를 publisher, 받는노드를 Subscriber
3. 마스터 코어는 노드의 전체적인 정보 관리를 한다.

### 필수 명령어 정리 <hr>
```py
$ roscore # ROS master 실행
$ roslist # 패키지 나열
$ rospack find [package_name] # 패키지 검색
$ rosce [location_name[/subdir]] # ROS 패키지 디렉토리로 이동
$ rosls [location_name[/subdir]] # ROS 버전의 ls 명령어
```

<br>

 ### ROS 실행 방법<hr>
- 참고: 만약 ROS 설치가 안된경우는 ROS 설치 내용을 참고해서 설치

1. ROS master 실행 
```py
$ roscore
```
2. ROS node 실행 (어떤 노드들이 실행되고 있는지 확인) 
```py
$ rosnode list
```
3. ROS Topic 
```py
$ rostopic list
# 만약 publiser와 subscriber + 더 정확한 정보를 보고 싶다면
$ rostopic list -v
# topic의 내용을 알고 싶은 경우
$ rostopic echo {topic 이름}
ex) rostopic echo /turtle1/cmd_vel
# topic의 type을 알고 싶은 경우
$ rostopic type {topic 이름}
ex) rostopic type /turtle1/cmd_vel
```
4. node 와 주고받는 topic을 시각화해서 보고싶은 경우
```py
$ rqt_graph
```


ex) <img src = "../img/rqt_graph_ex.JPG">

- teleop_turtle: publisher , turtlesim: subscriber , turtle1/cmd_vel : 전송topic
