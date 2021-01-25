import pymysql
import configparser
def mysqlset():
  # 获取数据库的配置文件
  conf = configparser.ConfigParser()
  conf.read('./config/db_config.ini')
  print(type(conf))
  sections = conf.sections()  #获取配置文件中所有sections，sections是列表
  print(sections)
  host = conf.get('mysql', 'host')
  port = conf.get('mysql', 'port')
  user = conf.get('mysql', 'user')
  password = conf.get('mysql', 'password')
  db_name = conf.get('mysql', 'db_name')
  charset = conf.get('mysql', 'charset')
  # 打开数据库连接
  #连接数据库
  db=pymysql.connect(host=host # 连接名称，默认127.0.0.1
  ,user=user # 用户名
  ,passwd=password # 密码
  ,port=int(port) # 端口，默认为3306
  ,db=db_name # 数据库名称
  ,charset=charset # 字符编码
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