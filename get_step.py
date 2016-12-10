#!/usr/bin/env python3.4

import os

def search(key):
    it = 0
    f = open('index.php', 'r')
    lines = f.readlines()
    it = 0
    for i in lines:
        if '===' in i:
            if key in i:
                while '===' not in lines[it + 1]:
                    print(lines[it])
                    it += 1
        it += 1

search("Sending")
