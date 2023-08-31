# ROS 노드 동기화 문제 해결

만약 받을 사람이 준비가 안된경우 물건을 던지면 받을 수 가 없고 잃어 버린다.
-> 이를 해결하기 위해 Topic을 받을 준비가 된 Node가 존재하는지 확인하는 작업을 거친다.

```py
get_num_connections()
#topic을 받을 node가 존재하지 않으면 0
#topic을 받을 node가 존재하면 1
```


## 예제 코드 <hr>
> sender_serial.py
```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Int32

rospy.init_node('sender_serial')

pub = rospy.Publisher('my_topic',Int32)

rate = rospy.Rate(5)
count = 1

#====topic을 받을 node가 생길때까지 대기===== 
while(pub.get_num_connections() == 0):
    count = 1
#==========================================
while not rospy.is_shutdown():
    pub.publish(count)
    count = count + 1
    rate.sleep() 
```

> receiver_serial.py
```py
#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def callback(msg):
    print msg.data

rospy.init_node('receiver_serial')

sub = rospy.Subscriber('my_topic',Int32,callback)

rospy.spin()
```