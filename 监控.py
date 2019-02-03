import psutil,time
#具体参数请见 #https://github.com/giampaolo/psutil

#cpu相关的监控
# psutil.cpu_count()#CPU数量
# print(psutil.cpu_times())#统计cpu用户/系统/空闲时间
#类似top一般监控cpu状态的指令
# for x in range(100):
#     print(psutil.cpu_percent(interval=1,percpu=True))
#     time.sleep(0.1)

#内存相关的监控
# # print(psutil.virtual_memory())#打印物理内存信息
# print(psutil.swap_memory())#打印交换内存的信息

# #磁盘相关的监控
# # print(psutil.disk_partitions())#打印磁盘分区信息
# print(psutil.disk_usage('/'))#打印出磁盘使用情况
# print(psutil.disk_io_counters())#磁盘Io信息


# #网络接口
# # print(psutil.net_io_counters())#网络读写包的个数
# print(psutil.net_if_stats())#获取网卡信息
# print(psutil.net_if_addrs())#获取网络地址


#获取进程信息
print(psutil.pids())#获取进程ID
print(psutil.Process(1).name())#获取进程x x= 1 的名字

