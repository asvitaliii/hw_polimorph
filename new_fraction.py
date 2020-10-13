class NewFraction(object):
    def __init__(self, string: str):
        if '/' in string:
            lst = string.split('/')
            self.__numerator = int(lst[0])
            self.__denominator = int(lst[1])
        elif '.' in string:
            lst = string.split('.')
            self.__numerator = int(lst[0]) * 10 ** len(lst[1]) + int(lst[1])
            self.__denominator = 10 ** len(lst[1])
        elif ',' in string:
            lst = string.split(',')
            self.__numerator = int(lst[0]) * 10 ** len(lst[1]) + int(lst[1])
            self.__denominator = 10 ** len(lst[1])
        if self.__denominator < 0:
            self.__numerator = self.__numerator * -1
            self.__denominator = self.__denominator * -1

    def __str__(self):
        return f'{self.__numerator}/{self.__denominator}'

    def gcd(self):
        print("new Evklid")
        mx = max(self.__get_num(), self.__get_den())
        mn = min(self.__get_num(), self.__get_den())
        r = None
        while r != 0:
            r = mx % mn
            mx = mn
            mn = r
        return NewFraction(str(int(self.__get_num() / mx)) + '/' + str(int(self.__get_den() / mx)))

    def __get_num(self) -> int:
        return self.__numerator

    def __get_den(self) -> int:
        return self.__denominator

    def __add__(self, other):
        print('new add')
        return NewFraction(str(self.__get_num() * other.__get_den()+self.__get_den() * other.__get_num()) + '/' +
                           str(self.__get_den() * other.__get_den())).gcd()

    def __sub__(self, other):
        print('new sub')
        return NewFraction(str(self.__get_num() * other.__get_den() - self.__get_den() * other.__get_num()) + '/' +
                           str(self.__get_den() * other.__get_den())).gcd()

    def __mul__(self, other):
        print('new mul')
        return NewFraction(str(self.__get_num() * other.__get_num()) + '/' + str(self.__get_den() * other.__get_den())).gcd()

    def __truediv__(self, other):
        print('new div')
        return NewFraction(str(self.__get_num() * other.__get_den()) + '/' + str(self.__get_den() * other.__get_num())).gcd()
