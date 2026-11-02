class Solution:
    def capitalizeTitle(self, title: str) -> str:

        words = title.split()
        result = []

        for word in words:

            new_word = ""

            for i in range(len(word)):

                ch = word[i]

                if len(word) <= 2:

                    if 'A' <= ch <= 'Z':
                        ch = chr(ord(ch) + 32)

                elif i == 0:

                    if 'a' <= ch <= 'z':
                        ch = chr(ord(ch) - 32)

                else:

                    if 'A' <= ch <= 'Z':
                        ch = chr(ord(ch) + 32)

                new_word += ch

            result.append(new_word)

        return " ".join(result)