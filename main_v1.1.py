# %%
import time

# Counter to check time of calculation
before = time.time()

#variables for recursion
temp=""
z=0

#function to recurse through each block and divide it based on whitespaces 
def rec_str(n,block):
    global temp
    global z
    z+=1
    if not block[n].isspace() and n<len(block)-1:
        temp+=block[n]
        rec_str(n+1,block)
    return

# Opening file and saving lines as a list.
def pro1():
    file = open(r"08306.txt", 'r')

    q1 = []
    for line in file:
        q1 += [line]

    file.close()

    q2 = []

    for line in q1:
        if line[0].isnumeric():
            q2 += [line]
        else:
            continue

    return q2, q1


q2, q1 = pro1()


# %%
def pro2():
    strut = ()
    global block
    global z
    global temp
    for block in q2:
        temp=""
        block+=" "
        i=0
        z=0
        l=[]
 
        while i <len(block):
            temp=""
            z=0
            if not block[i].isspace():
                rec_str(i,block)
                i+=z-1
                if temp=="ABA":
                    l.append("ABSENT")
                    l.append("ABSENT")
                elif temp=="ABST":
                    l.clear()
                    l=[""]*30
                else:
                    l.append(temp)
            i+=1
        roll_no=l[0]
        grd1,grd2,grd3,grd4,grd5=l[-17],l[-14],l[-11],l[-8],l[-5]
        mrk1,mrk2,mrk3,mrk4,mrk5=l[-18],l[-15],l[-12],l[-9],l[-6]
        sub1,sub2,sub3,sub4,sub5=l[-19],l[-16],l[-13],l[-10],l[-7]
        fin = sub = ()
        sub += (sub1, mrk1, grd1),
        sub += (sub2, mrk2, grd2),
        sub += (sub3, mrk3, grd3),
        sub += (sub4, mrk4, grd4),
        sub += (sub5, mrk5, grd5),
        fin=l[-4]+l[-3]+l[-2]+l[-1]
        strut += ((roll_no, sub, fin)),

    return strut

q3 = pro2()


# %%

def array_maker(process):
    a_roll_no, a_sub1, a_sub2, a_sub3, a_sub4, a_sub5, a_mrk1, a_mrk2, a_mrk3, a_mrk4, a_mrk5, a_grd1, a_grd2, a_grd3, a_grd4, a_grd5, a_fin = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []

    varl = ['a_roll_no', 'a_sub1', 'a_sub2', 'a_sub3', 'a_sub4', 'a_sub5', 'a_mrk1', 'a_mrk2', 'a_mrk3', 'a_mrk4',
            'a_mrk5', 'a_grd1', 'a_grd2', 'a_grd3', 'a_grd4', 'a_grd5', 'a_fin']

    array_raw = {}

    for item in process:
        a_roll_no += [item[0]]
        a_sub1 += [item[1][0][0]]
        a_mrk1 += [item[1][0][1]]
        a_grd1 += [item[1][0][2]]

        a_sub2 += [item[1][1][0]]
        a_mrk2 += [item[1][1][1]]
        a_grd2 += [item[1][1][2]]

        a_sub3 += [item[1][2][0]]
        a_mrk3 += [item[1][2][1]]
        a_grd3 += [item[1][2][2]]

        a_sub4 += [item[1][3][0]]
        a_mrk4 += [item[1][3][1]]
        a_grd4 += [item[1][3][2]]

        a_sub5 += [item[1][4][0]]
        a_mrk5 += [item[1][4][1]]
        a_grd5 += [item[1][4][2]]

        a_fin += [item[2]]

    array_raw = [a_roll_no, a_sub1, a_sub2, a_sub3, a_sub4, a_sub5, a_mrk1, a_mrk2, a_mrk3, a_mrk4, a_mrk5, a_grd1,
                 a_grd2, a_grd3, a_grd4, a_grd5, a_fin]

    array_f = dict(zip(varl, array_raw))

    return array_f, a_roll_no


array, a_roll_no = array_maker(q3)

# %%

import numpy as np
import pandas as pd

df = pd.DataFrame(array, index=a_roll_no)

# %%

sub = {}

for row in df.itertuples():

    print(row.Index, row.a_sub1, row.a_mrk1, row.a_grd1)
    # sub1
    if row.a_sub1 not in sub:
        sub[row.a_sub1] = ((row.Index, row.a_mrk1, row.a_grd1)),

    elif row.a_sub1 in sub:
        sub[row.a_sub1] += (row.Index, row.a_mrk1, row.a_grd1),
    # sub2
    if row.a_sub2 not in sub:
        sub[row.a_sub2] = ((row.Index, row.a_mrk2, row.a_grd2)),

    elif row.a_sub2 in sub:
        sub[row.a_sub2] += (row.Index, row.a_mrk2, row.a_grd2),
    # sub3
    if row.a_sub3 not in sub:
        sub[row.a_sub3] = ((row.Index, row.a_mrk3, row.a_grd3)),

    elif row.a_sub3 in sub:
        sub[row.a_sub3] += (row.Index, row.a_mrk3, row.a_grd3),
    # sub4
    if row.a_sub4 not in sub:
        sub[row.a_sub4] = ((row.Index, row.a_mrk4, row.a_grd4)),

    elif row.a_sub4 in sub:
        sub[row.a_sub4] += (row.Index, row.a_mrk4, row.a_grd4),
    # sub5
    if row.a_sub5 not in sub:
        sub[row.a_sub5] = ((row.Index, row.a_mrk5, row.a_grd5)),

    elif row.a_sub5 in sub:
        sub[row.a_sub5] += (row.Index, row.a_mrk5, row.a_grd5),

del row

# %%

df_d = {}


def sub_to_df(key_0):
    roll, mrk, grd = (), (), ()

    for item in sub[key_0]:
        roll += (item[0]),
        mrk += (item[1]),
        grd += (item[2]),

    array_data = [roll, mrk, grd]
    array_head = ['Roll No', 'Marks', 'Grade']

    df_f = pd.DataFrame(dict(zip(array_head, array_data)))

    df_d[key_0] = df_f

    return df_d


for key in sub:
    df_d = sub_to_df(key)

del key

del a_roll_no
del q1, q2, q3, sub

after = time.time()

print('Elapsed time:', after - before)

# import csv
# varl = ['a_roll_no','a_sub1','a_sub2','a_sub3','a_sub4','a_sub5','a_mrk1','a_mrk2','a_mrk3','a_mrk4','a_mrk5','a_grd1','a_grd2','a_grd3','a_grd4','a_grd5','a_fin']
# with open('raw.csv', 'a') as csv_file:
#    csv_writer = csv.DictWriter(csv_file, fieldnames=varl
#                                )
#    csv_writer.writeheader()
#    csv_writer.writerow(df)

# Giving errors while saving to excel.
# Will look into it soon
from pandas import ExcelWriter

##from pandas.io.parsers import ExcelWriter
#
#
# def save_xls(list_dfs, xls_path):
#    with ExcelWriter(xls_path) as writer:
#        for n, df in enumerate(list_dfs):
#            df.to_excel(writer,'sheet%s' % n)
#        writer.save()
#
# save_xls(df_d,r'tet1.xlsx')

# Saving to csv
pd.concat(df_d).to_csv('filename')
