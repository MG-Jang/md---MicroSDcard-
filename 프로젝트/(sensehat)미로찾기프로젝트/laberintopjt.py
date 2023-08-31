from sense_hat import SenseHat
from time import sleep
from queue import Queue

sense = SenseHat()

O = [0, 0, 0]  # Red
X = [80, 20, 120]  # White
T = [0, 120, 0]
F = red = (130, 0, 0)
Route = [130, 80, 0]

map = [
O, X, O, O, O, O, O, O,
O, X, X, X, X, O, X, O,
O, O, O, O, O, O, O, O,
O, X, X, X, X, O, X, O,
O, O, X, O, O, O, X, O,
O, O, X, O, X, X, X, O,
O, X, X, O, O, O, O, O,
O, O, O, O, X, X, X, F
    ]

wall = [[0 for j in range(7)] for i in range(7)]
wall = [
[0, 1, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 0, 1, 0],
[0, 0, 1, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 1, 1, 1, 0],
[0, 1, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 1, 1, 0]
    ]

def wall_check(y,x):
    #print("wall:",wall[x][y])
    if wall[x][y] == 1:
        return 0
    else:
        return 1

def inside_map(x,y): 
    if ( 0 <= x <= 7) & ( 0 <= y <= 7):
        #print("check",x,y)
        #print("wall_check",wall_check(x,y))
        if wall_check(x,y):
            #print("check",x,y)
            return 1
        else :
            return 0
    else: 
        return 0 

sense.clear(255,255,255)
sense.set_pixels(map)

tx = 0
ty = 0

# find short route

q = Queue()
dr = [1,-1,0,0]  
dc = [0,0,-1,1]

flag = 0

cx =7
cy = 7
flag = 0 


while True:
    #sense.clear(255,255,255)
    sense.set_pixels(map)
    sense.set_pixel(tx,ty,T)
    for event in sense.stick.get_events():
        if (event.direction == "right") & (event.action == "pressed"):
            if inside_map(tx +1,ty):
                tx +=1
        if (event.direction == "left") & (event.action == "pressed"):
            if inside_map(tx -1,ty):
                tx -=1
        if (event.direction == "down") & (event.action == "pressed"):
            if inside_map(tx ,ty +1):
                ty +=1
        if (event.direction == "up") & (event.action == "pressed"):
            if inside_map(tx,ty -1):
                ty -=1

    #sense.clear()
    #sleep(0.5)
    # find route start
    map_visit = [[0 for j in range(8)] for i in range(8)]
    map_num = [[0 for j in range(8)] for i in range(8)]
    map_visit[tx][ty] =1
    flag = 0
    q.__init__()
    q.put([tx,ty])
    flag = 0
    while True:
        #print("qsize",q.qsize())
        if q.qsize() == 0:
                flag =1
        A = q.get()

        # for i in range(8):
        #     print(map_num[i])

        for i in range (4):
            ax = A[0] - dc[i]
            ay = A[1] - dr[i]
            if((ax == 7) & ( ay == 7)):
                map_num[ax][ay] = map_num[A[0]][A[1]] + 1
                flag =1
            elif inside_map(ax, ay):
                if(map_visit[ax][ ay] == 0):
                    map_visit[ax][ ay] = 1
                    map_num[ax][ay] = map_num[A[0]][A[1]] + 1
                    q.put([ax, ay])
        if flag == 1:
            break
    print("dis", map_num[7][7])
    flag = 0
    dis = map_num[7][7]
    cx =7
    cy = 7
    while True:
        dis -=1
        for i in range (4):
            if(dis == 0):
                flag =1
                break 
            px = cx - dc[i]
            py = cy - dr[i]
            if inside_map(px, py):
                if(map_num[px][py] == dis):
                    print("hi")
                    sense.set_pixel(px,py,Route)
                    #sleep(1)
                    map_num[px][py] = -1
                    cx = px
                    cy = py
                    break
        if flag == 1:
            break

    #find route end
    
    
    
    
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x=round(x, 0)
    y=round(y, 0)
    z=round(z, 0)
    if x == -1.0 :
        #print("1")
        if inside_map(tx -1,ty):
            tx -= 1
    elif x == 1.0:
        #print("2")
        if inside_map(tx+1,ty):
            tx += 1
    if y == -1.0 :
        #print("3")
        if inside_map(tx ,ty -1):
            ty -= 1
    elif y == 1.0:
        #print("4")
        if inside_map(tx,ty + 1):
            ty += 1
    sleep(0.5)
    #print("x={0}, y={1}, z={2}".format(x, y, z))
    for i in range(8):
        print(map_num[i])
    if tx== 7 & ty == 7:
        break 

sense.show_message("YOU WIN~~")
sleep(2)
se.clear()