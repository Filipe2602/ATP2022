import aula6_2
obras=aula6_2.leObras("obras.csv")

def menu(obras):
    print("---------Menu--------- \n (1) Ler informação \n (2) Quantas obras existem? \n (3) Tabela \n (4) Ordenar por titulo \n (5) Ordenar por ano \n (6) Compositores \n (7) Obras por periodo \n (8) Obras por ano \n (9) Obras por compositor \n (10) Gráfico \n (11) Obras por compositor")
    opc=int(input("Escolha um opção"))

    while opc !=0:
        if opc==1:
            aula6_2.leObras("obras.csv")
            opc=int(input("Escolha uma opção"))

        if opc==2:
            aula6_2.tamanhoObras(obras)
            opc=int(input("Escolha uma opção"))

        if opc==3:
            aula6_2.imprime(obras)
            opc=int(input("Escolha uma opção"))

        if opc==4:
            aula6_2.titAno(obras)
            opc=int(input("Escolha uma opção"))   

        if opc==5:
            aula6_2.nomeano(obras)
            opc=int(input("Escolha uma opção"))  

        if opc==6:
            aula6_2.compOrd(obras)
            opc=int(input("Escolha uma opção"))  

        if opc==7:
            aula6_2.distPeriodo(obras)
            opc=int(input("Escolha uma opção"))  

        if opc==8:
            aula6_2.distAno(obras)
            opc=int(input("Escolha uma opção")) 

        if opc==9:
            aula6_2.distComp(obras)
            opc=int(input("Escolha uma opção")) 

        if opc==10:
            aula6_2.grafico(obras)
            opc=int(input("Escolha uma opção"))

        if opc==11:
            aula6_2.tabela(obras)
            opc=int(input("Escolha uma opção"))

    if opc==0:
        print("Até à Próxima")