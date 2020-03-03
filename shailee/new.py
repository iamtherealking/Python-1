import time
running= True
start_time=time.time() #time taken to reach here
print("start_time : {}".format(start_time))
while running:
    aeleko_time=time.time()
    print("aeleko time : {}".format(aeleko_time))
    second_elapsed=aeleko_time-start_time
    print("second elapsed : {}".format(second_elapsed))
    if second_elapsed==3:
        start_time=aeleko_time
        print("aeleko time : {}".format(start_time))


    