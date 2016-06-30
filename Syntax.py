#!/usr/bin/python
import random


class struct:
    def __init__(self, spaces):
        self.spaces = spaces  # уровень вложенности инструкции
        self.loop = 0
        self.name = "for _ in range("
        self.ttl = -1

    def spc(self):
        return self.spaces

    def increase(self):
        self.spaces += 4

    def addloop(self):
        self.loop += 1

    def removeloop(self):
        self.loop -= 1

    def decrease(self):
        self.spaces -= 4

    def inf(self):
        return [self.spaces, self.loop]

    num = {}  # список номера функции и ее значения.

    was = False

    def getname(self):
        self.ttl += 1
        return self.name

first = True

def go_on(fname, n):  # генерирует отступы
    if (n == 4) and first:
        print("def temp():", file=fname)
        global first
        first = False
    for i in range(n):
        print(" ", end="", file=fname)


def forloop(struc, fname, diap):
    go_on(fname, struc.spc())
    # print("for ", diap[0], "...", diap[1], sep="", file=fname)
    print(struc.getname(), diap[1], "):", sep="", file=fname)
    #go_on(fname, struc.spc())
    #print("{", file=fname)

    struc.increase()

    struc.addloop()
    struc.was = True


def loopend(struc, fname, diap):
    if (struc.inf()[0] == 4) or struc.was:
        return
    struc.decrease()
    struc.removeloop()
    #go_on(fname, struc.spc())
    #print("")
    #print("}", file=fname)


def rnd(struc, fname, diap, n):
    go_on(fname, struc.spc())
    print("yield \"", n, "(", diap[0], ",", diap[1], ")\"", sep="", file=fname)
    struc.was = False


def FRAME(struc, n, diap):
    return struc.num[n]


def ReplFrame(struc, n, diap):
    struc.num[n] = random.randint(diap[0], diap[1])


# инициализация

struc = struct(4)
circ = {0: forloop, 1: loopend, 2:loopend}
