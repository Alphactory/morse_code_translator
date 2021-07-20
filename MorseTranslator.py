class MorseTranslator:
    def __init__(self, source_file="morse.csv"):
        self.source_dict = {}
        source = open(source_file)
        for line in source.read().split("\n"):
            splitline = line.split(",")
            try:
                self.source_dict[splitline[1]] = splitline[0]
            except IndexError:
                continue

    def get_letter(self, morse):
        morse = morse.replace("-", "_")
        try:
            return self.source_dict[morse]
        except KeyError:
            return "{?}"

    def translate(self, string):
        result = ""
        for word in string.split("/"):
            for letter in word.split(" "):
                result += self.get_letter(letter)
            result += " "
        return result
