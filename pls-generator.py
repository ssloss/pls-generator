#!/usr/bin/env python3.3

import os
import sys
import argparse

"""
Creates a .pls playlist in the current working directory from all the files 
with the extension given as a command line argument.
"""

def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description="Make a .PLS file out of all \
    the video or audio files in a given directory.")
    parser.add_argument("-t", "--type", required=True, help="Video file type (ex. mp4, flv, etc.)", 
            type=str)

    args = parser.parse_args()
    

if __name__ == '__main__':
    sys.exit( main() )
