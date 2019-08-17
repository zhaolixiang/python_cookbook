import os
filename=os.path.dirname(os.path.abspath(__file__))
files1=os.listdir(filename+"/image")
files2=os.listdir(filename)
#any表示该iterable只要存在一个满足条件的，就返回True，否则才返回False
if any(name.endswith('.py') for name in files1):
    print('存在py文件')
else:
    print('不存在py文件')



#any表示该iterable只要存在一个满足条件的，欧返回True，否则才返回False
if any(name.endswith('.py') for name in files2):
    print('存在py文件')
else:
    print('不存在py文件')