import random
import os
import errno
import sys

#nom des database
files = ['hashtags_base', 'abstract', 'graphics', 'minimalism', 'art', 'hdr']
#qualité de charque hashtags de la database
nb_hashtags = [18,3,3,2,2,2]

def randomizer (my_file, nb_hashtags):
    #stockage du text dans un tableau input_hashtags
    f=open('db/' + my_file +'.txt',"r")
    input_hashtags=f.read().split('\n')
    f.close()
    #genere un tableau de 10 élements de chiffres aléatoire
    #de 0 à la taille du tableau input_hashtags sans doublons
    rand_nb=random.sample(range(len(input_hashtags)-1),nb_hashtags)
    #genere un tableau output_hashtags rempli de 0 de la taille de input_hashtags
    output_hashtags = [0] * nb_hashtags
    fb=open('random_tags.txt',"a")
    for i in range(len(rand_nb)):
        output_hashtags [i] = input_hashtags[rand_nb[i]]
        fb.write(output_hashtags[i])
        #fp.write("\n")
        fb.write(" ")
    fb.close()


def create_path(filename):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    with open(filename, "w") as f:
        f.write("FOOBAR")


open('random_tags.txt',"w").close()
for j in range(len(files)):
    randomizer(files[j], nb_hashtags[j])

