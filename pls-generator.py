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

    file_list = []

    # navigate directory tree
    for dirpath, dirname, curFiles in os.walk(path):
        # for each file in the current directory
        for iFile in curFiles:
            curName, curExtension = os.path.splitext(iFile)
            # if the extension matches, keep it around
            if curExtension == fileType:
                fileName = os.path.join(dirpath, iFile)
                file_list.append( fileName )

    return file_list

def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description="Make a .PLS file out of all \
    the video or audio files in a given directory.")
    parser.add_argument("-e", "--extension", required=True, help="Video file \
            extension (ex. mp4, flv, etc.)", type=str)
    #TODO: add ability to use other than CWD
    #TODO: add ability to save to location other than CWD
    args = parser.parse_args()

    # search for files
    mediaFileList = find_files_of_type(args.extension) 
    print(mediaFileList)
    

if __name__ == '__main__':
    sys.exit( main() )
