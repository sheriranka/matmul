#Format to python


#f is file
#m is rows
#n is cols
def divide(m,n,f):
    
    f.write(f'def div{m}x{n}(a):\n\n')
    
    #length of col
    f.write(f'\tcol = len(a)//{m}\n')
    #length of row
    f.write(f'\trow = len(a[0])//{n}\n\n')
      
    #variable assignment
    
    for i in range(m):      
        f.write(f'\t#row {i+1}\n\n')
        for j in range(n):
            #tab
            f.write('\t')
            if i == 0:
                if j == 0:
                    f.write(f'a{i+1}{j+1} = a[0:col,{j}:row]\n')
                elif j == 1:
                    f.write(f'a{i+1}{j+1} = a[0:col,row:{j+1}*row]\n')
                else:
                    f.write(f'a{i+1}{j+1} = a[0:col,{j}*row:{j+1}*row]\n')
            elif i == 1:
                if j == 0:
                   f.write(f'a{i+1}{j+1} = a[col:{i+1}*col,{j}:row]\n')
                elif j == 1:
                   f.write(f'a{i+1}{j+1} = a[col:{i+1}*col,row:{j+1}*row]\n')
                else:
                   f.write(f'a{i+1}{j+1} = a[col:{i+1}*col,{j}*row:{j+1}*row]\n')
            else:
                if j == 0:
                   f.write(f'a{i+1}{j+1} = a[{i}*col:{i+1}*col,{j}:row]\n')
                elif j == 1:
                   f.write(f'a{i+1}{j+1} = a[{i}*col:{i+1}*col,row:{j+1}*row]\n')
                else:
                   f.write(f'a{i+1}{j+1} = a[{i}*col:{i+1}*col,{j}*row:{j+1}*row]\n')
    
    
    
    #variable return
    
    f.write("\n\treturn (")
    for i in range(1, m+1):
        
        if i != 1:
            f.write("\n\t  ")
        
        for j in range(1,n+1):
            if i == m and j == n:
                f.write(f'a{i}{j})')
            elif j == n+1:
                f.write(f'a{i}{j},\n')
            else:
                f.write(f'a{i}{j}, ')
                

#m and n and file
#keep m and n consistent
def build(m, n, f):
    
    f.write("\tresult = np.concatenate((")
    
    for i in range(1,n+1):
        f.write("np.concatenate((")
        for j in range(1,m+1):
            if j == m:
                f.write(f'c{j}{i}')
            else:
                f.write(f'c{j}{i}, ')
        
        if i == n:
            f.write('), axis=0)), ')
        else:
            f.write('), axis=0), ')
        
    f.write("axis=1)")
    
    f.write("\n\n\treturn result\n\n")

#write func header

def func_head(f,mod0,tensor):
    
    #m and n are swapped here sorry
    m = tensor[0]
    n = tensor[1]
    p = tensor[2]
    
    #write function name
    f.write(f'def mat{m}{n}{p}')
    if not mod0:
        f.write("mod2")
    f.write("(a,b,depth):")
    f.write("\n\n")
    #write matrix variables
    f.write("\tif depth == 0:\n")
    if mod0:
        f.write("\t\treturn strassenInit(a,b,True)")
    else:
        f.write("\t\treturn strassenInit(a,b,False)")
        
    f.write("\n\telse:\n")
    #a
    f.write("\n\n")
    
    f.write("\t\t")
    for i in range(1,m+1):
        for j in range(1,n+1):
            if i == m and j == n:
                f.write(f'a{i}{j} ')
            else:
                f.write(f'a{i}{j}, ')
    f.write(f'= div{m}x{n}(a)\n')
    #b
    f.write("\t\t")
    for i in range(1,n+1):
        for j in range(1,p+1):
            if i == n and j == p:
                f.write(f'b{i}{j} ')
            else:
                f.write(f'b{i}{j}, ')
    f.write(f'= div{n}x{p}(b)\n')
    
    f.write("\n\n")
   
    
#write functions by reading from file 

    
def writemod0(f,w,tensor):
    
    #strings
    s = f'mat{tensor[0]}{tensor[1]}{tensor[2]}'
    #i had to look this up

    while True:
        c = f.read(1)
        if not c:
            break
        
        w.write("\t\t")
        if c == " ":
            #skip weird space and read entire line
            c = f.readline()
        
        #if weird space isnt there then its fine
        else:
            w.write(c)
            c = f.readline()
            
        new = c.replace("func",s)
        new = new.replace(")",", depth-1)")
        w.write(new)


def writemod2(f,w,tensor):
    
    #strings
    s = f'mat{tensor[0]}{tensor[1]}{tensor[2]}mod2'
    
    while True:
        c = f.read(1)
        if not c:
            break
        
        w.write("\t\t")
        if c == " ":
            #skip weird space and read entire line
            c = f.readline()
        
        #if weird space isnt there then its fine
        else:
            w.write(c)
            c = f.readline()
            
        new = c.replace("func",s)
        new = new.replace("+","^")
        new = new.replace(")",", depth-1)")
        w.write(new)
        

#filename
#mod0, true or false
def all2python(filename,mod0,w):
    
    f = open("algos/"+filename, "r")
    #remove the .txt
        
    #get tensor from file :3
    tensor = filename[0:3]
    t = []
    for i in range(3):
        t.append(int(tensor[i]))


    #call divide
    if(t[0] == t[1] and t[1] == t[2]):
        divide(t[0],t[0],w)
    else:
        divide(t[0],t[1],w)
        w.write("\n\n")
        divide(t[1],t[2],w)
        w.write("\n\n")

    #call actual func creation
    w.write("\n\n")
    func_head(w, mod0, t)
    
    #call read
    if mod0:
        writemod0(f, w, t)
    else:
        writemod2(f, w, t)
    
    w.write("\n")
    
    #call unite matrix
    
    build(t[0],t[2],w)
    
    w.write("\n\n")
    
    f.close()
    
    
#actually read all the files now!
fs = open("files.txt","r")
md = open("filesmod.txt","r")

w = open("allPython.txt", "a")
files = fs.readline().split()
mods = md.readline().split()

m = []

for i in mods:
    if i[-5] == "0":
        m.append(True)
    else:
        m.append(False)
        

for i in range(len(files)):
    all2python(files[i], m[i], w)
    
w.close()



