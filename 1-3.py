import numpy as np

grades=list(range(10))#定义一个0-9的分数列表
print("grades:"+str(grades))
first,*middle,last=grades
print("middle:"+str(middle))
print("去掉第一个和最后一个分数后的平均值："+str(np.mean(middle)))