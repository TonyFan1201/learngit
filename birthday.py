#100个人集中在一个房间，至少有两个人生日相同的概率有多大？
Num=100
p=1
for i in range(1,100):
    p=p*(366-i)/365
P=1-p
print("概率为：",end=" ")
print(P)