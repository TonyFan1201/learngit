num = input("请输入要计算的数值（1 - 100）：")
num = int(num)
if num >= 1 and num <= 100:
    i = 1
    result = 1  # 结果
    while i <= num:
        result = result * i
        i = i + 1
    # 不适用缩进的代码，表示while循环结束后继续执行的语句
    print("最终结果：{}".format(result))
else:
    print("请输入有效数字")