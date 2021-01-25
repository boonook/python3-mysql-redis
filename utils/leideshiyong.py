def leideshiyong():
  class employee:
    count=0
    def __init__(self,name):
      self.name = name
      employee.count +=1
    def dayinname(self):
      print(self.name)
  emp1 = employee('boonook')
  emp1.dayinname()
  print(employee.count)