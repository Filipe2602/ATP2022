import csv

import matplotlib.pyplot as plt





def leObras(filename):
    file=open(filename, encoding="UTF8")
    file.readline()
    csv_file = csv.reader(file,delimiter=";")

    lista=[]
    for obras in csv_file:
        lista.append(tuple(obras))
    
    return(lista)
    



def tamanhoObras(obras):
    return len(obras)


def imprime(obras):
    print(f"{'|Nome':20}|  {'Descricao':25}|   {'Ano':8}|  {'compositor':15}|") 
    for nome,desc,ano,_,comp,*_ in obras:
        print(f"|{nome[:20]:20}|  {desc[:25]:25}|   {ano:8}|  {comp[:15]:15}|")     

def ordem(tuplo):
    return tuplo[0]

def ordem1(tuplo):
    return tuplo[1] 

def titAno(obras):
    lista=[]
    for nome,_ , ano, *_ in obras:
        lista.append((nome,ano))

    lista.sort(key=ordem) 
    return (lista)   


def nomeano(obras):
    lista=[]
    for nome,_,ano,*_ in obras:
        lista.append((nome,ano))

    lista.sort(key=ordem1)  
    return (lista)  



def titporAno(obras):
    dici= {} 
    for nome,_, ano, *_ in obras:
        if ano in dici.keys():
            dici[ano].append(nome)
        else:
            dici[ano] = [nome]   
    return dici 


def compOrd(obras):
    nomes=[]
    for _,_,_,_,compositor,*_ in obras:
        if compositor not in nomes:
            nomes.append(compositor)

    nomes.sort()
    
    print(nomes)
    


def distPeriodo(obras):
    dici= {}
    for _,_,_,periodo,*_ in obras:
        if periodo in dici.keys():
            dici[periodo]+=1
        else:    
            dici[periodo] = 1
    return dici        


def distAno(obras):
    dici= {}
    for _,_,ano,*_ in obras:
        if ano in dici.keys():
            dici[ano]+=1
        else:
            dici[ano] = 1
    
    
    
        print("Há {} compositores do ano {}".format (dici[ano],ano))



def distComp(obras):   
    dici={}
    for _,_,_,_,compositor,*_ in obras:  
        if compositor in dici.keys():
            dici[compositor]+=1
        else:
            dici[compositor]=1    

        print("Há {} obras feitas por {}".format(dici[compositor],compositor))        
        

def grafico(obras):
    n=int(input("Indique o gráfico que pretende: \n (1) Periodo \n (2) Ano \n (3) Compositor"))

    
    dici={}
    if n==1:
        for _,_,_,periodo,*_ in obras:
          if periodo in dici.keys():
            dici[periodo]+=1
          else:    
            dici[periodo] = 1
           

    elif n==2:
        for _,_,ano,*_ in obras:
          if ano in dici.keys():
            dici[ano]+=1
          else:
            dici[ano] = 1

    elif n ==3:
        for _,_,ano,*_ in obras:
          if ano in dici.keys():
            dici[ano]+=1
          else:
            dici[ano] = 1



    plt.bar(dici.keys(), dici.values())
    plt.show()



def obracomp(obras):
    dici={}
    
    
    for nome,_,_,_,compositor,*_ in obras:
      if compositor not in dici:
        lista=[nome]
        dici[compositor]=lista
      else:
        lista.append(nome)
        dici[compositor]=lista

   

            
       
    return dici



def tabela(obras):
    
    print(f"{ 'Compositor:':31}|{'Nome da Obra:':100}|")
    
    dici={}
    lista=[]
    
    
    for nome,_,_,_,compositor,*_ in obras:
        if compositor not in dici:
            lista=[nome]
            dici[compositor]=lista
        else:
            lista.append(nome)
            dici[compositor]=lista

        
          
              
        
    n=0    
    t=len(dici)     
    p=list(dici.keys())
    d=list(dici.values())
    while t>0:
     print(f"|{str(p[n]):30}|{str(d[n]):100}| ") 
     n=n+1
     t=t-1
    

        

      
        


 

    
    

    

       

  
   
    
 











 
       
   



    







 


