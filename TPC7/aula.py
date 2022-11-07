import csv
import matplotlib.pyplot as plt

def leAlunos(filename):
    file=open(filename, encoding="UTF8")
    file.readline()
    csv_file = csv.reader(file,delimiter=",")
    lista=[]
    for alunos in csv_file:
        lista.append(tuple(alunos))

    return(lista)   

aluno=leAlunos("alunos.csv")


def distAlunos(aluno):   
    dici={}
    for _,_,cursop,*_ in aluno:
        if cursop in dici:
         dici[cursop]+=1
        else:
         dici[cursop]=1
      
       
    return dici          


def medAlunos(aluno):
    novalista=[]


    for id,nome,curso,tpc1,tpc2,tpc3,tpc4 in aluno:
        x=int(tpc1)+int(tpc2)+int(tpc3)+int(tpc4)
        media=int(x/4)
        tuplo=(id,nome,curso,tpc1,tpc2,tpc3,tpc4,media)
        novalista.append(tuplo)  
  
    
    return novalista
    
aluno1=medAlunos(aluno)
   

def escaAlunos(aluno1):
    escalao=()
    novalista1=[]
    for id,nome,curso,tpc1,tpc2,tpc3,tpc4,media in aluno1:
        if media>=1 and media <=4:
            escalao=("E")
        if media>=5 and media <=8:
            escalao=("D")
        if media>=9 and media <=12:
            escalao=("C")
        if media>=13 and media <=16:
            escalao=("B")
        if media>=17 and media <=20:
            escalao=("A")
        tuplo=(id,nome,curso,tpc1,tpc2,tpc3,tpc4,media,escalao)   
        novalista1.append(tuplo)       

    return novalista1    

aluno2= escaAlunos(aluno1)    


def distEsc(aluno2):
    dici={}
    for _,_,_,_,_,_,_,_,escalao in aluno2:
        if escalao in dici:
            dici[escalao]+=1
        else:
            dici[escalao]=1    
    return dici    


def distGrafico(aluno2):
    dici={}
    for _,_,_,_,_,_,_,_,escalao in aluno2:
        if escalao in dici:
            dici[escalao]+=1
        else:
            dici[escalao]=1

        y=dici.values()
        x=dici.keys()
        
    plt.plot (x,y)   
    plt.xlabel("Escalão")
    plt.ylabel("Número de alunos")
    plt.show()

def distTabela(aluno2):
    dici={}
    for _,_,cursop,*_ in aluno2:
        if cursop in dici:
         dici[cursop]+=1
        else:
         dici[cursop]=1

    n=0
    p=list(dici.keys())
    d=list(dici.values())
    print(f"|{'Curso:':20}|{'Número de alunos no curso:':10}|")
    
    while n<len(dici):
       print(f"|{str(p[n]):20}|{str(d[n]):26}|")
       n=n+1
    
      


       



