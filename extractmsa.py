import os
import re

full_path = os.path.realpath(__file__)
directory = os.path.dirname(full_path)
count = 0

for filename in os.listdir(directory):
    if filename.endswith(".clustal_num"):
        count = count + 1
        print("File founded\t" + filename)
        f = open(filename, "r")
        line_list = f.readlines()
        f.close()
        savename = ""
        output = ">"
 
        for i in range(len(line_list)):
            if i % 4 == 0 and i != 0:
                tokenized = line_list[i].split()
                if i == 4:
                    savename = tokenized[0]
                    output = output + savename
                output =  output + "\n" + tokenized[1] 
            else:
                continue
        
        savedname = re.sub('[^a-zA-Z0-9 \n\.]', '.', savename) + ".fasta"
        temp = open(savedname, "w")
        temp.write(output)
        temp.close()
        print("Saved as\t" + savedname + "\n")
    else: 
        continue
if(count == 0):
    print("There is no .clustal_num file in ", directory)
else:
    print("Done converting ", count, " files!")