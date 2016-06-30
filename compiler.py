import Syntax
import wave
import struct
import numpy as N
import random

blen = 2200
freq = 22050

def my_code(cd):
    namespace  = {}
    exec(cd,namespace)
    return namespace["temp"]()

def compiler():
    import out
    print("Loaded out.py")
    print("Compiling...")
    lst = list(my_code(out.code))
    print("Compiled!")
    print("Linking...")

    print("Bytes len: ", len(lst), " = ", blen * len(lst))

    music = wave.open('out.wav', 'w')
    music.setparams((2, 1, freq, 0, 'NONE', 'not compressed'))

    for i in lst:
        if (i == "0"):
            packed_value = wave.struct.pack('h', 0)
            for _ in range(100):
                music.writeframes(packed_value)
            continue

        key = i[0:i.find("(")]
        frame = Syntax.struc.num[int(key)]

        duration = 0.05
        samplerate = freq  # Hz
        samples = duration * samplerate
        frequency = frame #Hz
        period = samplerate / float(frequency)  # in sample points
        omega = N.pi * 2 / period

        xaxis = N.arange(int(period), dtype=N.float) * omega
        ydata = 16384 * N.sin(xaxis)

        signal = N.resize(ydata, 400) # 2-й параметр - скорость

        ssignal = b''
        for i in range(len(signal)):
            ssignal += wave.struct.pack('h', int(signal[i]))  # transform to binary

        music.writeframes(signal)

        #packed_value = wave.struct.pack('h', frame)
        #for _ in range(blen):
        #    music.writeframes(packed_value)
    music.close()

    print("Linked to out.wav!")

