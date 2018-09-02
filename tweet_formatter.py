from StdSuites import string
from string import ascii_letters

text = open('tweet.txt', 'r').read().split()

for line in text:
    for word in line:
        if word in ascii_letters or word in string.digits:
            if line in text:
                text.remove(line)

f = open('formatted_text.txt', 'w')
for x in text:
    f.write(str(text) + '¥n')

f.close()
