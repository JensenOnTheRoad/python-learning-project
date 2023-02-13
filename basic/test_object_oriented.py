class Person:
    name = ''
    age = ''

    # 对象初始化方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    """
    创建对象时执行的方法，单例模式会用到
    
    __new__() 是一种负责创建类实例的静态方法，
    它无需使用 staticmethod 装饰器修饰，
    且该方法会优先 __init__() 初始化方法被调用。
    """

    # 当print输出对象时，
    # 只要定义了该方法，那么输出打印这个方法return的数据
    def __str__(self):
        print("str method is called")
        return self.name

    # 对象删除时执行的方法
    def __del__(self):
        print("object deleted.")

    def say(self):
        print("hello world")


if __name__ == '__main__':
    person = Person("zhangsan", 24)
    print(person)
    person.say()
