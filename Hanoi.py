#汉诺塔问题编程解答。
def move(n,A,B,C):  #n为圆盘数，A是初始圆柱，B是中间圆柱，C是目标圆柱
    if n==1:
        print(A,"-->",C)
    else:
        move(n-1,A,C,B)
        print(A,"-->",C)
        move(n-1,B,A,C)

n=int(input("请输入圆盘数："))
move(n,'A','B','C')