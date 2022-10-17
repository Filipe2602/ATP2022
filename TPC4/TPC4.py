#TPC4
import time




cinema=[]



def menu():
    print ("------------------------ Menu ------------------------\n (1) Criar Sala \n (2) Remover Sala \n (3) Filmes em exibição \n (4) Disponibilidade de lugar \n (5) Vender Bilhete \n (6) Informação das salas \n (7) Sair")
  

 

def inserirsala(cinema):
    filme=input("introduza o nome do filme:")
    for s in cinema:
        nlugares, vendidos, nome= s
        if nome==filme:
            print("Filme já existe")
            menu()
    nlugares= int(input("introduza o número de lugares da sala:"))  
    vendidos=[]     
    cinema.append((nlugares, vendidos, filme)) 
    print("Sala criada com sucesso!")  
    print("Salas:", cinema) 
    menu()


def removersala(cinema): 
    index= int(input("introduza o indice da sala:"))   
    cinema.pop(index)
    print("Sala removida com sucesso!")
    print("Salas:",cinema)
    menu()


def listarsalas(cinema):
    print("Sala  Filme") 
    for p in cinema:
        nlugares, vendidos, filme=p 
        print("Sala#{0}".format(cinema.index(p), "", filme))
    time.sleep(1)
    menu()    
     


   
def lugardisponivel(cinema, filme,lugar):
    for p in cinema:
        nlugares, vendidos, nome= p
        if filme==nome:
            if lugar in vendidos:
                res=False
            else:
                res=True
        else:
            res=False
    return res                       
        


def vendebilhete(cinema, filme, lugar):
    if lugardisponivel(cinema,filme,lugar):
        for p in cinema:
            nlugares,vendidos,nome=p
            if filme==nome:
                vendidos.append(lugar)     
        print("lugar vendido com sucesso")  
        print("Salas:", cinema) 
    else:
        print("Lugar indisponuvel") 
    menu()


def listardisponibilidadesala(cinema):
    print("Sala  Filme  Lugares Disponiveis")  
    for p in cinema:
        nlugares, vendidos, filme=p
        print("Sala#{0}".format(cinema.index(p)), "", nlugares - len(vendidos))
    time.sleep(1)
    menu()    









print("Bem Vindo!") 
menu()
Cinema=[]
opc=int(input("Escolha a opção!")) 


 


while opc!=0:
    if opc==1:
        inserirsala(cinema)
        opc=int(input("Escolha a opção!")) 

    if opc==2:
        removersala(cinema)  
        opc=int(input("Escolha a opção!")) 

    if opc==3: 
        listarsalas(cinema)
        opc=int(input("Escolha a opção!")) 

    if opc==4:
        filme= input("Introduza o nome do filme:")
        lugar=int(input("introduza o lugar:"))   
        print("Lugar disponivel?", lugardisponivel(cinema,filme,lugar))
        opc=int(input("Escolha a opção!")) 

    if opc==5:
        filme= input ("Introduza o nome do filme:")    
        lugar=int(input("Introduza o lugar:"))
        vendebilhete(cinema,filme,lugar)
        opc=int(input("Escolha a opção!")) 

    if opc==6:
        listardisponibilidadesala(cinema)  
        opc=int(input("Escolha a opção!"))   

if opc==0:
    print("Até à próxima!")        
    