import time  # 引入time模块\
from utils.model1 import models1
from utils.mysqlset import mysqlset
from utils.redisset import redisset
from utils.handlearr import handlearr
from utils.progrees import progrees
def ceshi():
  print('123123123')
  dict = {'a': 1, 'b': 2, 'b': '3'}
  print(dict['a'])
  ticks = time.time()
  print(ticks)
  localtime = time.localtime(time.time())
  print(localtime)
  localtimes = time.asctime(time.localtime(time.time()))
  print(localtimes)
  print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
  print("**********************************************************************************")
  class employee:
    count=0
    def __init__(self,name):
      self.name = name
      employee.count +=1
    def dayinname(self):
      print(self.name)
  emp1 = employee('boonook')
  emp2 = employee('boonook2')
  emp1.dayinname()
  print(employee.count)
  a = models1()
  print(a)
  mysqlset()
  # 链接redis
  redisset()
  print("*******************************************操作数组start***************************************")
  handlearr()
  print("*******************************************操作数组end***************************************")

  #打印进度条
  # =========应用==========
  data_size = 3030333  # 定义传输的数据，实际应用中这个值改一下就可以了
  recv_size = 0
  while recv_size < data_size:
    #time.sleep(0.01)  # 模拟数据的传输延迟
    recv_size += 1024  # 每次收1024
    recv_per = int(100 * recv_size / data_size)  # 接收的比例
    progrees(recv_per, width=100)  # 调用进度条函数，进度条的宽度默认设置为30
  #打印进度条完毕
ceshi()