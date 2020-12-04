#!/usr/bin/env python


f = open("zad7_remove_words.txt", "r+", encoding='utf-8')
text = f.read()
my_list = ["and","Max","large","was","Trojans"]

for i in range(0,len(my_list)):
    s = 0
    while((text.find(my_list[i], s))!= -1):
        x = text.find(my_list[i], s)
        if(x != 0):
            if((text[x-1] != " " and text[x-1] != "\n" and text[x-1] != "\t")):
                s = x + len(my_list[i])
                continue
        if(x+ len(my_list[i]) != len(text)):
            if((text[x+len(my_list[i])] != " " and text[x+len(my_list[i])] != "\n" and text[x+len(my_list[i])] != "\t")):
                s = x + len(my_list[i])
                continue
        text = text[:x] + text[x+len(my_list[i]):]
        s = x
        continue
        
print(text)
f.close()
f = open("zad7_remove_words.txt", "w+", encoding='utf-8')
f.write(text)
f.close()