import redis
import configparser
def redisset():
  # 获取redis的配置文件
  conf = configparser.ConfigParser()
  conf.read('./config/db_config.ini')
  host = conf.get('redis', 'host')
  port = conf.get('redis', 'port')
  db = conf.get('redis', 'db')
  # 普通连接
  conn = redis.Redis(host=host, port=int(port),db=db,decode_responses=True) #python3读取redis返回数据带有'b'的问题,在连接数据库的时候加上decode_responses=True即可
  # 可以使用url方式连接到数据库
  # conn = redis.Redis.from_url('redis://127.0.0.1:6379/1')
  conn.set('name', 'LinWOW')
  print("***********************************************************")
  print(conn.get('name'))