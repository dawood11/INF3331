#!/usr/bin/env python

import random   # Random number generator
import os       # Crossplatform OS rutines
import sys      # interpreter tools


legal_chars = "abcdefghijklmnopqrstuvwxyz"+\
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"+"0123456789_"


def random_string(length=6, prefix="", legal_chars=legal_chars):
    """
Create a random string of text.

Parameters
----------
length : int
    Length of the string (minus the prefix part).
prefix : string
    Prefix the string with some text.
legal_chars : string
    A string of charracter that are allowed to be used in the
    output.

Returns
-------
rnd_str : str
    A string of random charracters.
    """
    # Insert user code here
    rnd_str = prefix.join(random.choice(legal_chars) for _ in range(length))
    # The method picks a random character from "legal_chars"
    # and for every iteration through the loop,
    # that character is joined to the string "rnd_str" until it has a spesific length

    return rnd_str

def generate_tree(target, dirs=3, rec_depth=2, verbose=False):
    """
Genereate a random folder structure with random names.

Parameters
----------
target : str
    Path to the root where folders are to be created.
dirs : int
    Maximum number of directories to be created per directory.
rec_depth : int
    Maximum directory depth.
verbose : bool
    Be loud about what to do.
    """
    # Insert user code here
    dir_depth = random.randrange(2,rec_depth+1) #sets the random directory depth between 2 and the chosen maximum number.
    dirs = random.randrange(2,dirs+1) #sets the random number of directories to be created per directory.

    #for x in range (3):
    make_Dir_tree(target,dir_depth,dirs, verbose)  

def make_Dir_tree(target, dir_depth, dirs, verbose):
    rand_s = random_string()
    rand_dirs = random.randrange(1, dirs)

    if dir_depth>=0 :
        for x in range (1, random.randint(1, dirs)):
            new_dir = target+"/"+random_string()
            os.makedirs(new_dir) #creates a directory with a random string inside the target directory
            make_Dir_tree(new_dir, dir_depth-1, dirs, verbose) #the recursive method continues but this time the target as the new directory created
            populate_tree(new_dir, random.randint(1, dirs), 800, 1388534400, 1406851201000, verbose) #calls the method that creates the files
        dir_depth-=1

def populate_tree(target, files=5, size=800, start_time=1388534400,
        end_time=1406851201000, verbose=False):
    """
Generate random files with random content.

Parameters
----------
target : str
    Path to the file tree where the files are being created.
files : int
    Maximum number of directories to be created.
size : int
    Maximum size in kilobyte for each file.
start_time : int
    Lower bound for access time (atime) and modified time (mtime)
    allowed in each file.
    Denoted in Unix time format.
end_time : int
    Same as start_time, but for upper bound.
verbose : bool
    Be loud about what to do.
    """
    
    new_dir_file = target+"/"+random_string() 
    
    if files >= 0:
        if os.path.exists(new_dir_file):
            print "ERROR!!!" #checks if the directory exists at all. returns an Error if not.
        else:
            new_file = open(new_dir_file, "w+") # a file is created and called a name with a random string
            if verbose == True:
                print new_dir_file

            new_file.write(random_string(random.randint(0,size),"", legal_chars + "\n"))
            # the random string inside the files is written with a size of a random number between 0 and constant 500(size)
            new_file.close()
            
            os.utime(new_dir_file, (start_time, end_time)) # Changing modification and access time
            populate_tree(target, files-1, size, start_time, end_time, verbose) #goes through recursivly again, but this time with a smaller option of random files
  #  def walk_function(arg, dirname, fnames):
        """
Function used in os.path.walk

Following the logic of Python scoping, this is a local function,
only visible inside of populate_tree.
This function should be passed to os.path.walk.

Parameters
----------
arg : obj
    Arbitrary argument specified at initialization.
dirname : str
    Name of a directory in file tree (changes with each call.
fnames : list
    List of filenames in file tree.
        """
        # Fill in code for walk function

  #  os.path.walk(target, walk_function, None)




# If-test to ensure code only executed if ran as stand-alone app.
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
    size = l<5 and 1000 or int(sys.argv[4])
    rec_depth = l<6 and 2 or int(sys.argv[5])
    start = l<7 and 1388534400 or int(sys.argv[6])
    end = l<8 and 1406851200 or int(sys.argv[7])
    seed = l<9 and "0" or sys.argv[8]
    verbose = l<10 and "0" or sys.argv[9]

    # Fix the random seed (if not None):
    if seed == "0":
        random.seed(None)
    else:       
        random.seed(int(seed))

    generate_tree(target, dirs, rec_depth, verbose)
