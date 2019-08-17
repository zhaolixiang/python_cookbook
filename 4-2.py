class Item:
    def __init__(self,name):
        self.name=name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)

if __name__ == '__main__':
    a=(1,Item('foo'))
    b=(5,Item('bar'))
    #下面一句打印True
    print(a<b)


    c=(1,Item('grok'))
    #下面一句会报错：TypeError: '<' not supported between instances of 'Item' and 'Item'
    print(c<a)


    d=(1,0,Item('foo'))
    e=(5,1,Item('bar'))
    f=(1,2,Item('grok'))
    #下面一句打印True
    print(d<e)
    #下面一句打印True
    print(d<f)