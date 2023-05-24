# 导入time模块
import time

# 定义工作时间和休息时间（单位为秒）
work_time = 25 * 60
break_time = 5 * 60

# 定义一个计时器函数，接受一个时间参数
def timer(seconds):
    # 获取当前时间
    start_time = time.time()
    # 计算结束时间
    end_time = start_time + seconds
    # 循环检查当前时间是否达到结束时间
    while time.time() < end_time:
        # 获取剩余时间
        remain_time = end_time - time.time()
        # 将剩余时间转换为分和秒
        minutes = int(remain_time // 60)
        seconds = int(remain_time % 60)
        # 打印剩余时间，使用\r覆盖上一行
        print(f"{minutes:02}:{seconds:02}", end="\r")
        # 每隔一秒刷新一次
        time.sleep(1)
    # 打印换行符
    print()

# 定义一个专注时钟函数，接受工作时间和休息时间参数
def focus_clock(work_time, break_time):
    # 定义一个计数器变量，记录完成的任务数
    count = 0
    # 循环执行以下操作
    while True:
        # 打印开始工作的提示信息
        print("开始工作！")
        # 调用计时器函数，传入工作时间参数
        timer(work_time)
        # 工作时间结束后，计数器加一
        count += 1
        # 打印完成任务的提示信息，并显示计数器的值
        print(f"完成任务！已完成{count}个任务。")
        # 打印开始休息的提示信息
        print("开始休息！")
        # 调用计时器函数，传入休息时间参数
        timer(break_time)
        # 休息时间结束后，打印结束休息的提示信息，并询问是否继续工作
        print("结束休息！")
        answer = input("是否继续工作？（y/n）")
        # 如果回答是y或Y，继续循环；否则，退出循环
        if answer.lower() == "y":
            continue
        else:
            break

# 调用专注时钟函数，传入工作时间和休息时间参数
focus_clock(work_time, break_time)
