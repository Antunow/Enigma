from tkinter import *
import tkinter.scrolledtext as ScrolledText
okno=Tk(className='ENIGMA')

def wprowadzenie(tekst):

    dic=['A','Ą','B','C','Ć','D','E','Ę','F','G','H','I','J','K','L','Ł','M','N','Ń','O','Ó','P','R','S','Ś','T','U','W','Z','Ż','Ź','Y',' ']
    tekst=tekst.upper()
    wpr=[]
    for i in tekst:
        if i in dic:
            wpr.append(dic.index(i))
    return wpr

def kolo1(test):
    kolo1_out = []
    litera = 0
    obroty=0
    wynik = 0
    litery = ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'U', 'S', 'P', 'A', # len (litery)=32
              'I', 'B', "R", "C", "J",'Ę','Ć','Ó','Ś','Ż','Ź','Ą',"Ł"]
    for i in test:
        litera+=i
        if i == 32:
            kolo1_out.append("X")
        elif litera>=len (litery):
            while litera>=len(litery):
                obroty+=1
                litera-=len(litery)
            kolo1_out.append(litery[litera])
        elif litera < len(litery):
            kolo1_out.append(litery[litera])

    wynik = "".join(kolo1_out)
    return wynik
    #print(test, '\n', wynik)


def kolo2(tekst ):
    kolo2_out = []
    litera = 0
    obroty = 0
    wynik = 0
    litery = ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'U', 'S', 'P', 'A',
              'I', 'B', "R", "C", "J", 'Ę', 'Ć', 'Ó', 'Ś', 'Ż', 'Ź', 'Ą', "Ł",'X']
    litery2 = ['A', 'J', 'D', 'K', 'S' ,'I', 'R', 'U', 'B', 'L' ,'H' ,'W' ,'T' ,'M' ,'C', 'Q', 'G' ,'Z' ,'N', 'P',
              'Y', 'F','V' ,'O' ,'E', 'Ę', 'Ć', 'Ó', 'Ś','X', 'Ż', 'Ź', 'Ą', "Ł"]
    tekst_to_liczby=[]
    for i in tekst:
        if i in litery:
            tekst_to_liczby.append(litery.index(i))#todo do poprawy odnieść sie do wbudowanego alfabetu bład jak na początku nieda się tego rozkodować

    for i in tekst_to_liczby:
        litera += i
        #if i == 33:
        #    kolo2_out.append("X")
        if litera >= len(litery2):
            while litera >= len(litery2):
                obroty += 1
                litera -= len(litery2)
            kolo2_out.append(litery2[litera])
        elif litera < len(litery2):
            kolo2_out.append(litery2[litera])

    wynik = "".join(kolo2_out)
    return wynik


def kolo3(tekst):
    litery2 = ['B', 'D', 'F','Ę', 'Ć', 'Ó', 'Ś', 'Ż', 'Ź', 'Ą', "Ł", 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z',
               'N', 'Y', 'E', 'I', 'W', 'G', 'A','K', 'M', 'U', 'S', 'Q', 'O']
    kolo2_out = []
    litera = 0
    obroty = 0
    wynik = 0
    litery =  ['A', 'J', 'D', 'K', 'S' ,'I', 'R', 'U', 'B', 'L' ,'H' ,'W' ,'T' ,'M' ,'C', 'Q', 'G' ,'Z' ,'N', 'P',
              'Y', 'F','V' ,'O' ,'E', 'Ę', 'Ć', 'Ó', 'Ś','X', 'Ż', 'Ź', 'Ą', "Ł"]

    tekst_to_liczby = []
    for i in tekst:
        if i in litery:
            tekst_to_liczby.append(litery.index(
                i))  # todo do poprawy odnieść sie do wbudowanego alfabetu bład jak na początku nieda się tego rozkodować

    for i in tekst_to_liczby:
        litera += i
        # if i == 33:
        #    kolo2_out.append("X")
        if litera >= len(litery2):
            while litera >= len(litery2):
                obroty += 1
                litera -= len(litery2)
            kolo2_out.append(litery2[litera])
        elif litera < len(litery2):
            kolo2_out.append(litery2[litera])

    wynik = "".join(kolo2_out)
    return wynik


def dekod1(tex):
    litery = ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'U', 'S', 'P', 'A', # len (litery)=32
              'I', 'B', "R", "C", "J",'Ę','Ć','Ó','Ś','Ż','Ź','Ą','Ł']
    dekod=[]
    rozszyfrowanie=[]
    suma=0
    obroty=0
    out=""
    przyrost=0
    loop_counter=0
    for i in tex:
        if i =="X":
            dekod.append(32)
            suma+=32
        elif loop_counter == 0:
            suma += litery.index(i)
            dekod.append(litery.index(i))
            loop_counter += 1
        else:
            if litery.index(i)>=suma:
                przyrost=litery.index(i)-suma
                suma += przyrost #todo wprowadzić syme z poprzedniej wersji albo przyrost
            elif litery.index(i)<suma:
                przyrost = litery.index(i)+ (len(litery)-suma)
                suma+= przyrost

            if suma<=len(litery):
                    dekod.append(przyrost )#zamieszanie z indeksami i literami
            elif suma>len(litery):
                while suma>len(litery):
                    obroty+=1
                    suma-=len(litery)
                dekod.append(przyrost)
    dic1 = ['A','Ą','B','C','Ć','D','E','Ę','F','G','H','I','J','K','L','Ł','M','N','Ń','O','Ó','P','R','S','Ś','T','U',
            'W','Z','Ż','Ź','Y',' ']
    for i in dekod:

        rozszyfrowanie.append(dic1[i])

    out="".join(rozszyfrowanie)
    #print (out)

    return out

def dekod2(tex):
    litery = ['A', 'J', 'D', 'K', 'S' ,'I', 'R', 'U', 'B', 'L' ,'H' ,'W' ,'T' ,'M' ,'C', 'Q', 'G' ,'Z' ,'N', 'P',
              'Y', 'F','V' ,'O' ,'E', 'Ę', 'Ć', 'Ó', 'Ś','X', 'Ż', 'Ź', 'Ą', "Ł"]
    dekod = []
    rozszyfrowanie = []
    suma = 0
    obroty = 0
    out = ""
    przyrost = 0
    loop_counter = 0
    for i in tex:
       # if i == "X":
       #     dekod.append(32)
       #     suma += 32
        if loop_counter == 0:
            suma += litery.index(i)
            dekod.append(litery.index(i))
            loop_counter += 1
        else:
            if litery.index(i) >= suma:
                przyrost = litery.index(i) - suma
                suma += przyrost  # todo wprowadzić syme z poprzedniej wersji albo przyrost
            elif litery.index(i) < suma:
                przyrost = litery.index(i) + (len(litery) - suma)
                suma += przyrost

            if suma <= len(litery):
                dekod.append(przyrost)  # zamieszanie z indeksami i literami
            elif suma > len(litery):
                while suma > len(litery):
                    obroty += 1
                    suma -= len(litery)
                dekod.append(przyrost)
    dic1 = ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'U', 'S', 'P', 'A',
              'I', 'B', "R", "C", "J", 'Ę', 'Ć', 'Ó', 'Ś', 'Ż', 'Ź', 'Ą', "Ł",'X']
    for i in dekod:
        rozszyfrowanie.append(dic1[i])

    out = "".join(rozszyfrowanie)
    # print (out)
    return  out

def dekod3(text):
    litery =['B', 'D', 'F','Ę', 'Ć', 'Ó', 'Ś', 'Ż', 'Ź', 'Ą', "Ł" ,'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z',
               'N', 'Y', 'E', 'I', 'W', 'G', 'A','K', 'M', 'U', 'S', 'Q', 'O']
    dekod = []
    rozszyfrowanie = []
    suma = 0
    obroty = 0
    out = ""
    przyrost = 0
    loop_counter = 0
    for i in text:
        # if i == "X":
        #     dekod.append(32)
        #     suma += 32
        if loop_counter == 0:
            suma += litery.index(i)
            dekod.append(litery.index(i))
            loop_counter += 1
        else:
            if litery.index(i) >= suma:
                przyrost = litery.index(i) - suma
                suma += przyrost  # todo wprowadzić syme z poprzedniej wersji albo przyrost
            elif litery.index(i) < suma:
                przyrost = litery.index(i) + (len(litery) - suma)
                suma += przyrost

            if suma <= len(litery):
                dekod.append(przyrost)  # zamieszanie z indeksami i literami
            elif suma > len(litery):
                while suma > len(litery):
                    obroty += 1
                    suma -= len(litery)
                dekod.append(przyrost)
    dic1 = ['A', 'J', 'D', 'K', 'S' ,'I', 'R', 'U', 'B', 'L' ,'H' ,'W' ,'T' ,'M' ,'C', 'Q', 'G' ,'Z' ,'N', 'P',
              'Y', 'F','V' ,'O' ,'E', 'Ę', 'Ć', 'Ó', 'Ś','X', 'Ż', 'Ź', 'Ą', "Ł"]
    for i in dekod:
        rozszyfrowanie.append(dic1[i])

    out = "".join(rozszyfrowanie)
    # print (out)
    return out

def dekoduj():
    text = t2.get(1.0, END+"-1c" )
   # wynik = dekod1(dekod2(dekod3(text)))
    #dekod1(dekod2(dekod3(kolo3(kolo2(kolo1(wprowadzenie(coś)))))))
    wynik=dekod1(dekod2(dekod3(str(text))))
    t1.delete(1.0,END)
    t1.insert(1.0, wynik)

def zakoduj():
    text = t1.get(1.0,END+"-1c")
    wynik = kolo3(kolo2(kolo1(wprowadzenie(text))))
    t2.delete(1.0, END)
    t2.insert(1.0,wynik)

    #return wynik


l1=Label(okno,text='''Program inspirowany niemiecką maszyną Enigma. 
Obsługuje polskie znaki lecz nie obsługuje liczb i znaków interpunkcyjnych.  
Udanego szyfrowania :)''')



t1=ScrolledText.ScrolledText(okno,width= 50)
t2=ScrolledText.ScrolledText(okno,width= 50)


b1=Button(okno,text='szyfruj',command=zakoduj)
b2=Button(okno,text="rozszyfruj",command=dekoduj)


l1.grid(row=0,column=5,columnspan=6 )


t1.grid(row =1,column=5,rowspan=6)
t2.grid(row = 1,column=6,rowspan=6)

b1.grid(row=7, column=5)
b2.grid(row=7, column=6)



okno.mainloop()

