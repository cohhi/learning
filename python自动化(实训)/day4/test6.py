import time


def get_test(start, end):
    starttime = time.time()
    total = 0
    for i in range(start, end + 1):
        total += i

    endtime = time.time()

    print(endtime - starttime)  # 妙啊,简直顶呱呱


get_test(1, 10000000)
