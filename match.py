with open("in.txt", "r") as f_in, open("ou.txt", "r") as f_out, open("des.tsv", "w") as f_des:
    for line_in, line_out in zip(f_in, f_out):
        numbering_in, source = line_in.strip().split(maxsplit=1)
        numbering_out, destination = line_out.strip().split(maxsplit=1)
        assert numbering_in == numbering_out, f"Numbering mismatch: {numbering_in} != {numbering_out}"
        f_des.write(f"{source}\t{destination}\n")
