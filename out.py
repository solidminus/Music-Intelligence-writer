code="""
def temp():
    yield "0"
    yield "1(400,800)"
    yield "0"
    yield "0"
    yield "0"
    yield "0"
    yield "2(400,800)"
    yield "0"
    yield "0"
    yield "0"
    yield "0"
    for _ in range(10):
        yield "0"
        yield "0"
        yield "0"
        yield "0"
        for _ in range(4):
            yield "3(400,800)"
            yield "0"
            yield "0"
            yield "0"
        yield "4(400,800)"
        yield "5(400,800)"
        yield "6(400,800)"
        for _ in range(3):
            yield "0"
            yield "0"
            yield "0"
            yield "0"
            yield "0"
            for _ in range(2):
                yield "0"
                yield "7(400,800)"
                yield "0"
                yield "0"
                yield "8(400,800)"
            yield "0"
            for _ in range(4):
                yield "0"
                yield "9(400,800)"
            yield "10(400,800)"
            yield "0"
        yield "0"
        for _ in range(5):
            yield "0"
            for _ in range(4):
                yield "0"
                yield "0"
                yield "0"
                for _ in range(3):
                    yield "0"
                    yield "0"
                    yield "11(400,800)"
                yield "0"
                for _ in range(3):
                    yield "12(400,800)"
                    for _ in range(10):
                        yield "13(400,800)"
                        yield "0"
                        for _ in range(4):
                            yield "0"
                            yield "0"
                            yield "0"
                            yield "14(400,800)"
                            yield "0"
                        yield "0"
                        yield "0"
                        for _ in range(6):
                            yield "0"
                            yield "0"
                            for _ in range(5):
                                yield "15(400,800)"
                            yield "0"
                            yield "0"
                            yield "0"
                            yield "0"
                        yield "0"
                        for _ in range(9):
                            yield "0"
                            for _ in range(7):
                                yield "0"
                                yield "16(400,800)"
                                yield "0"
                                yield "0"
                            yield "17(400,800)"
                        yield "18(400,800)"
                        yield "0"
                    yield "0"
                yield "19(400,800)"
                for _ in range(7):
                    yield "0"
                    yield "20(400,800)"
                yield "0"
                yield "21(400,800)"
                yield "22(400,800)"
                yield "0"
            yield "23(400,800)"
            yield "24(400,800)"
            for _ in range(10):
                yield "0"
                yield "0"
                for _ in range(10):
                    yield "0"
                    yield "0"
                    yield "0"
                    for _ in range(6):
                        yield "0"
                        yield "0"
                        yield "0"
                        yield "25(400,800)"
                        yield "26(400,800)"
                        for _ in range(9):
                            yield "0"
                            yield "0"
                            yield "27(400,800)"
                            yield "0"
                            yield "0"
                        yield "0"
                    yield "0"
                    yield "28(400,800)"
"""
