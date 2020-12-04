#!/usr/bin/env python


f = open("zad8_replace_words.txt", "r+", encoding='utf-8')
text = f.read()
my_dict = {"discovery":"super","after":"before","hold":"release","extremely":"not"}
#Brak informacji na temat czy "i" i "oraz" mają być zamieniane w "locie" czy też nie

for i, j in my_dict.items():
    s = 0
    while((text.find(i, s))!= -1):
        x = text.find(i, s)
        if(x != 0):
            if((text[x-1] != " " and text[x-1] != "\n" and text[x-1] != "\t")):
                s = x + len(i)
                continue
        if(x+ len(i) != len(text)):
            if((text[x+len(i)] != " " and text[x+len(i)] != "\n" and text[x+len(i)] != "\t")):
                s = x + len(i)
                continue
        text = text[:x] +j+ text[x+len(i):]
        s = x + len(j)
        continue
        
print(text)
f.close()
f = open("zad8_replace_words", "w+", encoding='utf-8')
f.write(text)
f.close()