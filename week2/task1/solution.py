import os
import io
import argparse
import tempfile
import json
import random
import string
from random import *
from collections import defaultdict
min_char = 8
max_char = 12
#allchar = string.ascii_letters + string.punctuation + string.digits
allchar = string.ascii_letters.lower() + string.digits



def generate():
    generated_string = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
    return generated_string


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", default="database.txt", help="Filename to store data")
parser.add_argument("-k", "--key", help="Add key-value to storage",  required=True)
parser.add_argument("-v", "--value", default="", help="Show key-value from storage or Add key-value to storage if key also provided")
parser.parse_args()
args = parser.parse_args()

#data = {}
data = defaultdict(list)
if os.stat(args.file).st_size == 0:
    with io.open(args.file, 'w', encoding='utf-8') as f:
        data[args.key] = list([args.key])
        f.write(json.dumps(data))
        f.close()

else:
    with open(args.file) as f:
        data = json.load(f)
        if args.value == "":
            try:
                print(', '.join(data[args.key]))
            except:
                print("None")
        else:
            if args.key in data:
                data[args.key].append(args.value)
            else:
                data[args.key] = []
                data[args.key].append(args.value)
    f.close()

with io.open(args.file, 'w', encoding='utf-8') as f:
    f.write(json.dumps(data))
    f.close()

print("Done")

#with open(args.file) as json_data:
#    data = json.load(json_data)
#    if args.value == "":
#        try:
#            print(', '.join(data[args.key]))
#        except:
#            print("None")
#    else:
#        data[args.key] = [args.key]
#json_data.close()


#with io.open(args.file, 'w', encoding='utf-8') as f:
#    f.write(json.dumps(data))
