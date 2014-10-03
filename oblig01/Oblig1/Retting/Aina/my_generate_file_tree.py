#!/usr/bin/env python
#Assignment 2
import random   # Random number generator
import os       # Crossplatform OS rutines
import sys      # interpreter tools
import string   # Support functionalitiy for string opperations
import shutil   # Support high-level operations on files and collections of files.
import time
import datetime
legal_chars = string.letters + string.digits+ "_" #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_ 

def random_string( length = 6, prefix = "", legal_chars = legal_chars ):
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
(prefix + rnd_str): str
    A prefixed string pluss a random string.
    """
    
    rnd_str = ""
    for i in range( length ): #For every iteration, a caracter is added to "rnd_str" until is has a spesific length              
        rnd_str += random.choice( legal_chars )  # chooses a random character from "legal_chars"

    return prefix + rnd_str

def generate_tree( target, fld_name, dirs=3, rec_depth=2, verbose=False ):
    """
Genereate a random folder structure with random names.

Parameters
----------
target : str
    Path to the root where folders are to be created.
fld_name: str
    Name of folder I want to create
dirs : int
    Maximum number of directories to be created per directory.
rec_depth : int
    Maximum directory depth.
verbose : bool
    Be loud about what to do.
    """    
    
    if verbose: print "\nMAKING DIRECTORIE TREE::\n------------------------ " #Prints a Headline of what the program is doing. 
    
    def folder_output( depth_level, fld_name):
        """ 
    Creating a nice looking output if printed. 
    This is a local function, only visible inside of generate_tree.
   
    Parameters
    ----------
    depth_level: int
        Keeps tracks of the level you traversed to. 
    fld_name: str
        Name of folder I want to print. 
    Returns
    -------
    output: str
        Proper indented output for use in verbose printing
    fld_name: str
        Name of folder
        """
        
        output = ''
        while( depth_level >= 0 ):
            depth_level = depth_level - 1
            if depth_level == -1: 
                output += "- "  
            else : 
                output += "   "
        
        return output + fld_name
    
    def generate_tree_recursion( target, fld_name, depth_level ):
        """
    A recursion function. 
    This is a local function, only visible inside of generate_tree.
    Genereate a random folder structure with random names. 
    
    Parameters
    ----------
    target: str
        Path to the root where folders are to be created. 
    fld_name: str
        Name of folder I want to create.
    depth_level: int
        Keeps tracks of the level you traversed to.
        """
 
        if verbose: print folder_output( depth_level, fld_name ) #If true, it will print what the program is doing. 
        target = target + fld_name + os.path.sep
        os.mkdir( target ) 

        continue_recursion = random.choice( range( 1, rec_depth + 1 ) ) > depth_level  # Check that we dont overstep our random choice of directory depth. The allowed directory depth minus our current director level. 
        if continue_recursion : #should there be subdirs? If True, the recursion will continue. 
            subdirs = random.choice( range( 1, dirs + 1 ) ) #how many subdirs in this directory
            for i in range( 1, subdirs + 1 ): #Controls number of directory inside every directory
                generate_tree_recursion( target, random_string( ), depth_level + 1 ) #creates the subfolder structure
    
    
    generate_tree_recursion(target,fld_name, 0)
        
        

def populate_tree( target, files=5, max_size=800, start_time=1388534400,
        end_time=1406851201, verbose=False ):
    """
Generate random files with random content.

Parameters
----------
target : str
    Path to the file tree where the files are being created.
files : int
    Maximum number of directories to be created.
max_size : int
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
    
    if verbose: print "\nCREATING FILES:\n---------------- "
    def file_output( filename, dirname, size_of_file, atime, mtime ):
        """ 
    Creating a nice looking output if printed. 
    This is a local function, only visible inside of populate_tree.
    
    Parameters
    ----------
        filename: str
            file name of the file that have been created.
        dirname: str
            directory name where the fila has been created. 
        size_of_file: int
            The size given to the file
        atime: float
            The accesstime given to the file
        mtime: float
            The modificationtime give to the file. 
    Returns
    -------
    output: str
        A string containing filename, file size, accesstime, modificationtime and foldername
        
        """
        atime = time.strftime("%d %b %Y %H:%M", time.localtime( atime ) ) #human readable local time
        mtime = time.strftime("%d %b %Y %H:%M", time.localtime( mtime ) ) #human readable local time
        output = "- \""+ filename + "\": size %3g[kB], atime: %s, mtime: %s" %(size_of_file, atime, mtime)+ ", in folder: " + dirname 
        
        return output
    
    def walk_function( arg, dirname, fnames ):
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
        
        number_of_files = random.choice( range( 1, files + 1) ) #random number of files in each directory
 
        for i in range( 1, number_of_files + 1 ):
        #setting variables
            filename = random_string( ) #generate random filename
            atimes = start_time + random.random( ) * ( end_time - start_time ) # random access time.  
            mtimes =  start_time + random.random( ) * ( end_time - start_time ) # random modification time.
            size_of_file = int(random.random()*max_size)  # [kB] a random size with a max limit of size       
        #Writing to file
            file = open( dirname +os.path.sep +filename,"w" )  #open file for writing
            file.write( random_string( length = size_of_file*1024, legal_chars = legal_chars+ "\n" ) ) #writing to file with a string matching the wanted size(size_of_file), since each character = 1 byte. Including lineshift(\n) in legal character to get better text file variation. 
            file.close( )

            os.utime( dirname +os.path.sep + filename , ( atimes,mtimes ) ) #Changing modification and access time
            if verbose: print file_output( filename, dirname, size_of_file, atimes, mtimes ) # if True, prints out what the program is doing. 

    os.path.walk( target, walk_function, None )
    
    
# If-test to ensure code only executed if ran as stand-alone app.
if __name__ == "__main__":

    l = len( sys.argv )
    if l < 4:
        print "Not enough arguments included."
        print "usage: %s target dirs files " % sys.argv[ 0 ] +\
            "[size rec_depth start end seed verbose]"
        sys.exit( 0 )

    target = sys.argv[ 1 ]
    dirs = int( sys.argv[ 2 ] )
    files = int( sys.argv[ 3 ] )

    # And-or trick to use argv only if argv is long enough.
    size = l < 5 and 1000 or int( sys.argv[ 4 ] )
    rec_depth = l < 6 and 2 or int( sys.argv[ 5 ] )
    start = l < 7 and 1388534400 or int( sys.argv[ 6 ] )
    end = l < 8 and 1406851200 or int( sys.argv[ 7 ] )
    seed = l < 9 and "0" or sys.argv[ 8 ]
    verbose = l < 10 and "0" or sys.argv[ 9 ]
    
    # Fix the random seed (if not None):
    random.seed( int( seed ) or None )

    path = target 
    main_fld_name = "file_tree_aina" #Main folder name, to put all the other folders and files.
     
    #WARNING deletes the whole filetree if it exist. 
    if main_fld_name and os.path.exists(path + main_fld_name):#If the main folder exist, then delete it. This will eliminate errors due to allredy existing folder
        shutil.rmtree(path + main_fld_name) #have to use shutil for deleting everything in that file tree. 
    
    generate_tree( path, main_fld_name, dirs, rec_depth, int( verbose ) )
    populate_tree( path + main_fld_name, files, size, start, end, int( verbose ) )



