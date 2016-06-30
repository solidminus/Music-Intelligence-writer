#!/usr/bin/python

import Generator
import compiler

def Main():
    filename = str(input("Specify a filename for code output: "))
    len = int(input("Len of program: "))
    freq = int(input("Frequency: "))

    Gen = Generator.Gen(filename, 5, [400, 800], freq, 10, True)
    Gen.generator(len)
    frames = Gen.get_frames()
    Gen.uninit()
    print()
    input("end")
    print(Generator.Syntax.struc.num)
    print("Calling compiling engine")
    compiler.compiler()


Main()
input("finished")

