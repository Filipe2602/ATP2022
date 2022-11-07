import aula
aluno=aula.leAlunos("alunos.csv")
aluno1=aula.medAlunos(aluno)
aluno2= aula.escaAlunos(aluno1)       

def menu():
 print (f"| {'Menu':=^30} |")
 print(f"| {'(1) Ler informação ':30} {'|':30} \n|{' (2) Alunos por curso':30}  {'|':30} \n|{' (3) Média de notas':30}  {'|':30} \n|{' (4) Escalões':30}  {'|':30} \n|{' (5) Escalões por alunos':30}  {'|':30} \n|{' (6) Gráfico':30}  {'|':30} \n|{' (7) Tabela':30}  {'|':30} \n|{' (0) Sair':30}  {'|':30}")
 print (f"| {'':=^30} |")
 opc=int(input("Escolha a opção"))
 while opc != 0:
    if opc==1:
        
        opc=int(input("Escolha a opção"))
    if opc==2:
        aula.distAlunos(aluno)    
        opc=int(input("Escolha a opção"))
    if opc==3:
        aula.medAlunos(aluno)
        opc=int(input("Escolha a opção"))
    if opc==4:
        aula.escaAlunos(aluno1)
        opc=int(input("Escolha a opção"))
    if opc==5:
        aula.distEsc(aluno2)    
        opc=int(input("Escolha a opção"))
    if opc==6:
        aula.distGrafico(aluno2) 
        opc=int(input("Escolha a opção"))
    if opc==7:
        aula.distTabela(aluno2)      
        opc=int(input("Escolha a opção")) 
 if opc==0:
    print(f"| {'Até à Próxima':=^30} |")       


