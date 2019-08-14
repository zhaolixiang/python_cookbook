line='nobody:*:-2:-2:unp user:/var/empty:/user/nim/false'

uname,*fileds,homedir,sh=line.split(':')
print(uname)
print(homedir)
print(sh)