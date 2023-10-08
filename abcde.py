#有一个五位数abcde，乘以4以后变成edcba，abcde是多少？
def loop():
    for i in range(10000, 100000):
        a = i // 10000
        b = i % 10000 // 1000
        c = i % 1000 // 100
        d = i % 100 // 10
        e = i % 10
        r = e * 10000 + d * 1000 + c * 100 + b * 10 + a
        if i * 4 == r:
            print("找到了：",end=" ")
            print(i)
            return  #找到就结束
loop() #运行函数