#运用Monte Carno 方法计算圆周率的近似值
import random

def PI(times):
    hits = 0
    for i in range(times):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x ** 2 + y ** 2 <= 1:
            hits += 1
    return 4.0 * hits/times

times = int(input("请输入投掷次数："))
print(PI(times))

