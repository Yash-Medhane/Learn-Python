
def table(n):
    str=""
    for i in range(1,11):
        str+=f'{n} X {i} = {n*i} \n'

    with open(f'./chapter7/tables/table_{n}','w') as f:
        f.write(str)


for i in range(1,21):
    table(i)