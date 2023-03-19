import re

with open("des.txt", "r") as f:
    lines = f.readlines()

with open("des.txt", "w") as f:
    for line in lines:
        # Match the pattern "numbering followed by a non-space character"
        match = re.match(r"(\d+)(\D)", line)
        if match:
            # Insert a space between the numbering and the non-space character
            line = f"{match.group(1)} {match.group(2)}{line[match.end(2):]}"
        f.write(line)