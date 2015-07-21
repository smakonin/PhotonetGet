#!/usr/bin/env python3
#
# Download photos from Photo.net (PhotonetGet.py)
# Copyright (C) 2015 Stephen Makonin. All Right Reserved.
#
# EXAMPLE: ./PhotonetGet.py dataset.txt 2

'''
How to obtain the original images?
----------------------------------

The photo ID is unique, but the exact URL of the files may change on the Photo.net 
server. Probably the best way to obtain the image URL is to download/wget the html 
page hosting the image, and scrape that html file for the image URL (there is 
usually a pattern that can be easily detected). The URLs for the html pages are 
currently of the following form:

    http://photo.net/photodb/photo?photo_id=<Photo-ID>
e.g.,
    http://photo.net/photodb/photo?photo_id=1008958

Instead of doing the above, at the time of this release, the images can be downloaded 
directly from URLs of the following form:

    http://gallery.photo.net/photo/<Photo-ID>-md.jpg
e.g.,
    http://gallery.photo.net/photo/1008958-md.jpg
'''

import sys, urllib.request

url = 'http://gallery.photo.net/photo/%d-md.jpg'
dir = './photos/%d-md.jpg'


if len(sys.argv) != 3:
    print()
    print('USAGE: %s [dataset.txt] [ids col from 1...]' % (sys.argv[0]))
    print()
    exit(1)

dataset = sys.argv[1]
colnum = int(sys.argv[2]) - 1

print('Opening dataset text file...')
with open(dataset) as fp:
    for line in fp:
        if len(line) < 2:
            continue

        cols = line.split(' ')
        id = int(cols[colnum])
        
        print('Downloading image id = %d...' % id)
        try:
            urllib.request.urlretrieve(url % id, dir % id)
        except urllib.error.URLError as e: 
            print('\tERROR: unable to download file:', e.reason) 
        except urllib.error.HTTPError as e: 
            print('\tERROR: unable to download file:', e.reason)
        except:
            print('\tERROR: unable to download file:', sys.exc_info()[0].code)   
