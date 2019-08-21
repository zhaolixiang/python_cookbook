import re

str_pat=re.compile(r'/\*(.*?)\*/')
text1="/* mark */"
text2='''/* mark 
            2018    */'''
print(str_pat.findall(text1))
print(str_pat.findall(text2))



import re

#将.换成(?:.|\n)
str_pat=re.compile(r'/\*((?:.|\n)*?)\*/')
text1="/* mark */"
text2='''/* mark 
            2018    */'''
print(str_pat.findall(text1))
print(str_pat.findall(text2))



import re

str_pat=re.compile(r'/\*(.*?)\*/',re.DOTALL)
text1="/* mark */"
text2='''/* mark 
            2018    */'''
print(str_pat.findall(text1))
print(str_pat.findall(text2))