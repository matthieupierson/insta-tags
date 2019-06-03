import random
import os
import sys

######################################################################################
#nom des database
#files = ['hashtags_base', 'abstract', 'graphics', 'minimalism', 'art', 'hdr']


######################################################################################
#quantitée de chaque hashtags de chaque database
#nb_hashtags = [18,3,3,2,2,2,2]


######################################################################################
#recuperer les noms des databases et les nombres des tags souhaités

info = []
nb_tags = []
databases = []

f = open("config.txt")
file = f.read().splitlines()

for i in range(len(file)) : 
    info.append(file[i].split())
    databases.append(info[i][0])
    nb_tags.append(info[i][1]) 

f.close()


######################################################################################
#randomiser

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




#################################### M A I N #########################################
open('random_tags.txt',"w").close()

f0 = open('random_tags.txt',"a")
f0.write(".\n.\n.\n.\n")
f0.close()

for j in range(len(databases)):
    #print(databases[j])
    #print(nb_tags[j])
    randomizer(databases[j], int(nb_tags[j]))