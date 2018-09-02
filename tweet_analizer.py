from tokenizer import Tokenizer
import json

not_decoded_file = open('formatted_text.txt', 'rb').read()
text = not_decoded_file.decode('utf-8')

t = Tokenizer()
words = t.tokenize(text)


def make_dictionary(words):
    tmp = '@'
    dictionary = {}
    for i in words:
        word = i.surface
        if word == '' or word == '¥n' or word == '¥r¥n': continue
        tmp.append(word)
        if len(tmp) < 3: continue
        if len(tmp) > 3: tmp = tmp[1:]
        set_word3(dictionary, tmp)
        if word == '.':
            tmp = ['@']
            continue
    return dictionary


def set_word3(dic, s3):
    w1, w2, w3 = s3
    if w1 not in dic: dic[w1] = {}
    if w2 not in dic[w1]: dic[w1][w2] = {}
    if w3 not in dic[w1][w2]: dic[w1][w2][w3] = 0
    dic[w1][w2][w3] += 1


dictionary = make_dictionary(words)
json.dump(dictionary, open("markov-blog.json", "w", "utf-8"))
