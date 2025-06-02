import time

def timer (end, start = 1):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done")

timer(10)