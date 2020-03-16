from tkinter import *
from tkinter import filedialog


root = Tk()
root.title('Organise AHEAD')
#root.iconbitmap(r'D:\resources\GUI\ada.ico')

root.filename = filedialog.askopenfilename(initialdir = '/', title='Select a file to process', filetypes=(("TXT Files", "*.txt"),("All Files", "*.*")))

#eventloop
root.mainloop()

#backend
import time

before = time.time()

def pro1():
    file = open(root.filename, 'r')

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
    for block in q2:
        roll_no = block[:7]
        fin = sub = ()

        sub1 = block[41:44]
        mrk1 = block[45:51].rstrip()
        grd1 = block[51:54].strip()
        sub += (sub1, mrk1, grd1),

        sub2 = block[54:57]
        mrk2 = block[58:64].rstrip()
        grd2 = block[64:67].strip()
        sub += (sub2, mrk2, grd2),

        sub3 = block[67:70]
        mrk3 = block[71:77].rstrip()
        grd3 = block[77:80].strip()
        sub += (sub3, mrk3, grd3),

        sub4 = block[80:83]
        mrk4 = block[84:90].rstrip()
        grd4 = block[90:93].strip()
        sub += (sub4, mrk4, grd4),

        sub5 = block[93:96]
        mrk5 = block[97:103].rstrip()
        grd5 = block[103:109].strip()
        sub += (sub5, mrk5, grd5),

        fin = block[119:133]

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

print('Elapsed time:',after-before)

#eventloop
root.mainloop()