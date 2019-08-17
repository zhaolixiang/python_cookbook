from operator import attrgetter
class User:
    def __init__(self,userId):
        self.userId=userId

    def __repr__(self):
        return 'User({})'.format(self.userId)

users=[User(40),User(20),User(30)]
print(users)

#方法1
print(sorted(users,key=lambda u:u.userId))

#方法2
print(sorted(users,key=attrgetter('userId')))