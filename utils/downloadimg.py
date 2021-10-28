import re
import requests
 
def downloadimg():
    count=1
    img_url = 'http://static.zongheng.com/upload/cover/40/d7/40d70cf9e2fd824f490da6f7ac4a8e8c.jpeg'
    r = requests.get(img_url,timeout=5)
    filename = "images/"+str(count)+'.jpeg'
    
    print(r.status_code) # 返回状态码
    if r.status_code == 200:
        open('C:\\Users\\cloudoxou\\Desktop\\img.png', 'wb').write(r.content) # 将内容写入图片
        print("done")
    del r