"""wcount.py: count words from an Internet file.

__author__ = "Jiangyufei"
__pkuid__  = "1800011734"
__email__  = "1800011734@pku.edu.cn"
"""

import sys
from urllib.request import urlopen
import urllib.error


'''Function "wcount" is to analyse the given lines and print the top-n words and their frequency.'''


def wcount(lines, topn=10):
    lst = lines.split()  # Turn the lines into a list including all the words.
    wordlist = []
    for word in lst:
        newword = ''
        for i in word:
            if ',.!?/()[]\/*"_:;#@$%&'.find(i) == -1 and i.isdigit() is False:  # Remove all the punctuations and numbers.
                newword += i
        wordlist.append(newword)

    wordlist.remove('')  # Remove all the strings that have nothing inside.

    result = {}
    for word in wordlist:
        if len(word) > 2:
            if word[-2] == "'":  # If word[-2] is "'", the word is possessive case of noun, which need to remove the "'s" in the end.
                word = word[:len(word)-2]
        if word not in result:
            result[word] = 0
        result[word] += 1
    sortedresult = sorted(result, key=lambda x: result[x], reverse=True)  # Sort the keys, according to values.
    if topn > len(sortedresult):
        topn = len(sortedresult)
    for word in sortedresult[:topn]:
        print(word.ljust(10), str(result[word]).rjust(5))  # Adjust the alignment using ljust and rjust.


if __name__ == '__main__':

    if len(sys.argv) == 1:  # If there is no input, print out the instruction.
        print('  Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    else:
        try:
            doc = urlopen(sys.argv[1])
            docstr = doc.read().decode().lower()
            doc.close()
        except urllib.error.HTTPError:  # If url wrong, print out "Wrong URL".
            print('Wrong URL')
        except urllib.error.URLError:  # If there is not internet connection, print out "Broken net".
            print('Broken net')
        else:                          # If there is no error, operate routine normally.
            if sys.argv[-1].isdigit():  # If input number after URL, choose the first number as topn.
                topn = int(sys.argv[2])
                wcount(docstr, topn)
            else:                      # If there is no number input, simply call "wcount".
                wcount(docstr)
