# need to execute this: pip install xmltodict 
import json, xmltodict, yaml, csv, os
from dict2xml import dict2xml
# xml to dict
def xmlToDict(filePath):
    with open(filePath,'r') as f:
        data=f.read()
        obj=xmltodict.parse(data)
    return obj
#jason to dict
def jsonToDict(filePath):
    with open(filePath) as f:
        data=json.load(f)
    return data

# YAML to dictionnary
def yamlToDict(filePath):
    with open(filePath) as f:
        reader=yaml.load(f)
    return reader
# from csv to dict
def csvToDict(filePath): 
    with open(filePath) as f:
        data=csv.DictReader(f,delimiter=';')
    return data

# from dict to xml
def newXmlFile(dict):
    with open("xmlData.xml",'w') as f:
        writing=dict2xml(dict)
        f.write(writing)

# function dictionary to csv file
def newCsvFile(dict):
    heads=[]
    for keys in dict:
        heads.append(keys)
    with open("myCsvData.csv",'w') as f:
        mywriter= csv.DictWriter(f, fieldnames=heads)
        mywriter.writeheader()
        mywriter.writerow(dict)

### création d'un fichier json et ajout d'element
def newJasonFile(dict):
    with open("jsonData.json",'a') as f:
        json.dump(dict,f)
        f.write(os.linesep)

### création de fichier yaml et ajout élément
def newYamlFile(dict):
    with open("yamlData.yaml",'a') as f:
        yaml.dump(dict, f)
        f.write(os.linesep)



### Création d'un interface un fichier avec la bonne extension
from tkinter import *
from tkinter.filedialog import askopenfilename
from pathlib import PureWindowsPath
print('\n\n')
def Opening():
    myDirector = askopenfilename(title="Ouvrir un fichier", initialdir=r"/home/ridialsa/",
                                           filetypes=(("xml Files", "*.xml"),
                                                      ("json Files", "*.json"),
                                                      ("csv Files", "*.csv"),
                                                      ("YAML Files", "*.yaml")))

    return PureWindowsPath(myDirector)

root = Tk()
root.geometry('200x100')

path=Opening()
paths=path.parents[0]
op=path.name
path=str(path).replace("\\","/")

extensions=["csv","json","xml","yaml"]
ext=op.split('.')[-1]

#print(f"nom file: {op}, extension: {ext}")
choice="0"
choices=["1", "2", "3", "4"]
print(" "*10, "#"*5," "*5,"quelle type de document voulez-vous créer ???", " "*5, "#"*5)
while(choice not in choices):
    if (ext=="csv"):
        print("2 pour xml")
        print("3 pour json")
        print("4 pour yaml")
        choices=["2", "3", "4"]
    elif (ext=="xml") :
        print("1 pour csv")
        print("3 pour json")
        print("4 pour yaml")
        choices=["1", "3", "4"]
    elif (ext=="json"):
        print("1 pour csv")
        print("2 pour xml")
        print("4 pour yaml")
        choices=["1", "2", "4"]
    else:
        print("1 pour csv")
        print("2 pour xml")
        print("3 pour json")
        choices=["1", "2", "3"]
    choice=input("choice : ")
choice=int(choice)
                            #################   Fin interface ####################

if (ext=="csv"): dict=csvToDict(path)
elif (ext=="json"): dict=jsonToDict(path)
elif (ext=="xml"): dict=xmlToDict(path)
else: dict=yamlToDict(path)

if choice==1:
    newCsvFile(dict)
elif choice==2:
    newXmlFile(dict)
elif choice==3:
    newJasonFile(dict)
else:
    newYamlFile(dict)



print(" "*10, "#"*5," "*5," Fichier ",choice, "crée dans le meme emplacement ", " "*5, "#"*5)
