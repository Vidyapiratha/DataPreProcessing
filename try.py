import csv
from googletrans import Translator
from json import JSONDecodeError
import json
#import translate
d=[]
wlist=[]
word=[]
# i=1
with open('s.txt', encoding='utf-8') as csvfile:

    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        # print(row)
        #print(row[0])
        new = row[1].replace('<NEWLINE>','')
        new = new.replace(' .,',',')
        new = new.replace(' .', '.')
        new = new.replace(' ,', ',')
        new = new.replace('  ', ' ')
        new = new.replace(' ?', '?')
        new = new.replace('\' ', '\'')
        new = new.replace("&quot;", "")
        new = new.replace(":", "")
        d.append(new)
        # print(new)
        # print("\n")
        #print(row[0],row[1],row[2],)

""""#translate.google('Hello,World!')
translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])
print(translator.detect(row[1]))"""


translator = Translator()
# output = translator.detect('ஆனந்த் ஷங்கரின் எழுத்து')
# print("Output"+str(output))
# translate = translator.translate('ஆனந்த் ஷங்கரின் எழுத்து', dest='en')
# print(translate)
i=0
count = 1
for elem in d:
    # print("Before Split")
    # print(elem)
    # print("\n")

    # print("After Split")
    elem= elem.split(".")

    # wlist.append(elem)
    # print(elem)
    # print("\n")
    file1 = open("TamilLines.txt", "a", encoding="utf-8")
    file2 = open("EngTamil.txt", "a", encoding="utf-8")
    file3 = open("EngTamilOnly.txt", "a", encoding="utf-8")
    try:
        for n in elem:
            if n=="":
                continue
            print(n)
            wlist.append(n)
            translated = translator.translate(n, dest='en')
            print(translated.text)
            print("\n")
            # file1.write(str(n))
            # file1.write("\n")
            # file1.flush()
            file2.write(str(count))
            file2.write("\t")
            file2.write(translated.text)
            file2.write("\t")
            file2.write(str(i))
            file2.write("\t")
            file2.write(str(i))
            file2.write("\n")
            file2.flush()
            count = count+1
            i = i+1
            if i ==3:
                i = 0

            file3.write(translated.text)
            file3.write("\n")
            file3.flush()
            # for word in n:
                # x=0
                # print(str(word)+"-" + str(x))
                # x=x+1
                # word = word.split("\t")
                # print(word)
    except JSONDecodeError:
        continue

    # try:
    #     for s in elem:
    #         print("Output")
    #         output = translator.detect(s)
    #         print(output)
    #     print("\n")
    # except JSONDecodeError:
    #     print()
    file1.close()
    file2.close()
    file3.close()

# print(wlist[2])
# translate = translator.translate(wlist[2], dest='en')
# print(translate.text)

print("Length"+str(len(wlist)))
for w in wlist:
    w = w.replace(' ', ',')
    w= w.split(",")
    for s1 in w:
        if s1=="" or s1==":" or s1=="\"":
            continue
        # print(s1)
        # print(type(s1))
        word.append(s1)
    # word = word.append(w)
print(len(word))

# output = translator.detect('ஆனந்த் ஷங்கரின் எழுத்து')
# print(output)
# print(translator.detect(new))
# print(wlist[500])
# print(translator.detect(wlist[500]))
