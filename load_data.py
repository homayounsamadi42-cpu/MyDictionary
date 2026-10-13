import csv
import json
csv.field_size_limit(1000000)
def english_english_persian_json(filename):
    word = []
    meaning = []
    f = open(filename,"r",encoding="utf-8")
    data = json.loads(f.read())
    for key in data.keys():
        word.append(key)
        meaning.append(data[key])
    f.close()
    return word,meaning

def english_english_csv(filename):
    word = []
    meaning = []
    f = open(filename)
    data = csv.reader(f)
    for u in list(data)[:10]:
        word.append(u[0])
        meaning.append(u[2])
    f.close()
    return word,meaning

def persian_persian_txt(filename):
    word = []
    meaning = []
    f = open(filename,"r",encoding="utf-8")
    for u in f.readlines()[:10]:
        word.append(u.rstrip("\n").split(":")[0])
        meaning.append(u.rstrip("\n").split(":")[1])
    return word,meaning

def load(letter,lan):
    words = []
    meaning = []
    if lan == "eng":
        f = open(f"English-English/{letter}.txt","r",encoding="utf-8")
    else:
        f = open(f"English-Persian/{letter}.txt","r",encoding="utf-8")
    for row in f.readlines():
        words.append(row.rstrip("\n").split(":")[0])
        meaning.append(row.rstrip('\n').split(":")[1])
    f.close()
    return words, meaning
