class Check_key():
    def __init__(self, key):
        self.input_key = key

    def Check_format(self, input_key):
        sections = [input_key[i:i + 4] for i in range(0, len(input_key), 4)]
        if len(sections)!= 3:
            return False
        for section in sections:
            if len(section)!= 4:
                return False
        return True

    def check_key(self, input_key):
        part1, part2, part3 = input_key[:4], input_key[4:8], input_key[8:]
        decimal1, decimal2, decimal3 = int(part1, 16), int(part2, 16), int(part3, 16)
        print(decimal1)
        print(decimal2)
        print(decimal3)
        self.result = int(decimal1 // 7 - decimal3 - decimal3 * decimal1 + decimal1 // decimal2 * 1111)
        print(self.result)
        self.str_result = str(self.result)

        if self.str_result[1] == "6" and self.str_result[4] == "8" and self.str_result[7] == "7":
            print("true")
            return True

key = ("274F1E5E1A0A") #274F1E5E1A0A
Activate = Check_key(key)

if Activate.Check_format(key):
    if Activate.check_key(key):
        print("Активация успешна")
else:
    print("Ключ не прошел проверку.")
