class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dig_order = []
        letter_order = []
        for x in logs:
            if (x[-1].isnumeric()):
                dig_order.append(x)
            elif (x[-1].isalpha()):
                letter_order.append(x)
        print(dig_order)
        print(letter_order)
        letter_order.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letter_order+dig_order

        