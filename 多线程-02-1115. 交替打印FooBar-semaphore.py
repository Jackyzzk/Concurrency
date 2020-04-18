import threading


class FooBar(object):
    """
我们提供一个类：
class FooBar {
  public void foo() {
    for (int i = 0; i < n; i++) {
      print("foo");
    }
  }

  public void bar() {
    for (int i = 0; i < n; i++) {
      print("bar");
    }
  }
}
两个不同的线程将会共用一个 FooBar 实例。其中一个线程将会调用 foo() 方法，另一个线程将会调用 bar() 方法。
请设计修改程序，以确保 "foobar" 被输出 n 次。
示例 1:
输入: n = 1
输出: "foobar"
解释: 这里有两个线程被异步启动。其中一个调用 foo() 方法, 另一个调用 bar() 方法，"foobar" 将被输出一次。
示例 2:
输入: n = 2
输出: "foobarfoobar"
解释: "foobar" 将被输出两次。
链接：https://leetcode-cn.com/problems/print-foobar-alternately
    """
    def print_f(self):
        print('foo', end='')

    def print_b(self):
        print('bar', end='')

    def run(self):
        t1 = threading.Thread(target=self.foo, args=(self.print_f, ))
        t2 = threading.Thread(target=self.bar, args=(self.print_b, ))
        t1.start()
        t2.start()

    # Semaphore(value=1)
    # Semaphore对象内部管理一个计数器，该计数器由每个acquire()调用递减，并由每个release()调用递增。
    # 计数器永远不会低于零，当acquire()发现计数器为零时，线程阻塞，等待其他线程调用release()。
    # Semaphore对象支持上下文管理协议。

    def __init__(self, n):
        self.n = n
        self.sem1 = threading.Semaphore()
        self.sem2 = threading.Semaphore(0)
        # self.sem2.acquire() 这一句可以整合到信号量里面

    def foo(self, printFoo):
        """
        :type printFoo: method
        :rtype: void
        """
        for i in range(self.n):
            self.sem1.acquire()
            printFoo()
            self.sem2.release()

    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        for i in range(self.n):
            self.sem2.acquire()
            printBar()
            self.sem1.release()


def main():
    n = 1
    test = FooBar(n)
    test.run()


if __name__ == '__main__':
    main()
