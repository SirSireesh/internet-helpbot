import os

def search(key):
    it = 0
    f = open('/home/chinmaya/code/src/github.com/Sirsireesh/internet-helpbot/internethelpbot/api/index.php', 'r')
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
                    it += 1
        it += 1
        json_steps = {'The Steps are:': ' '}
        c = 0
    for i in steps:
        json_steps[i] = images[c]
        c += 1
    return json_steps
    
