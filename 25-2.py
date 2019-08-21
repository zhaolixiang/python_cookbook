import re
text='Mark is a handsome guy and mark is only 18 years old.MARK'

def matchcase(word):
    def replace(m):
        #re.sub会将匹配到的对象，循环调用replace方法传入
        print(m)
        #获取匹配的文本
        text=m.group()
        if text.isupper():
            #如果文本全部是大写，就返回word的全部大写模式
            return word.upper()
        elif text.islower():
            # 如果文本全部是小写，就返回word的全部小写模式
            return word.lower()
        elif text[0].isupper():
            #如果文本是首字母大写，就返回word的首字母大写模式
            return word.capitalize()
        else:
            #其他情况，直接返回word
            return word
    return replace

result=re.sub('mark',matchcase('python'),text,flags=re.IGNORECASE)

print(result)