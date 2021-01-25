user,passwd = 'zxw',1234
def zhuangshifu():
  print("zhuangshifu")
  def auth(type):
    def outwrapper(func):
      def wrapper(*args,**kwargs):
          print('wrapper2')
          if type == 'lll':
              username = input('username:').strip()
              password = int(input('password:').strip())
              if user == username and passwd == password:
                  print("\033[32;1muser pass ~~~~~~\033[0m")
                  func(*args,**kwargs)
              else:
                  exit("\033[31;1minvalid user ~~~~~~\033[0m")
          elif type == 'kkk':
              print('fuck off')
      return wrapper
    return outwrapper

  @auth('lll')
  def home():
    print("welcome to index page")
  home()