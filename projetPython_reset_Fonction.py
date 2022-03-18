import datetime

def validPren(dicts,columname):
    validity=True
    if columname=='Prénom':
        n=3
    else:
        n=2
    if dicts[columname].isalpha():
        i=0
        for el in dicts[columname]:
            if el.isalpha():
                i+=1
        if i<n:
            validity=False
    else:
        validity=False
    return validity
#### gestion des note
## si la note ne contient pas 3, 4,5 ou ou qu'il ne contient pas pas A ou B, on renvoi False
### si c'est le cas , on change le format de la note eexple '5èmeB' et renvoi True
num=["3","4","5","6"]
def validClasse(line):
    row=line["Classe"]
    valide=False
    valide1=valide2=False
    if "A"  in row :
        valide1=True
        c="A"
    elif "B" in row:
        valide1=True
        c="B"
    for i in num:
        if i in row:
            valide2=True
            j=i
    if valide1 and valide2:
        valide = True
        line["Classe"]=j+"ème"+c
    return valide
####### traitement des numero
def validNumero(line):
    row = line['Numero']
    valide=False
    if len(row)==7 and row.isalnum():
        if  not row.isalpha():
            valide=True
        j=0
        for i in row:
            if not i.isalpha(): j+=1
        if j==len(row):valide=  False
    return valide
###### traitement des dates
    #### énumeré les different type de separateur de notre dataset
def typeSeparateur(table):
    listeChar=[]
    for tab in table:
        for element in tab["Date de naissance"]:
            if not element.isalnum():
                listeChar.append(element)
    listeChar=list(set(listeChar))
    return listeChar

    ### validation date de naissance

def splitingDate(line,liste):
    valide = True
    row = line["Date de naissance"]
    if row and type(row) == str:
        for sep in liste:
            if sep in row:
                row = row.split(sep)
                break

        if row[1] in ['janv.', 'janvier']: row[1] = '1'
        if row[1] in ['mars', '-03']: row[1] = '3'
        if row[1] == 'avr.': row[1] = '4'
        if row[1] in ['mai', '-05', '5']: row[1] = '5'
        if row[1] in ['juin', '06']: row[1] = '6'
        if row[1] == 'juillet': row[1] = '7'
        if row[1]=='août':row[1]='8'
        if row[1] in ['septembre', '9', 'sept.']: row[1] = '9'
        if row[1] == 'octobre': row[1] = '10'
        if row[1] == 'novembre': row[1] = '11'
        if row[1] == 'decembre': row[1] = '12'




        if row[0].isnumeric() and row[1].isnumeric() and row[2].isnumeric():
            row = [int(el) for el in row]
            try:
                row = datetime.date(row[2], row[1], row[0])
            except ValueError:
                valide = False
        else:
            valide = False


    line["Date de naissance"] = row
    return valide

#### traitement des notes
def validNote(line):
    note=line["Note"]
    valide=True
    if  type(note)==str:
        try:
            MoyenneG=0
            note=note.replace(' ','')
            note=note.split('#')
            for i in range(len(note)):
                matiere=note[i]
                matiere=matiere.split("[")
                matiere[1]=(matiere[1].split("]"))[0]
                note[i]=matiere
            #créer un dictionnate matiere: note
            d={}
            for i in note:
                d.setdefault(i[0],i[1])
            note=d
            ###separation devoir et examen
            for i in note:
                l=note[i]
                l=l.split(':')
                if len(l)==1:
                    l.append('0')
                elif not l[1] :
                    l[1]='0'
                l[0]=l[0].split(';')
                l[0]=[float(i) for i in l[0]]
                l[1]=float(l[1])
                """for n in line[0]:
                    if n>20 or n<0: valide=False
                if line[1]>20 or line[1]<0: valide=False"""
                Moyenne=round((sum(l[0])/len(l[0]) +2*l[1])/3,2)
                MoyenneG+=Moyenne
                liste=["Devoir","Examen"]
                d={"Devoir":l[0],'Examen':l[1], "Moyenne":Moyenne}

                note[i]=d
            MoyenneG=round(MoyenneG/len(note),2)
            note["MoyenneG"]=MoyenneG
            line["Note"]=note
        except:
            valide=False
        if MoyenneG<0 or MoyenneG> 20: valide=False
    return valide

### nbre d'espace sur les print
def espace(n):
    n=str(n)
    esp=(10-len(n))//2
    if  (10-len(n))%2==0:
        return [esp,esp]
    else:
        return [esp, esp+1]
def affiche(row):
    nam=espace(row['Nom'])
    pren=espace(row['Prénom'])
    classe=espace(row['Classe'])
    moy=espace(row['Note']['MoyenneG'])


    print(' '*3, '|', ' ', row['Numero'], ' ', '|',
          ' '*nam[0],row['Nom'], ' '*nam[1],'|',
          ' '*pren[0],row['Prénom'],' '*pren[1],'|',
          ' '*classe[0],row['Classe'],' '*classe[1],'|',
          ' '*2,row['Date de naissance'],' '*2,'|',
          ' '*moy[0],row['Note']['MoyenneG'],' '*moy[1],'|')