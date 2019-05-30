import random
import os
import sys

#nom des database
#files = ['hashtags_base', 'abstract', 'graphics', 'minimalism', 'art', 'hdr']
#quantitée de chaque hashtags de chaque database


nb_hashtags = [18,3,3,2,2,2,2]
textfile=0
k=0

for element in os.listdir('db/'):
    if element.endswith('.txt'):
        textfile=textfile+1

files=[0]*textfile

for element in os.listdir('db/'):
    if element.endswith('.txt'):
        files[k]=element[:len(element)-4]
        k=k+1
    
print(files)

def randomizer (my_file, nb_hashtags):
    #stockage du texte dans un tableau input_hashtags
    f=open('db/' + my_file +'.txt',"r")
    input_hashtags=f.read()
    f.close()

    f=open('db/' + my_file +'.txt',"r")
    for letter in range(len(input_hashtags)):
        if input_hashtags[letter] == " ":
            input_hashtags=f.read().split(" ")
            break
        elif input_hashtags[letter] == "\n":
            input_hashtags=f.read().split("\n")
            break
    f.close()

    #genere un tableau de nb_hashtags élements de chiffres aléatoire
    #de 0 à la taille du tableau input_hashtags sans doublons
    rand_nb=random.sample(range(len(input_hashtags)),nb_hashtags)

    #genere un tableau output_hashtags rempli de 0 de la taille de input_hashtags
    output_hashtags = [0] * nb_hashtags
    fb=open('random_tags.txt',"a")
    for i in range(len(rand_nb)):
        output_hashtags [i] = input_hashtags[rand_nb[i]]
        fb.write(output_hashtags[i])
        fb.write(" ")
    fb.close()

open('random_tags.txt',"w").close()
for j in range(len(files)):
    randomizer(files[j], nb_hashtags[j])

