class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.number_slots = {} # {slot_nr: is_assigned}

        for i in range(0, maxNumbers):
            self.number_slots[i] = False

    def get(self) -> int:
        for key, val in self.number_slots.items():
            if val == False:
                self.number_slots[key] = True
                return key
        return -1

    def check(self, number: int) -> bool:
        return self.number_slots[number] == False

    def release(self, number: int) -> None:
        self.number_slots[number] = False


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)