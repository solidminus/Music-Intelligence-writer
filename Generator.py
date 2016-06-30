import Syntax
import random


class Gen:
    def __init__(self, namfil, loop_freq, global_diap, frequency, loop_diap, on_the_fly):
        self.namfil = namfil  # имя файла для кода
        self.loop_freq = loop_freq  # частота появления циклов
        self.global_diap = global_diap  # глобальный диапазон частот ( для генерации звуков )
        self.frequency = frequency  # частота появления звуков
        self.loop_diap = loop_diap  # максимальное количество итераций
        self.fname = open(self.namfil, "w")
        self.frames = []
        self.tempory = []  # временное хранилище байт для вложенных циклов
        self.n = 0
        print("code=\"\"\"", file=self.fname)

    def uninit(self):
        print("\"\"\"", file=self.fname)
        self.fname.close()

    def generator(self, len):
        random.seed()
        for i in range(0, len):
            rnd = random.randint(0, self.loop_freq)
            print(rnd, "", sep=" ", end="")
            if rnd <= 2:
                print("rnd is ", rnd, " going to ", Syntax.circ[rnd], sep="")
                Syntax.circ[rnd](Syntax.struc, self.fname, [0, random.randint(2, self.loop_diap)])

            rnd = random.randint(0, self.frequency)
            if rnd == 1:
                print("Generating frame ", sep="", end="")
                self.n += 1
                Syntax.rnd(Syntax.struc, self.fname, self.global_diap, self.n)
                Syntax.ReplFrame(Syntax.struc, self.n, self.global_diap)
            elif self.frequency > 1:

                Syntax.go_on(self.fname, Syntax.struc.spc())
                print("yield \"0\"", file=self.fname)

        #while Syntax.struc.spc() > 4:
         #   print(">", end="")
          #  Syntax.loopend(Syntax.struc, self.fname, self.global_diap)

    def get_frames(self):
        return self.frames
