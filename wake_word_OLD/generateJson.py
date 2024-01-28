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
    one = os.listdir("one")  # Fix: Corrected the directory to "one"
    
    for z in zero:
        data.append({
            "key": os.path.join("zero", z),
            "label": 0
        })
    for o in one:
        data.append({
            "key": os.path.join("one", o),  # Fix: Corrected the directory to "one"
            "label": 1
        })      
    random.shuffle(data)

    total_files = len(data)
    train_size = int(total_files * percentage)

    with open("train.json", "w") as f:
        for r in data[:train_size]:
            line = json.dumps(r)
            f.write(line + "\n")

    with open("test.json", "w") as f:
        for r in data[train_size:]:
            line = json.dumps(r)
            f.write(line + "\n")

if __name__ == "__main__":
    generate()
