word  = str(input())
file_name = word[0]
file_o = open(f'{file_name}.txt',"r")
for line in file_o:
    if word == line.rstrip("\n").split(":")[0]:
        print(line.rstrip("\n").split(":")[1])
        break
    
file_o.close()