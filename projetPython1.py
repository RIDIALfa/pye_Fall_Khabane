#!/usr/bin/env python
# coding: utf-8

# ### PREHEMBULE

# In[4]:


import os


# In[5]:


import os


# In[6]:


os.chdir("/home/ridialsa/Bureau/sa/python/projet1")


# In[37]:


import csv


# In[45]:


with open('datat.tsv') as f:
    data=csv.reader(f, delimiter="\t")
    line=list(data)
    head=line[0] # recuperer les entetes    


# In[47]:


#ERREUR_PREN_PREMIERLETTRE
#ERREUR_PREN_NBLETTRE


# ### DEBUT

# In[52]:


table=[]
line.pop(0) # suprimer la ligne entete
for l in line:
    tab=dict(zip(head[1:],l[1:]))
    table.append(tab)


# In[60]:


# tester
table[83]


# In[61]:


# remplacer les "," par des "."         
i=0
for l in table: 
        l["Note"]=l["Note"].replace(",",".")
    


# In[62]:


# tester
table[83]


# ### APPLICATION SUR LES NOTES

# In[63]:


# disparsing des notes par matière
for element in table:
    element["Note"]= element["Note"].split("#")
     


# In[67]:


# fonction pour recuperer les notes
def matiere(note):
    note=note.split("[") # separer noms matières et notes
    note[1]=(note[1].split("]"))[0] # eliminater caractere ']' qui gène
    return note
    
    
matiere("Math[11;13:06]") #test de la fonction


# In[69]:


#essai
for tab in table:
        f = []
        for note in tab['Note']:
            note = matiere(note)
            f.append(note)
        tab['Note'] = f


# In[71]:


# transformation ['Math', '04;13:05'] ==> 'Math':'04;13:05'
for element in table:
    d={}
    for i in element["Note"]:
        d.setdefault(i[0],i[1])
    element["Note"]=d
    


# In[73]:


for element in table:
    for ele in element["Note"]:
        element["Note"][ele]=element["Note"][ele].split(":") # separer les devoirs et la composition
        


# In[83]:


# alouer la note "0" à ceux qui n'ont pas fait de composition
for element in table:
    for notes,vnotes in element["Note"].items():
        if len(vnotes)==1:
            vnotes.append("0")
       


# In[105]:


for element in table:
    for ele,val in element["Note"].items():
        ele=ele.split()
        if type(val[0])!=list:
            val[0]=val[0].split(";") #séparer les devoirs ['12','18']
            


# In[110]:


# 
listed=["Devoir","Composition"]
moyenneG=0
for element in table:
    for ele,val in element["Note"].items():
        d={k:v for k,v in zip(listed,val) }  # les mettre en dictionnaire : { DEVOIR: ['12','18'], COMPSITION: '15' }
        d["Devoir"]=[float(l) for l in d["Devoir"]]    
        d["Composition"]=float(d["Composition"])
        moy=(sum(d["Devoir"])/len(d["Devoir"])+2*d["Composition"])/3
        d.setdefault("Moyenne",moy)
        tab["Note"][ele]=d
        moyenneG+=moy     
    element["Note"].setdefault("MoyenneGen",moyenneG/len(tab["Note"]))  


# In[111]:


table[0]["Note"]


# In[ ]:


for element in table:
    for ele,val in element["Note"].items():
        


# ### APPLICATION DATE

# In[23]:


# recuperer les differentes types de separations des dates
listeChar=[]
for tab in table:
    for element in tab["Date de naissance"]:
        if not element.isalnum():
            listeChar.append(element)
listeChar=list(set(listeChar))


# In[24]:


# split sur les dates
for tab in table:
    for i in tab["Date de naissance"]:
        if i in listeChar:
            if type(tab["Date de naissance"])!=list:   # eviter d spliter ceux qui l'ont déjà été
                tab["Date de naissance"]=tab["Date de naissance"].split(i)
   # print(tab["Date de naissance"])  


# In[25]:


# recuperer les jours non entier
#for tab in table:
 #   for elementJour in tab["Date de naissance"][0]:
       # if not elementJour.isnumeric(): print(tab["Date de naissance"][0])


# In[26]:


# mois non valid
jour,mois,an=[],[],[]
for tab in table:
    if tab["Date de naissance"] :
        if not (tab["Date de naissance"][1]).isnumeric() :
            mois.append(tab["Date de naissance"][1])
        if  not (tab["Date de naissance"][0]).isalnum():
            jour.append(tab["Date de naissance"][0])
        if  not (tab["Date de naissance"][2]).isalnum():
            jour.append(tab["Date de naissance"][2])
        
        


# In[27]:


#conda config --set auto_activate_base False


# ### APPLIQUER SUR NUMERO

# In[28]:


for tab in table :
    if len(tab["Numero"])==7:
        if tab["Numero"].isalnum() :
            for i in tab["Numero"]:
                if i.isalpha(): i=i.upper()
        else: ERREUR_NUM_TYPE=True
    else: ERREUR_NUM_TAIL=True  


# ### APPLIQUER SUR PRENOM

# In[29]:


for tab in table:
    if tab["Prénom"][0].isalpha():
        i=0
        for el in tab["Prénom"]:
            if el.isalpha(): i+=1
        if i<3: 
            ERREUR_PREN_NBLETTRE=True
            #print(ERREUR_PREN_NBLETTRE)
       # else: print(tab["Prénom"])
        
    else: 
        ERREUR_PREN_PREMIERLETTRE=True
        #print(ERREUR_PREN_PREMIERLETTRE)


# ### APPLIQUER SUR NOM

# In[30]:


for tab in table:
    if tab["Nom"][0].isalpha():
        i=0
        for el in tab["Prénom"]:
            if el.isalpha(): i+=1
        if i<2: 
            ERREUR_NOM_NBLETTRE=True
            #print(ERREUR_PREN_NBLETTRE)
       # else: print(tab["Prénom"])
        
    else: 
        ERREUR_NOM_PREMIERLETTRE=True
        #print(ERREUR_PREN_PREMIERLETTRE)


# ### POUR LES CLASSES

# In[31]:


num=["3","4","5","6"]
for tab in table:
    c=0
    #if "A" not in tab["Classe"] and "B" not in tab["Classe"]:
     #   print(tab["Classe"])
    if "3" not in tab["Classe"] and "4" not in tab["Classe"] and "5" not in tab["Classe"] and "6" not in tab["Classe"]:
        print(tab["Classe"])
    


# In[32]:


table[200]


# In[33]:


ta=[{'Numero': 'IHFK34G',
 'Nom': 'DIOUM',
 'Prénom': 'Harry',
 'Date de naissance': ['14', 'janv.', '95'],
 'Classe': '5e A',
 'Note': {'SVT': ['12;19;01', '04'],
  'HG': ['15', '11'],
  'Math': ['12;14.5;11', '13'],
  'Francais': ['18;11', '10'],
  'Anglais': ['17.5', '15'],
  'PC': ['3;15', '9']}},{'Numero': 'IHFK34G',
 'Nom': 'DIOUM',
 'Prénom': 'Harry',
 'Date de naissance': ['14', 'janv.', '95'],
 'Classe': '5e A',
 'Note': {'SVT': ['12;19;01', '04'],
  'HG': ['15', '11'],
  'Math': ['12;14.5;11', '13'],
  'Francais': ['18;11', '10'],
  'Anglais': ['17.5', '15'],
  'PC': ['3;15', '9']}}]


# In[34]:


ta[0]


# In[ ]:





# In[ ]:




