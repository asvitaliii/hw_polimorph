from fractions import Fraction


class NewFraction(Fraction):
    def __str__(self):
        return f'{self._numerator}/{self._denominator}'

    def gcd(self):
        print("new Evklid")
        mx = max(self.__get_num(), self.__get_den())
        mn = min(self.__get_num(), self.__get_den())
        r = None
        while r != 0:
            r = mx % mn
            mx = mn
            mn = r
        return NewFraction(int(self.__get_num() / mx), int(self.__get_den() / mx))

    def __get_num(self):
        return self._numerator

    def __get_den(self):
        return self._denominator

    def __add__(self, other):
        print('new add')
        return NewFraction(self.__get_num() * other.__get_den()+self.__get_den() * other.__get_num(),
                           self.__get_den() * other.__get_den()).gcd()

    def __sub__(self, other):
        print('new sub')
        return NewFraction(self.__get_num() * other.__get_den() - self.__get_den() * other.__get_num(),
                           self.__get_den() * other.__get_den()).gcd()

    def __mul__(self, other):
        print('new mul')
        return NewFraction(self.__get_num() * other.__get_num(), self.__get_den() * other.__get_den()).gcd()

    def __truediv__(self, other):
        print('new div')
        return NewFraction(self.__get_num() * other.__get_den(), self.__get_den() * other.__get_num()).gcd()
