import time
running=True
start_time=time.time()
print("start_time{}".format(start_time))
while running:
    now_time=time.time()
    print("now_time{}".format(now_time))
    second_depends=now_time-start_time
    print("second_depends{}".format(second_depends))
    if second_depends==3:
        start_time=now_time
        print("now_time:{}".format(start_time))
        second_depends=int()