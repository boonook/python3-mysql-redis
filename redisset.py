import redis
def redisset():
  # 普通连接
  conn = redis.Redis(host='127.0.0.1', port=6379,db="1")
  # 可以使用url方式连接到数据库
  # conn = redis.Redis.from_url('redis://127.0.0.1:6379/1')
  conn.set('name', 'LinWOW')
  print("***********************************************************")
  print(conn.get('name'))