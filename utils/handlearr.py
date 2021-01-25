def handlearr(arr=[1,2,4,3]):
  """
    函数定义
    :param arr:    数组
  """
  #获取长度
  print(len(arr))
  print(arr)
  # 添加数据
  arr.append(2)
  for x in arr:
    print(x)
  arr.sort()
  print(arr)
  cars = [
    {'car': 'Porsche', 'year': 1963},
    {'car': 'Audi', 'year': 2010},
    {'car': 'BMW', 'year': 2019},
    {'car': 'Volvo', 'year': 2013}
  ]
  def myFunc(e):
    return e['year']
  cars.sort(key=myFunc)
  for i,j in enumerate(cars):
    # 获取数组下标以及获取下标对应的值
    print(i,j)
  for y in cars:
    y['id'] = 1
    print(y['year'])
    print(y)
  print(cars)
