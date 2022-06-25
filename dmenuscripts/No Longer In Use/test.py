#!/usr/bin/env python3
import subprocess
import time

with open("./test.txt","r",encoding="UTF-8") as f:
    lines = f.read().split("\n")
    i=0
    finalline=""
    count = 0
    for line in lines:
        count=count+1
        print("██████████████ On Count : {} ███████████████".format(count))
        if line!="":
            if (i==2):
                subprocess.run("chromium --incognito {}".format(finalline), shell=True)
                finalline=line
            else:
                finalline=finalline + " " + line
            i=(i+1)%3
    subprocess.run("chromium --incognito {}".format(finalline), shell=True)
