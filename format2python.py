#Format to python

f = open("ALLR.txt", "r")

dummy = 0
filename = ""
counter = 0

while True:
    
    x = f.readline()
    if not x:
        break
    #tensor check means next is
    #name of file
    if(x) == '"tensor check"\n':
        prevname = filename
        c = f.read(7)
        #get rid of unwanted stuff
        c = c.replace('`', '')
        c = c.replace(',', '')
        filename = f'algos/{c}.txt'
        if filename == prevname:
            counter += 1
            filename = f'algos/{c}mod0.txt'
        else:
            counter = 0
        w = open(filename, "a")
        f.readline() #read rest of line
        f.readline() #read "FORMULA HERE!!!"
        
        #read until end of multiplications
        c = ""
        while True:
            prev = c
            c = f.read(1)
            #end of multiplication
            if c == "]":
                w.write(")\n")
                break
            
            #start function write
            if c == "=":
                w.write(c)
                w.write("func(")
            #separate parameters in function as long as
            #its the actual function and not integers
            #multiplied by a matrix part
            elif c == "*" and not prev.isnumeric():
                w.write(",")
            #write to file
            #check if end of expression, skip comma
            #add end parentheses + newline
            elif c == "," and (prev == "`" or prev == ")"):
                w.write(")")
                w.write("\n")
            #if underscore or ` or start or , then skip
            #skip parentheses also
            elif c == "`" or c == "_" or c == "[" or c=="," or c=="(" or c==")":
                dummy = 0
            #just write like normal
            else:
                w.write(c)
        
        #read until end of sum
        c = ""
        while True:
            prev = c
            c = f.read(1)
            #end of sum
            if c == "]":
                w.write("\n")
                break
            
            #write to file
            #check if end of expression, skip comma
            #and newline. extra thing added to be sure
            #its the end of a thing
            if c == "," and prev.isnumeric():
                d = f.read(1)
                if not d.isnumeric():
                    w.write("\n")
                else:
                    w.write(d)
            #if underscore or ` or start or , then skip
            elif c == "`" or c == "_" or c == "[" or c==",":
                dummy = 0
            #just write like normal
            else:
                w.write(c)
        
        #end of converting
        #close file
        w.close()
        #keep reading
        
     
f.close()