class Solution:
    def jumFloor(self,n):
        x, y = 1, 1
        for i in range(n):
            x, y =y, x+y
        return x

s = Solution()
n=int(input("青蛙要跳到多少级台阶："))
s.jumFloor(n)
print("跳法种数：",end=" ")
print(s.jumFloor(n))
