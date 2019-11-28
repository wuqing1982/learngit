a = 1 # 赋值a = 1
def fun(a):
  print("in the fun(a)------->id of a------->"+str(id(a)), "id of 1------->"+str(id(1)))
  a = 2 
  print("when a=2 then a in fun(a)------------>"+str(id(a)),"id of 2 in the fun(a)------->"+str(id(2)))
  
print("re-point","id of a------->"+str(id(a)), "id of 2------->"+str(id(2)))# re-point 41322448 41322448
print("func_out","id of a------->"+str(id(a)), "id of 1------->"+str(id(1))) # func_out 41322472 41322472
fun(a)
print(a) # 1 

#名字空间的问题，函数内部的a，和全局的a不是一个内存存放的位置