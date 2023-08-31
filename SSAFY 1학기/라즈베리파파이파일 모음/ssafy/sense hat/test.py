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