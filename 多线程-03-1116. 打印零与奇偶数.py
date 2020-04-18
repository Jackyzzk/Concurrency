from threading import Semaphore
from threading import Thread


class ZeroEvenOdd(object):
    """
假设有这么一个类：
class ZeroEvenOdd {
  public ZeroEvenOdd(int n) { ... }      // 构造函数
  public void zero(printNumber) { ... }  // 仅打印出 0
  public void even(printNumber) { ... }  // 仅打印出 偶数
  public void odd(printNumber) { ... }   // 仅打印出 奇数
}
相同的一个 ZeroEvenOdd 类实例将会传递给三个不同的线程：
线程 A 将调用 zero()，它只输出 0 。
线程 B 将调用 even()，它只输出偶数。
线程 C 将调用 odd()，它只输出奇数。
每个线程都有一个 printNumber 方法来输出一个整数。
请修改给出的代码以输出整数序列 010203040506... ，其中序列的长度必须为 2n。
输入：n = 2
输出："0102"
说明：三条线程异步执行，其中一个调用 zero()，另一个线程调用 even()，
最后一个线程调用odd()。正确的输出为 "0102"。
输入：n = 5
输出："0102030405"
链接：https://leetcode-cn.com/problems/print-zero-even-odd
    """
    def print_num(self, x):
        print(x, end='')

    def run(self):
        t0 = Thread(target=self.zero, args=(self.print_num, ))
        t1 = Thread(target=self.odd, args=(self.print_num, ))
        t2 = Thread(target=self.even, args=(self.print_num, ))
        t0.start()
        t1.start()
        t2.start()

    def __init__(self, n):
        self.n = n
        self.sem0 = Semaphore()
        self.sem1 = Semaphore(0)
        self.sem2 = Semaphore(0)

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(self.n):
            self.sem0.acquire()
            printNumber(0)
            if i & 1:
                self.sem2.release()
            else:
                self.sem1.release()

    def even(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(self.n >> 1):
            self.sem2.acquire()
            printNumber(2 * i + 2)
            self.sem0.release()

    def odd(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range((self.n + 1) >> 1):
            self.sem1.acquire()
            printNumber(2 * i + 1)
            self.sem0.release()


def main():
    n = 11
    test = ZeroEvenOdd(n)
    test.run()


if __name__ == '__main__':
    main()
