import re

i=0
motif = re.compile(r'[^a-zA-Z0-9 ,\'\"\n/\*@=!_;`\-\.\(\)\\:\?\+&<>\[\]]')
with open("catalogue.sql","r",encoding="utf-8") as file:
    for line in file:
        found=motif.findall(line)
        if found:
            i+=1
            print(found,end=" ")
print(f"\n{i} lignes concernées")


motif = re.compile(r'INSERT INTO `catalogue`.*VALUES \(\'(.*?)\'')
with open("catalogue.sql","r",encoding="utf-8") as file:
    for line in file:
        found=motif.search(line)
        if found:
            print(found.group(1),end="\n")


motif = re.compile(r'INSERT INTO `catalogue`.*VALUES \(\'(.*)\'')
with open("catalogue.sql","r",encoding="utf-8") as file:
    for line in file:
        found=motif.search(line)
        if found:
            print(found.group(1),end="\n")

s="""INSERT INTO `catalogue` (`auteur`, `titre`, `collection`, `numcoll`, `editeur`, `date`, `isbn`, `ams`, `cle`, `cote`, `inventaire`, `type`, `lang`, `lango`, `numfiche`) VALUES ('Allain  M.F.  ','An introduction to stochastic differential equations','',0,'Univ.Copernic, Torun, Pologne',1981,'','60-02','EDS','60ALL81','0001','M','eng','',1)"""

motif=re.compile(r'INSERT INTO `catalogue`.*VALUES \(\'(.*)\'')
found=motif.search(s)
found.group(1)
found.group(2) # naffiche rien car il faut 2 groupes de paranthéses ici: VALUES \(\'(.*)\'')

found=motif.search(s)
found
found.group()
found.group(1)


commentaire1 = re.compile(r'/\*!.*?\*/')
commentaire2 = re.compile(r'^--.*')
blancs = re.compile(r'^\s*(.*)\s*$')
noop = re.compile(r'^;$')
with open("catalogue.sql","r",encoding="utf-8") as file:
    for line in file:
        line = commentaire1.sub(r'',line)
        line = commentaire2.sub(r'',line)
        line = blancs.sub(r'\1',line)
        line = noop.sub(r'',line)
        if len(line)>0:
            print(line)


from pprint import pprint as pp

cata = []
filter = re.compile(r'^INSERT INTO.*VALUES \((.*)\);')
sep = re.compile(r'[\',]+')
with open("/users/jaclin/catalogue.sql","r",encoding="utf-8") as file:
    for line in file:
        found=filter.search(line)
        if found:
            sub = found.group(1)
            cata.append(sep.split(sub))
pp(cata)
