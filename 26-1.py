import re

str_pat=re.compile(r'\"(.*)\"')
text1='mark say "love"'
text2='mark say "love",jingjing say "yes"'
print(str_pat.findall(text1))
print(str_pat.findall(text2))




import re

str_pat=re.compile(r'\"(.*?)\"')
text1='mark say "love"'
text2='mark say "love",jingjing say "yes"'
print(str_pat.findall(text1))
print(str_pat.findall(text2))