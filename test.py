import re

with open('outv.txt', 'r') as file:
    data = file.read()
    
    # remove multiple line breaks
    data = re.sub('\n+', '\n', data)
    
    # remove multiple spaces
    data = re.sub(' +', ' ', data)
    
with open('outv.txt', 'w') as file:
    file.write(data)
with open("outv.txt", "r") as f_in, open("outve.txt", "w") as f_out:
    for line in f_in:
        if len(line.strip()) >= 6:
            f_out.write(line)
