# threading 里面有一个类叫 Thread
import threading


class Foo(object):
    # function object Oriented,即面向对象函数
    """
我们提供了一个类：
public class Foo {
  public void one() { print("one"); }
  public void two() { print("two"); }
  public void three() { print("three"); }
}
三个不同的线程将会共用一个 Foo 实例。
线程 A 将会调用 one() 方法
线程 B 将会调用 two() 方法
线程 C 将会调用 three() 方法
请设计修改程序，以确保 two() 方法在 one() 方法之后被执行，three() 方法在 two() 方法之后被执行。
示例 1:
输入: [1,2,3]
输出: "onetwothree"
解释:
有三个线程会被异步启动。
输入 [1,2,3] 表示线程 A 将会调用 one() 方法，线程 B 将会调用 two() 方法，线程 C 将会调用 three() 方法。
正确的输出是 "onetwothree"。
示例 2:
输入: [1,3,2]
输出: "onetwothree"
解释:
输入 [1,3,2] 表示线程 A 将会调用 one() 方法，线程 B 将会调用 three() 方法，线程 C 将会调用 two() 方法。
正确的输出是 "onetwothree"。
尽管输入中的数字似乎暗示了顺序，但是我们并不保证线程在操作系统中的调度顺序。
你看到的输入格式主要是为了确保测试的全面性。
链接：https://leetcode-cn.com/problems/print-in-order
    """
    def one(self):
        print("one", end='')

    def two(self):
        print("two", end='')

    def three(self):
        print("three")

    def run(self):
        self.thread = [None] * 3
        func = [(self.first, self.one), (self.second, self.two), (self.third, self.three)]
        for i in range(3):
            self.thread[i] = threading.Thread(target=func[i][0], args=(func[i][1],))
            self.thread[i].start()

    # With语句的基本语法格式:
    # with expression[as target]:
    # with_body

    # expression：是一个需要执行的表达式；
    # target：是一个变量或者元组，存储的是 expression 表达式执行返回的结果，可选参数。
    # 紧跟 with 后面的语句会被求值，返回对象的 __enter__() 方法被调用，
    # 这个方法的返回值将被赋值给 as 关键字后面的变量，当 with 后面的代码块全部被执行完之后，
    # 将调用前面返回对象的 __exit__() 方法。
    #  with 语句最关键的地方在于被求值对象必须有 __enter__() 和 __exit__() 这两个方法，
    # 那我们就可以通过自己实现这两方法来自定义 with 语句处理异常。
    # lock 对象的 enter 方法返回的是一个布尔值，表示如果加锁成功就返回 True

    def __init__(self):
        self.lock2 = threading.Lock()
        self.lock3 = threading.Lock()
        self.lock2.acquire()
        self.lock3.acquire()

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        printFirst()
        self.lock2.release()

    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        with self.lock2:
            printSecond()
            self.lock3.release()

    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        with self.lock3:
            printThird()


def main():
    nums = [2, 3, 1]
    test = Foo()
    test.run()


if __name__ == '__main__':
    main()
