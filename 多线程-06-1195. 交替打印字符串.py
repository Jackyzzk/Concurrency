from threading import Thread
from threading import Semaphore


class FizzBuzz(object):
    """
编写一个可以从 1 到 n 输出代表这个数字的字符串的程序，但是：
如果这个数字可以被 3 整除，输出 "fizz"。
如果这个数字可以被 5 整除，输出 "buzz"。
如果这个数字可以同时被 3 和 5 整除，输出 "fizzbuzz"。
例如，当 n = 15，输出： 1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz, 11, fizz, 13, 14, fizzbuzz。
假设有这么一个类：
class FizzBuzz {
  public FizzBuzz(int n) { ... }               // constructor
  public void fizz(printFizz) { ... }          // only output "fizz"
  public void buzz(printBuzz) { ... }          // only output "buzz"
  public void fizzbuzz(printFizzBuzz) { ... }  // only output "fizzbuzz"
  public void number(printNumber) { ... }      // only output the numbers
}
请你实现一个有四个线程的多线程版  FizzBuzz， 同一个 FizzBuzz 实例会被如下四个线程使用：
线程A将调用 fizz() 来判断是否能被 3 整除，如果可以，则输出 fizz。
线程B将调用 buzz() 来判断是否能被 5 整除，如果可以，则输出 buzz。
线程C将调用 fizzbuzz() 来判断是否同时能被 3 和 5 整除，如果可以，则输出 fizzbuzz。
线程D将调用 number() 来实现输出既不能被 3 整除也不能被 5 整除的数字。
链接：https://leetcode-cn.com/problems/fizz-buzz-multithreaded
    """
    @staticmethod
    def print_f():
        print('fizz', end=', ')

    @staticmethod
    def print_b():
        print('buzz', end=', ')

    @staticmethod
    def print_fb():
        print('fizzbuzz', end=', ')

    @staticmethod
    def print_i(x):
        print(x, end=', ')

    def run(self):
        Thread(target=self.fizz, args=(self.print_f, )).start()
        Thread(target=self.buzz, args=(self.print_b, )).start()
        Thread(target=self.fizzbuzz, args=(self.print_fb, )).start()
        Thread(target=self.number, args=(self.print_i, )).start()

    def __init__(self, n):
        self.n = n + 1
        self.sem3 = Semaphore(0)
        self.sem5 = Semaphore(0)
        self.sem35 = Semaphore(0)
        self.sem1 = Semaphore()

    def fizz(self, printFizz):
        """
        :type printFizz: method
        :rtype: void
        """
        for i in range(1, self.n):
            if not i % 3 and i % 5:
                self.sem3.acquire()
                printFizz()
                self.sem1.release()

    def buzz(self, printBuzz):
        """
        :type printBuzz: method
        :rtype: void
        """
        for i in range(1, self.n):
            if i % 3 and not i % 5:
                self.sem5.acquire()
                printBuzz()
                self.sem1.release()

    def fizzbuzz(self, printFizzBuzz):
        """
        :type printFizzBuzz: method
        :rtype: void
        """
        for i in range(1, self.n):
            if not (i % 3 or i % 5):
                self.sem35.acquire()
                printFizzBuzz()
                self.sem1.release()

    def number(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1, self.n):
            self.sem1.acquire()
            if i % 3 and i % 5:
                printNumber(i)
                self.sem1.release()
            elif i % 5:
                self.sem3.release()
            elif i % 3:
                self.sem5.release()
            else:
                self.sem35.release()


def main():
    n = 15
    test = FizzBuzz(n)
    test.run()


if __name__ == '__main__':
    main()

