class Anagram:
    def __init__(self, text):
        self.dict = {}
        text = text.replace(" ", "").lower()
        for char in text:
            if char not in self.dict:
                self.dict[char] = 0

            self.dict[char] += 1

    def __eq__(self, other):
        return self.dict == other.dict

    def __str__(self):
        keys = sorted(list(self.dict.keys()))
        return str({key: self.dict[key] for key in keys})


if __name__ == "__main__":
    a = Anagram("naked Norwegian")
    b = Anagram("wandering oaken")

    print(a)
    print(b)
    print(a == b)

    c = Anagram("dry banana hippy hat")
    d = Anagram("Happy Birthday Anna")

    print(c)
    print(d)
    print(c == d)
