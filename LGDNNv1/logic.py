import numpy as np

class bool():

    """ Perform Logic-Gate Computation on an array of boolean values"""
    def AND(self, arr):
        out: bool = False

        length = np.size(arr)

        for index in range(0, length-1):
            a = arr[index]
            b = arr[index+1]
            arr[index+1] = np.logical_and(a, b)


        out = arr[length-1]

        return out


    def NAND(self, arr):
        out: bool = False

        length = np.size(arr)

        for index in range(0, length-1):
            a = arr[index]
            b = arr[index+1]
            arr[index+1] = np.logical_not(np.logical_and(a, b))


        out = arr[length-1]

        return out


    def OR(self, arr):
        out: bool = False

        length = np.size(arr)

        for index in range(0, length-1):
            a = arr[index]
            b = arr[index+1]
            arr[index+1] = np.logical_or(a, b)


        out = arr[length-1]

        return out


    def XOR(self, arr):
        out: bool = False

        length = np.size(arr)

        for index in range(0, length-1):
            a = arr[index]
            b = arr[index+1]
            arr[index+1] = np.logical_xor(a, b)


        out = arr[length-1]

        return out


    def NOR(self, arr):
        out: bool = False

        length = np.size(arr)

        for index in range(0, length-1):
            a = arr[index]
            b = arr[index+1]
            arr[index+1] = np.logical_not(np.logical_or(a, b))


        out = arr[length-1]

        return out


    def XNOR(self, arr):
        out: bool = False

        length = np.size(arr)

        for index in range(0, length-1):
            a = arr[index]
            b = arr[index+1]
            arr[index+1] = np.logical_not(np.logical_xor(a, b))


        out = arr[length-1]

        return out

class integer:

    """ Perform Logic-Gate Computation on Boolean values represented as Integers. No array support"""
    def AND(self, a: int, b: int):
        out: int = 0

        if a and b:
            out = 1

        return out


    def OR(self, a: int, b: int):
        out: int = 0

        if a or b:
            out = 1

        return out


    def NOR(self, a: int, b: int):
        out: int = 0

        if a == 0 and b == 0:
            out = 1

        return out


    def XNOR(self, a: int, b: int):
        out: int = 0

        if a == b:
            out = 1

        return out


    def XOR(self, a: int, b: int):
        out: int = 1

        if a == b:
            out = 0

        return out


    def NAND(self, a: int, b: int):
        out: int = 1

        if a and b:
            out = 0

        return out