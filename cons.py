with open("outve.txt", "r") as f:
    lines = f.readlines()

counter = 1
for i in range(len(lines)):
    line = lines[i].strip()
    try:
        numbering = int(line.split()[0])
    except:
        lines[i] = 'fail'+line
        continue        
    if numbering != counter:
        if numbering==1:
            counter=2
            continue
        else:
            lines[i] = 'fail'+line
    counter += 1

with open("outvee.txt", "w") as f:
    f.writelines(lines)