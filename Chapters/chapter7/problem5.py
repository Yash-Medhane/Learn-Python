word = ['donkey','gande','pagal']

with open("./temp.txt",'r') as f:
    context=f.read()

for i in word:
   context = context.replace(i,"#"*len(i))

with open("./temp.txt",'w') as f:
    f.write(context)