#****************************************************************************************************************************************************
#
# This module is designed to pull "Image ImageDescription" from a folder of images and generate a CSV file for use in ContentDM collection metadata
#
# The outputs are:
#       * a CSV file of the file names, dc:identifier(s), and metadata pulled from Exif "Image ImageDescription" and " Image DateTime"
#
# Created by Jacob Shelby, November 2015, based on a PDF page extraction module built by Kelly Thompson
#
#****************************************************************************************************************************************************

#**************************************************************
# import all the necessary libraries
#**************************************************************

#import exifread
import exifread

# used to create directories
import os

# regular expressions
import re

# import cStringIO
import string

# library for creating/workingwith/writing to/parsing CSV files.  We're outputting to CSV
import csv

# library for working w/ file-like objects
import io

# get the date for the filename
import datetime
today = datetime.date.today().strftime('%Y-%m-%d')


#**************************************************************
# Create the directory folder where you will put everything you're collecting
#**************************************************************

# create variable for name of directory
datadir = 'pages'

# path is collection of fx w/in OS.
# could say from OS import PATH to save memory
# returns true/false
# keeps all files in same place
if not os.path.isdir(datadir):
    os.mkdir(datadir)

#**************************************************************
# Create the CSV file for the metadata for all the images you are mining.
#**************************************************************

# create metadata file
# should get current date instead of being hard coded
# get date and save as variable, put variable in...
# mode w=write + read/write??
metadata = open(datadir + '/pages_' + today + '.csv', mode='w+')

##########################################
# create writer for writing to CSV file
wtr = csv.writer(metadata, delimiter=',')
##########################################

# create array for header row
headerrow = ['Annotation', 'Date Digital', 'Identifier (DOI)', 'File Name']
wtr.writerow(headerrow)

# getting folder
folderpath = './'

def to_unicode_or_bust(
        obj, encoding='utf-8'):
    if isinstance(obj, basestring):
        if not isinstance(obj, unicode):
            obj = unicode(obj, encoding)
    return obj

                      
#**************************************************************
# Begin the process 
# For each:
#**************************************************************


folderlist = os.listdir(folderpath)

for d in folderlist:
    if d.endswith('.tif') or d.endswith('.jpg'):
        d = d.strip(' ')
        #row = [d]
        #wtr.writerow(row)
        imageopen = open(folderpath + '/' + d, 'rb')
        tags = exifread.process_file(imageopen)
    
        ImageDescription = "Image ImageDescription"
        DateTime = "Image DateTime"
        if ImageDescription in tags:
            row = [tags[ImageDescription],tags[DateTime],d[:-4],d]
            wtr.writerow(row)
        else:
            row = ['',tags[DateTime],d[:-4],d]
            wtr.writerow(row)


    #****************************************************************
    # keep cycling...
    #****************************************************************
        
#****************************************************************
# close the CSV file
#****************************************************************
metadata.close()

print "Done."

