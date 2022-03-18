import csv
import projetPython_reset_Fonction  as pf
import colorama
from colorama import Fore
from colorama import Style
colorama.init()

with open('/home/ridialsa/Bureau/sa/python/projet1/datat.tsv') as f:
    file=csv.reader(f, delimiter='\t')
    data=list(file)
    head=data.pop(0)

    for m in range(len(data)-1):
        mtr=data[m][-1]
        mtr=mtr.replace('Francais','Fr')
        mtr=mtr.replace('FRANCAIS','Fr')
        mtr=mtr.replace('Francais', 'Fr')
        mtr=mtr.replace('FRANÇAIS','Fr')
        mtr=mtr.replace('Français', 'Fr')
        mtr=mtr.replace('ANGLAIS', 'Anglais')
        mtr=mtr.replace('Science_Physique', 'Pc')
        mtr = mtr.replace('PC', 'Pc')
        mtr=mtr.replace('Math', 'Maths')
        mtr=mtr.replace('MATH', 'Maths')
        data[m][-1]=mtr

table=[]
for row in data:
    tab=dict(zip(head[1:],row[1:]))
    table.append(tab)

liste=pf.typeSeparateur(table)
i=0
validedListe=[]
unvalidedListe=[]
listNum=[]
for line in table:
 if  (pf.splitingDate(line,liste) and pf.validNumero(line) and pf.validClasse(line) and pf.validPren(line,'Prénom') and pf.validPren(line,'Nom') and pf.validNote(line)):
    if line['Numero'] not in listNum:
        validedListe.append(line)
        listNum.append(line['Numero'])
 else:
     unvalidedListe.append(line)

def myFunction(line):
    return line["Note"]["MoyenneG"]

"""print('\n', ' '*28,'_'*30)
print(Fore.LIGHTGREEN_EX + Style.BRIGHT +  ' '*31,'_'*10,'MENU','_'*10,'' + Style.RESET_ALL)
print(' '*29,'_'*30,'\n')
print(Fore.LIGHTGREEN_EX + Style.BRIGHT +' '*10,'OPTION 1 : Afficher les n premier lignes valides')
print(Fore.LIGHTGREEN_EX, ' '*10,'OPTION 2 : Afficher les n premier lignes non valides'+ Style.RESET_ALL)
print(Fore.LIGHTGREEN_EX, ' '*10,'OPTION 3 : Afficher une ligne par son numero'+ Style.RESET_ALL)

y=int(input('___:'))
while (y!=1 and y!=2 and y!=3):
    print(Fore.LIGHTRED_EX + Style.BRIGHT + ' ' * 10, 'Option Invalide !!!!'+ Style.RESET_ALL)
    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + ' ' * 10, 'press 1: n first valide , 2: n last valide, 3 : appeler une ligne par son numero'+ Style.RESET_ALL)
    y = int(input(Fore.LIGHTGREEN_EX +'choice ___:'+ Style.RESET_ALL))

if y==3:
    x=input(Fore.LIGHTMAGENTA_EX + 'Donner le numéro' + Style.RESET_ALL)
    for row in validedListe:
        ok=False
        if row['Numero']==x:
            print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + ' ' * 3, '| ', '  Numero   |', '    Nom      |',
                  '   Prénom    |',
                  '   Classe    |', '    Birth Day    |', '   Moyenne   |' + Style.RESET_ALL)
            print(Fore.LIGHTBLUE_EX + Style.BRIGHT + '\n')
            pf.affiche(row)
            ok=True
            break
    if not ok: print(Fore.RED + 'cette ligne n\'est pas valide')
elif y==1:
    validedListe.sort(key=myFunction)
else:
    validedListe.sort(reverse=True,key=myFunction)

i=0
if y!=3:

    print(' ' * 10, ' Donner le nombre de ligne à afficher :)')
    x = int(input('___: '))
    print(Fore.BLUE +'' )
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + ' ' * 3, '| ', '  Numero   |', '    Nom      |', '   Prénom    |',
          '   Classe    |', '    Birth Day    |', '   Moyenne   |' + Style.RESET_ALL)
    for rows in validedListe:
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT +'\n')
        pf.affiche(rows)
        i+=1
        if i==x: break"""

