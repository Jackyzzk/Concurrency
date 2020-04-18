from threading import Thread
from threading import Semaphore

class H2O(object):
    """
现在有两种线程，氢 oxygen 和氧 hydrogen，你的目标是组织这两种线程来产生水分子。
存在一个屏障（barrier）使得每个线程必须等候直到一个完整水分子能够被产生出来。
氢和氧线程会被分别给予 releaseHydrogen 和 releaseOxygen 方法来允许它们突破屏障。
这些线程应该三三成组突破屏障并能立即组合产生一个水分子。
你必须保证产生一个水分子所需线程的结合必须发生在下一个水分子产生之前。
换句话说:
如果一个氧线程到达屏障时没有氢线程到达，它必须等候直到两个氢线程到达。
如果一个氢线程到达屏障时没有其它线程到达，它必须等候直到一个氧线程和另一个氢线程到达。
书写满足这些限制条件的氢、氧线程同步代码。
示例 1:
输入: "HOH"
输出: "HHO"
解释: "HOH" 和 "OHH" 依然都是有效解。
示例 2:
输入: "OOHHHH"
输出: "HHOHHO"
解释: "HOHHHO", "OHHHHO", "HHOHOH", "HOHHOH", "OHHHOH", "HHOOHH", "HOHOHH" 和 "OHHOHH" 依然都是有效解。
限制条件:
输入字符串的总长将会是 3n, 1 ≤ n ≤ 50；
输入字符串中的 “H” 总数将会是 2n；
输入字符串中的 “O” 总数将会是 n。
链接：https://leetcode-cn.com/problems/building-h2o
    """
    @staticmethod
    def print_h():
        print('h', end='')

    @staticmethod
    def print_o():
        print('o', end='')

    def run(self, s):
        n = 0
        for x in s:
            if x == 'O':
                n += 1

        def run1():
            for i in range(2 * n):
                self.hydrogen(self.print_h)

        def run2():
            for i in range(n):
                self.oxygen(self.print_o)

        Thread(target=run1).start()
        Thread(target=run2).start()

    # Barrier(parties, action=None, timeout=None)
    # 每个线程通过调用wait()尝试通过障碍，并阻塞，直到阻塞的数量达到parties时，阻塞的线程被同时全部释放。
    # action是一个可调用对象，当线程被释放时，其中一个线程会首先调用action，之后再跑自己的代码。
    # timeout时默认的超时时间。
    #
    # 作者：雷子_
    # 链接：https://www.jianshu.com/p/b4ee3c32c06d
    # 来源：简书
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    def __init__(self):
        self.sem1 = Semaphore(2)
        self.sem2 = Semaphore(0)
        self.status = 0

    def hydrogen(self, releaseHydrogen):
        """
        :type releaseHydrogen: method
        :rtype: void
        """
        self.sem1.acquire()
        releaseHydrogen()
        if self.status:
            self.sem2.release()
        self.status ^= 1


    def oxygen(self, releaseOxygen):
        """
        :type releaseOxygen: method
        :rtype: void
        """
        self.sem2.acquire()
        releaseOxygen()
        self.sem1.release()
        self.sem1.release()


def main():
    s = "OOHHHH"
    # s = "HOH"
    test = H2O()
    test.run(s)


if __name__ == '__main__':
    main()
