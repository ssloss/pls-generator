#!/usr/bin/env python3.3

import os
import sys
import argparse

"""
Creates a .pls playlist in the current working directory from all the files 
with the extension given as a command line argument.
"""

def find_files_of_type( fileType, path=os.path.abspath(os.curdir) ):
    """ Finds all the files of type 'fileType' in the directory given by 
    'path', and returns a list of their full paths 
    """

    # add the prepended dot to the fileType
    if fileType[0] != '.':
        fileType = '.' + fileType

    fileList = []

    # navigate directory tree
    for dirpath, dirname, curFiles in os.walk(path):
        # for each file in the current directory
        for iFile in curFiles:
            curName, curExtension = os.path.splitext(iFile)
            # if the extension matches, keep it around
            if curExtension == fileType:
                fileName = os.path.join(dirpath, iFile)
                fileList.append( fileName )

    return fileList

def make_pls(fileList):
    """ Makes a .PLS file given a list of files.
    File format given by:  https://wiki.videolan.org/Playlist/
    """

    # list concatenation is faster than string concat in python, so make a list of 
    # what will become our .PLS file
    plsStrList = []
    plsStrList.append('[playlist]\n')
    plsStrList.append('NumberOfEntries=' + str(len(fileList)) + '\n') 

    for i, iFile in enumerate(fileList):
        plsStrList.append('File' + str(i+1) + '=' + iFile + '\n')

    # return the string form
    return ''.join(plsStrList)

def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description="Make a .PLS file out of all \
    the video or audio files in a given directory.")
    parser.add_argument("-e", "--extension", required=True, help="Video file \
            extension (ex. mp4, flv, etc.)", type=str)
    #TODO: add ability to use other than CWD
    #TODO: add ability to specify save filename
    #TODO: add ability to save to location other than CWD
    args = parser.parse_args()

    # search for files
    mediaFileList = find_files_of_type(args.extension) 

    # write out the PLS file
    fileName = 'playlist.pls'
    with open(fileName, 'w') as pls_file:
        pls_file.write( make_pls(mediaFileList) )
    

if __name__ == '__main__':
    sys.exit( main() )
