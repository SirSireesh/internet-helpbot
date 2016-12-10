#!/usr/bin/env python3.4

import os
from subprocess import call

def search(key):
    it = 0
    f = open('index.php', 'r')
    lines = f.readlines()
    it = 0
    img = []
    images = []
    steps  = []
    for i in lines:
        if '===' in i:
            if key in i:
                while '===' not in lines[it + 1]:
                    #print(lines[it])
                    if '[[' in lines[it]:
                        img = lines[it]
                        it1 = 0
                        #print(img)
                        for c in img:
                            if c != '[':
                                it1 += 1
                            else :
                                break
                        img = img[it1 + 1:]
                        it1 = 0
                        for c in img:
                            if c != ':':
                                it1 += 1
                            else :
                                break
                        img = img[it1 + 1:]
                        it1 = 0
                        for c in img:
                            if c != '|':
                                it1 += 1
                            else:
                                break
                        img = img[:it1]
                        img = img.replace(' ', '-') 
                        images.append(img)
                        steps.append(lines[it][:(len(lines[it])) - (len(img) + 18)])
                        print("The step is : ", lines[it][:(len(lines[it])) - (len(img) + 18)])
                    it += 1

#        call(["open",'/Volumes/Data/Temp/GMail/' +  str(img)])

        it += 1
    print("Images :\n", images)
    print("Steps :\n", steps)

search("Sending")
