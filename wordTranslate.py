def main():
    while (True):
        print("Please enter 26 character for your new alphabet")
        print("The first character replaces 'a' and the last character replaces 'z'")
        userin = input()
        if (len(userin) != 26):
            print("Not 26 character")
        else:
            break
    alpha = createalphabet(userin)
    while (True):
        print("\nEnter a word to translate using the new encoding (Enter to exit)")
        print("Old Word:", end=" ")
        word = input()
        if (word == ""):
            break
        newword = translate(alpha, word)
        print("New Word: " + newword, end="")
    return 0


def createalphabet(charencoding):
    alphabet = {}
    for i in range(ord('a'), ord('z')):
        alphabet[chr(i)] = charencoding[i-ord('a')]
    return alphabet


def translate(alphabet, word):
    newword = ""
    for i in range(0, len(word)):
        newword += alphabet[word[i]]
    return newword


if __name__ == "__main__":
    main()
