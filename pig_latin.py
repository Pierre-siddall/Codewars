import string
def pig_it(text):
    wordlist = text.split()
    for i in range(len(wordlist)):
        if wordlist[i] in string.punctuation:
            pass
        else:
            tmp = wordlist[i][0]
            wordlist[i]=wordlist[i][1:]+tmp+'ay'
    return' '.join(wordlist)


if __name__ == '__main__':
    pig_it('O tempora o mores !')
