# di = ['message',{'tag':'success'}]
# nd = {'tag':'success' }
# print(nd['tag'])
# for x in di:
#     print(x)
#     print(x['tag'])

# class trual():
#     def __init__(self,var):
#         self.var = var
#         self.add(var)

#     def add(self,var):
#         self.val = var
#         self.val += 10

#     def __str__(self):
#         return str(self.val)
        
# ob = trual(10)
# print(ob)
# print(id(ob))

# def fun(*arg,**kwargs):
#     for i in arg:
#         print(i)

#     print('kwargs:',kwargs)
#     for key,value in kwargs.items():
#         print(key,value)

# names = ['amit', 'bisht', 'singh']
# fun(letter='l', metter='m','amit')

class a:
    variab = 10
    def helloprint(self):
        print('hello')

o = a;
ins = o.__class__
print(type(ins))
# ins.variab