import os
import json
import random

def generate():
    '''
    https://github.com/LearnedVector/A-Hackers-AI-Voice-Assistant/tree/master
    Highly inspired by this
    '''
    data = []
    percentage = 0.8
    zero = os.listdir("zero")
    one = os.listdir("one")
    for z in zero:
        data.append({
            "key": os.path.join("zero", z),
            "label": 0
        })
    for o in one:
        data.append({
            "key": os.path.join("zero", o),
            "label": 1
        })      
    random.shuffle(data)

    f = open(f"train.json", "w")

    with open("train.json", "w") as f:
        d = len(data)
        i=0
        while(i<int(d-d/percentage)):
            r=data[i]
            line = json.dumps(r)
            f.write(line + "\n")
            i = i+1

        f = open(f"train.json", "w")

    with open("test.json", "w") as f:
        d = len(data)
        i=0
        while(i<int(d-d/percentage)):
            r=data[i]
            line = json.dumps(r)
            f.write(line + "\n")
            i = i+1

if __name__ == "__main__":
    generate()
