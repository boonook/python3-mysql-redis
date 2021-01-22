import time  # 引入time模块\
from utils.model1 import models1
from utils.mysqlset import mysqlset
from utils.redisset import redisset
from utils.handlearr import handlearr
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
  handlearr()
ceshi()