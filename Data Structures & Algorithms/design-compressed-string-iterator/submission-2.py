class StringIterator:

    def __init__(self, compressedString: str):
        self.res = []
        self.pos = 0
        
        i = 0
        while i < len(compressedString):
            num = 0
            char = compressedString[i]
            i += 1

            while i < len(compressedString) and compressedString[i].isdigit():
                num = num * 10 + int(compressedString[i])
                i += 1
            self.res.append([char, num])

    def next(self) -> str:
        if not self.hasNext():
            return ' '
        # char, count = self.res[self.pos]
        # if count == 0:
        #     self.pos += 1
        #     char2, count2 = self.res[self.pos]
        #     count2 -= 1
        #     return char2
        # else:
        #     count -= 1
        #     return char
        char, count = self.res[self.pos]
        
        if count == 0:
            self.pos += 1
            char, count = self.res[self.pos]
        
        self.res[self.pos][1] -= 1 
        return char

    def hasNext(self) -> bool:
        return self.pos < len(self.res)
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# N12
# num = 0
# 10 + 2 = 12

# L3
# num = 0
# num = 10 * 0 + 3 = 3
