#!/usr/bin/env python

import random   # Random number generator
import os       # Crossplatform OS rutines
import sys      # interpreter tools


legal_chars = "abcdefghijklmnopqrstuvwxyz"+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"+"0123456789_"


def random_string(length=6, prefix="", charz=legal_chars):
    rnd_str=prefix.join(random.choice(charz) for _ in range(length))
    return rnd_str


def generate_tree(target, dirs, rec_depth=3, verbose=False):
    
    if verbose:
        print "creating lists for storing names of directories"
    dir_array = []
    rec_array = []
 
    for i in range(rec_depth):
        rec_array.append(random_string())
        if verbose:
            print "makes random string and adds it to array of length rec_depth"
        for j in range(random.randint(0,dirs)):
            dir_array.append(random_string())    
            os.makedirs(rec_array[i]+'/'+dir_array[j])
            if verbose:
                print "makes new directories"
       

def populate_tree(target, files, size, start_time, end_time, verbose=False):
    start_path = target
    
    dir_list = []
    file_list = []

    # go into every directory and do the file reading and writing
    for root, dirs, filez in os.walk(os.getcwd()):
        for dir in dirs:
            dir_list.append(os.path.join(root, dir))
            if verbose:
                print "walks all directories, adds names of directories to list"
    
    for x in range(len(dir_list)):
        os.chdir(dir_list[x])
        if verbose:
            print "changed directory to directory in list"
        
        for y in range(random.randint(0,files)):
            filename = random_string()+".txt"                    
            new_file = open(filename, 'w')                       
            new_file.write(random_string(random.randint(0,size*1024),"", legal_chars))    
            os.utime(filename, (start_time, end_time))            
            file_list.append(filename)
            if verbose:
                print "created new file :"+file_list[y]


if __name__ == "__main__":     

    l = len(sys.argv)

    if l < 4:
        print "Not enough arguments included."
        print "usage: %s target dirs files " % sys.argv[0] +\
            "[size rec_depth start end seed verbose]"
        sys.exit(0)

    target = sys.argv[1]
    dirs = int(sys.argv[2])
    files = int(sys.argv[3])

    # And-or trick to use argv only if argv is long enough.
    rec_depth = l<5 and 2 or int(sys.argv[4])
    size = l<6 and 1000 or int(sys.argv[5])
    start = l<7 and 1388534400 or int(sys.argv[6])
    end = l<8 and 1406851200 or int(sys.argv[7])
    seed = l<9 and "0" or sys.argv[8]
    verbose = l<10 and "0" or sys.argv[9]

    # Fix the random seed (if not None):
    random.seed(int(seed) or None)

    os.chdir(target)
    generate_tree(target, dirs, rec_depth, int(verbose))
    populate_tree(target, files, size, start, end, int(verbose))