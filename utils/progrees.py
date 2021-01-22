import time


def progrees(percent, width=100):
    '''
    进度打印功能
    :param percent: 进度
    :param width: 进度条长度
    '''
    if percent >= 100:
        percent = 100

    show_str = ('[%%-%ds]' % width) % (int(width * percent / 100) * "#")  # 字符串拼接的嵌套使用
    print('\r%s %d%%' % (show_str, percent), end='')