import random
def randomdata():
  a = random.random()
  print(a)
  # 用于生成一个指定范围内的随机浮点数，生成的随机数n: a <= n <= b
  print(random.uniform(1,10))
  # 用于生成一个指定范围内的整数，生成的随机数n: a <= n <= b
  print(random.randint(1,10))
  #.random.randrange([start], stop[, step])，从指定范围内，按指定基数递增的集合中 获取一个随机数。
  print(random.randrange(10,30,2))
  #
  p = ['A' , 'B', 'C', 'D', 'E' ]
  random.shuffle(p)
  print('随机配徐',p)