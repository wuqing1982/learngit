# -*- coding: utf-8 -*-
# 
#   author: starhqking  
# 
# 一个关于snake的类演示代码

class Snake():#Python中的类名约定以大写字母开头

    ###关于类的一个简单例子###

    #属性
    color = 'red'
    weight = 100
    legs = 6
    shell = False
    mouth = '小嘴'



    #方法
    def climb( self ):
        print("我正在很努力的向前爬")
    
    def run( self ):
        print("我正在飞快的向前跑")
     
    def bite( self ):
        print("咬死你咬死你")
    
    def eat( self ):
        print("有的吃，真满足")
     
    def sleep( self ):
        print("困了，睡觉了，晚安，zzzz")
