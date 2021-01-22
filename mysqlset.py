import pymysql
def mysqlset():
  # 打开数据库连接
  #连接数据库
  db=pymysql.connect(host = '127.0.0.1' # 连接名称，默认127.0.0.1
  ,user = 'root' # 用户名
  ,passwd='1234' # 密码
  ,port= 3306 # 端口，默认为3306
  ,db='zhdj' # 数据库名称
  ,charset='utf8' # 字符编码
  )
  # # 使用cursor()方法获取操作游标
  cursor = db.cursor()
  # # SQL 查询语句
  sql = "SELECT * FROM user"
  try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
      id = row[0]
      name = row[1]
      # 打印结果
      print (str(id)+name)
  except:
    print ("Error: unable to fetch data")
  # 关闭数据库连接
  db.close()