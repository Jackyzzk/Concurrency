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

    def __init__(self):
        self.sem2 = threading.Semaphore(0)
        self.sem3 = threading.Semaphore(0)

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        printFirst()
        self.sem2.release()

    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        self.sem2.acquire()
        printSecond()
        self.sem3.release()

    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        self.sem3.acquire()
        printThird()


def main():
    nums = [2, 3, 1]
    test = Foo()
    test.run()


if __name__ == '__main__':
    main()
