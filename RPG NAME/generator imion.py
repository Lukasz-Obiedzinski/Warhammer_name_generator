#Generator postaci warhammera zalezny od plci/rasy

__author__="dev"
#importy
import random

#nalezy stworzyc osobne pliki dotyczace imion BN dla kazdego
#
'''
i=0
for i in range(0,12):
    print(i)
    
    with open("cz_meskie.txt", "r") as f:
        im_cz_m=f.readlines()
        losuj_imie=random.choice(im_cz_m)


    with open("cz_meskie2.txt", "r") as f:
        im_cz_m2=f.readlines()
        losuj_imie2=random.choice(im_cz_m2)

    with open("cz_meskie3.txt", "a") as f:
        f.write("{}. {} {}\n".format(i,str.rstrip(losuj_imie),str.rstrip(losuj_imie2)))
    i+=1
f.close

#stworzenie pliku ktory uporzadkuje alfabetycznie tabele

with open("cz_meskie.txt", "r") as f:
    im_cz_m=f.readlines()
    im_cz_m_good=sorted(im_cz_m)
    im_cz_m_good=" ".join(im_cz_m_good)
    with open("cz_meskie4.txt", "w") as f:
        
        f.write(" {:1<}\n".format(str.rstrip(im_cz_m_good)))
        
f.close
'''


#stworzenie nowych imion na bazie pierwszych dwoch liter + niemiecki zaczatek
i=0
for i in range(0,100):
    

    with open("dod1.txt", "r") as f:
        dod1=f.readlines()
        losuj_dod1=sorted(dod1)
        losuj_dod1="".join(losuj_dod1)
        with open("dod1.txt", "w") as f:
            f.write("{}\n".format(str.rstrip(losuj_dod1)))
        f.close


        losuj_dod1=random.choice(dod1)    
             
        with open("dod2.txt", "r") as f:
            dod2=f.readlines()
            losuj_dod2=random.choice(dod2)
        
        with open("im_new.txt", "a") as f:
            f.write("{}{}\n".format(str.rstrip(losuj_dod2),
                                    str.rstrip(losuj_dod1)))
            
        
    f.close
i+=1

with open("im_new.txt", "r") as f:
    im_new=f.readlines()
    im_new=sorted(im_new)
    im_new="".join(im_new)
    with open("im_new.txt", "w") as f:
        f.write("{}\n".format(str.rstrip(im_new)))
    f.close
f.close

## krasnoludzkie rzeczy


with open("dwarf_1_m_name.txt", "r") as f:
    # sortowanie
    line1=f.readlines()
    sort=sorted(line1)
    sort="".join(sort)
    with open("dwarf_1_m_name.txt", "w") as f:
        f.write(sort)
    f.close
    
    i=0
    j=0
    for i in range(0,50):
        with open("dwarf_names_short.txt", "a") as f:
                
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
            if j<8:
                f.write("0{}-0{} : {}{} {}{}son\n".format(j+1,j+2,losuj_1.strip(),
                                          losuj_2.strip(),
                                          losuj_4.strip(),
                                          losuj_6.strip()))
                
            elif j<10:
                f.write("0{}-10 : {}{} {}{}son\n".format(j+1,losuj_1.strip(),
                                          losuj_2.strip(),
                                          losuj_4.strip(),
                                          losuj_6.strip()))
            elif j>=10:
                f.write("{}-{} : {}{} {}{}son\n".format(j+1,j+2,losuj_1.strip(),
                                          losuj_2.strip(),
                                          losuj_4.strip(),
                                          losuj_6.strip()))
                
            
        f.close
        j+=2
       

j=0

with open("dwarf_names_short.txt", "r") as f:
# sortowanie
    line2=f.readlines()
    sort1=sorted(line2)
    sort1="".join(sort1)
    with open("dwarf_names_short.txt", "w") as f:
        f.write(sort1)
       
    f.close

#tworzenie nazwisk 3 czlonowych krasnoludzkich

    for i in range(0,50):
        with open("dwarf_names_long.txt", "a") as f:
                
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
            if j<8:
                f.write("0{}-0{} : {}{} {}{}{}son\n".format(j+1,j+2,losuj_1.strip(),
                                          losuj_2.strip(),
                                          losuj_4.strip(),
                                          losuj_5.strip(),
                                          losuj_6.strip()))
                
            elif j<10:
                f.write("0{}-10 : {}{} {}{}{}son\n".format(j+1,losuj_1.strip(),
                                          losuj_2.strip(),
                                          losuj_4.strip(),
                                          losuj_5.strip(),
                                          losuj_6.strip()))
            elif j>=10:
                f.write("{}-{} : {}{} {}{}{}son\n".format(j+1,j+2,losuj_1.strip(),
                                          losuj_2.strip(),
                                          losuj_4.strip(),
                                          losuj_5.strip(),
                                          losuj_6.strip()))
                
            
        f.close
        j+=2

with open("dwarf_names_long.txt", "r") as f:
# sortowanie
    line2=f.readlines()
    sort1=sorted(line2)
    sort1="".join(sort1)
    with open("dwarf_names_long.txt", "w") as f:
        f.write(sort1)
       
    f.close

f.close


######################################################



    








        

        
        
