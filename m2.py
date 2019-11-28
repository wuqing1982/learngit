def foo(x):
    print("executing foo(%s)"%(x))

class A(object):
    def foo(self,x):
        print("executing foo(%s,%s)"%(self,x))

@classmethod
def class_foo(cls,x):
    print("executing class_foo(%s,%s)"%(cls,x))

@staticmethod
def static_foo(x):
    print("executing static_foo(%s)"%(x))



A.play=static_foo #静态方法属于类，应该添加到类上面，所有对象都自动拥有play属性

a=A()

foo("1---普通方法") 

a.foo("2---实例方法") 

a.play("3---静态方法")

#a.static_foo("3---静态方法")

A.play("4---类方法")


          
#原因： person.xy=test 这个是错误的，原因是不可将静态方法添加到对象上面， 静态方法属于类，应该添加到类上面。 Person.xy=test，这样Person类的所有对象都会自动拥有xy属性
#
#作者：yeathMe
#链接：https://www.jianshu.com/p/2896ba409e70
#来源：简书
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。  

#@staticmethod
#def test():
#    print "--------test_----"
#class Person(object):
#    def __init___(self,newName, newAge):
#        self.name=newName
#        self.age=newAge
#        
#
#
#person=Person()
#person.xy=test
#person.xy()            