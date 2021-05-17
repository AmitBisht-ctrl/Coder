# di = ['message',{'tag':'success'}]
# nd = {'tag':'success' }
# print(nd['tag'])
# for x in di:
#     print(x)
#     print(x['tag'])

class trual():
    def __init__(self,var):
        self.var = var
        self.add(var)

    def add(self,var):
        self.val = var
        self.val += 10

    def __str__(self):
        return str(self.val)
        
ob = trual(10)
print(ob)
print(id(ob))