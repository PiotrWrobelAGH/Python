#!/usr/bin/env python
import os
def get_text():
    print("Wprowadz dane, dane beda w formacie: Zadanie, opis, data")
    i = 0
    my_list = []
    my_list.append([])
    while True:
        temp = input(f"Rekord {i}: Podaj tytul zadania. Kliknij enter bez tekstu aby zakonczyc\n")
        if(temp == ""):
            break
        my_list[i].append(temp)
        temp = input(f"Rekord {i}: Podaj opis zadania\n")
        my_list[i].append(temp)
        temp = input(f"Rekord {i}: Podaj termin zadania do wykonania\n")
        my_list[i].append(temp)
        i = i+1
        my_list.append([])
    my_string = ''
    for i in range(len(my_list)-1):
        my_string = my_string + my_list[i][0] + ',' + my_list[i][1] + ',' + my_list[i][2]
        if(i != len(my_list)-2):
            my_string = my_string + "\n"
    return my_string
def main():
    fileslist = os.listdir(os.getcwd())
    if("zad18_csv.txt" not in fileslist):
        new_text = get_text()
        f = open("zad18_csv.txt", "w+", encoding='utf-8')
        f.write(new_text)
        f.close()
        return
    f = open("zad18_csv.txt", "r+", encoding='utf-8')
    text = f.read()
    f.close()
    list_of_lines = text.split("\n")
    print(text)
    while(True):
        print(f"Ktory rekord usunac?[0-{len(list_of_lines)-1}]. Kliknij enter bez tekstu aby pominac")
        num = input()
        if (num != ""):
            num = int(num)
            list_of_lines.pop(num)
            test = "\n".join(list_of_lines)
            print(test)
            f = open("zad18_csv.txt", "w+", encoding='utf-8')
            f.write(test)
            f.close()
            if(len(list_of_lines) == 0):
                break
        else:
            break
    f = open("zad18_csv.txt", "r+", encoding='utf-8')
    text = f.read()
    f.close()
    new_text = get_text()
    if(text == ""):
        new_text = text + new_text
    else:
        if(new_text != ""):
            new_text = text + "\n" + new_text
        else:
            new_text = text
    f = open("zad18_csv.txt", "w+", encoding='utf-8')
    f.write(new_text)
    f.close()
if __name__ == "__main__":
    main()