from utils.ceshi import ceshi
import configparser
def main():
  # print('main')
  ####读取服务的配置信息
  conf = configparser.ConfigParser()
  print(type(conf))           #conf是类
  conf.read('./config/db_config.ini')
  # 获取所有 sections
  sections = conf.sections()  #获取配置文件中所有sections，sections是列表
  print(sections)
  # 获取指定 key 的 value
  value = conf.get('mysql', 'host')   #根据section和value获取key值,等价于value = conf.get(conf.sections()[0], conf.options(conf.sections()[0])[0])
  print(value)
  ceshi()
if __name__ == '__main__':
    main()