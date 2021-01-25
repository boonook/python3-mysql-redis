import copy
def hanshu():
  # lambda函数：首要用途是指点短小的回调函数
  sum = lambda arg1,arg2:arg1+arg2
  print(sum(1,2))
  print(123)
  # list去重
  a=[1,2,4,2,4,5,6,5,7,8,9,0]
  # 1.使用set去重
  print(set(a))
  # 深拷贝和浅拷贝
  obj = {"id":"1","name":"BOONOOK"}
  obj2 = obj
  obj2['age'] = 17
  print(obj)
  #**
  # {'id': '1', 'name': 'BOONOOK', 'age': 17}
  # **#
  obj3 = [1, 2, 3, ['a', 'b']]
  obj4 = copy.copy(obj3)
  obj4[3].append('cccccc')
  print('obj4',obj4)  # [1, 2, 3, ['a', 'b', 'cccccc']]
  print('obj3',obj3)  # [1, 2, 3, ['a', 'b', 'cccccc']]

  obj5 = {"id":"1","name":"BOONOOK","info":{"email":'boonook@163.com',"role":{"roleName":"admin"}}}
  obj6=copy.deepcopy(obj5)
  obj6['age'] = '27'
  print('obj6',obj6)
  print('obj5',obj5)


