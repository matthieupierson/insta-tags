import random
import os
import sys




k = 0
files = []

for element in os.listdir('db/'):
    if element.endswith('.txt'):
        files.append(element[:len(element)-4])
    
print(files)

f1 = open('config.txt',"w")
f1.close()

f1 = open('config.txt',"a")
for i in range(len(files)) :
    f1.write(files[i])
    f1.write(" ")
    print ("How many tags do you want from '", files[i],"' database?")
    number = input()

    f=open('db/' + files[i] +'.txt',"r")
    input_hashtags=f.read()
    f.close()
    f=open('db/' + files[i] +'.txt',"r")
    for letter in range(len(input_hashtags)):
        if input_hashtags[letter] == " ":
            input_hashtags=f.read().split(" ")
            break
        elif input_hashtags[letter] == "\n":
            input_hashtags=f.read().split("\n")
            break
    f.close()

    while int(number)>len(input_hashtags) :
        print ("You have",len(input_hashtags),"tags in this database. Please change your desired amount of tags :) ")
        number = input()

    f1.write(number)
    f1.write("\n")

f1.close()