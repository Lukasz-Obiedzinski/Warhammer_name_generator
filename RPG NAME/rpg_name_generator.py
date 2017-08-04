__author__='dev'

## krasnoludzkie rzeczy

import random

with open("dwarf_1_m_name.txt", "r") as f:
    # sortowanie
    line1=f.readlines()
    sort=sorted(line1)
    sort="".join(sort)
    with open("dwarf_1_m_name.txt", "w") as f:
        f.write(sort)
    f.close
    i=0
    for i in range(0,10):
        with open("dwarf_names.txt", "a") as f:
            
            #losowanie 1 i 2 czlonu imienia
            losuj_1=random.choice(line1)

            losuj_2=random.choice(line1)
            losuj_2=str.lower(losuj_2)

            losuj_3=random.choice(line1)
            losuj_3=str.lower(losuj_3)

            losuj_4=random.choice(line1)

            losuj_5=random.choice(line1)
            losuj_5=str.lower(losuj_5)

            losuj_6=random.choice(line1)
            losuj_6=str.lower(losuj_6)

            #tworzenie imienia
            f.write("{}{} {}{}son\n".format(losuj_1.strip(),
                                      losuj_2.strip(),
                                      losuj_4.strip(),
                                      losuj_6.strip()))
            
        f.close
        i+=1
with open("dwarf_names.txt", "r") as f:
# sortowanie
    line2=f.readlines()
    sort1=sorted(line2)
    sort1="".join(sort1)
    with open("dwarf_names.txt", "w") as f:
        f.write(sort1)
    f.close

f.close







