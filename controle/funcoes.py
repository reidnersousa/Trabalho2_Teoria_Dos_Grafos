import networkx as nx

def opcoes(o):
    #print("Digite 1 para escolha o grafo 1")
    #print("Digite 2 para escolha o grafo 2")
    #print("Digite 3 para escolha o grafo 3")
    #print("Digite 4 para escolha o grafo 4")
    #print("Digite 5 para escolha o grafo 5")
    return escolha_Arquivo(o)

def escolha_Arquivo(escolha):
    
    switcher ={
        1:"https://raw.githubusercontent.com/reidnersousa/IFB-Teoria_dos_Grafos/main/trabalho2/arquivo_de_Entrada/trab2grafo_1.txt",
        2:"https://raw.githubusercontent.com/reidnersousa/IFB-Teoria_dos_Grafos/main/trabalho2/arquivo_de_Entrada/trab2grafo_2.txt",
        3:"https://raw.githubusercontent.com/reidnersousa/IFB-Teoria_dos_Grafos/main/trabalho2/arquivo_de_Entrada/trab2grafo_3.txt",
        4:"https://raw.githubusercontent.com/reidnersousa/IFB-Teoria_dos_Grafos/main/trabalho2/arquivo_de_Entrada/trab2grafo_4.txt",
        5:"https://raw.githubusercontent.com/reidnersousa/IFB-Teoria_dos_Grafos/main/trabalho2/arquivo_de_Entrada/trab2grafo_5.txt"
    }

    return switcher.get(escolha,"escolha invalida")


def TransformaNPEmLista(arrayDi):
    l=[]
    #Numero_de_linhas=46824
    
    ListaNP =list(arrayDi)
    ultimo=ListaNP[-1]                      ## 11616 29809
    ultimoIndex=ListaNP.index(ultimo)
    #print("ultimo elemento",ultimo,"p",ultimoIndex)
    Numero_de_linhas =int(ultimoIndex)+1    ##  ultimo Index = 46824 +1
    
    for i in range(1,Numero_de_linhas):
        #print(arrayDi[i])
        string = str(arrayDi[i])
        #print(string)
        lista = string.split()
        l.append(lista)
    return l



def Criar_Vertice_Aresta(ll):
   
    E={}
    lista_Aux=[]
    lista_Aux2=[]
    for i in range(len(ll)):
        
        ll[i][2]=int(ll[i][2])
        lista_Aux.append(ll[i][0])
        lista_Aux2.append(tuple(ll[i]))
    Vertice=set(lista_Aux)
    Aresta=lista_Aux2
    return Vertice,Aresta


def dijkstra_caminho(G,V):
    print(nx.dijkstra_path(G,'1','10',weight='weight'))
    print("custo para ir do Vertice 1 ao vertice 10 e de",nx.dijkstra_path_length(G,'1','10'))
 
    print(nx.dijkstra_path(G,'1','100',weight='weight'))
    print("custo para ir do Vertice 1 ao vertice 100 e de",nx.dijkstra_path_length(G,'1','100'))


 
    if len(V)>1000:
        print(nx.dijkstra_path(G,'1','1000',weight='weight'))
        print("custo para ir do Vertice 1 ao vertice 10 e de",nx.dijkstra_path_length(G,'1','1000'))
 
        if len(V)> 10000:
            print(nx.dijkstra_path(G,'1','10000',weight='weight')) 
            print("custo para ir do Vertice 1 ao vertice 10000 e de",nx.dijkstra_path_length(G,'1','10000'))




#################

def menor_Vizinho(e_posi,objetivo,destino):
    objetivo=str(objetivo)
    destino=str(destino)
    l_aux=[]
    menor=5
    for i in range(len(e_posi)):
        if objetivo in e_posi[i]:
            l_aux.append(e_posi[i])
    
    for k in range(len(l_aux)):
        if menor > l_aux[k][2]:
            menor = l_aux[k][2]
            indice=k
        menor_v=l_aux[indice]
        
        if menor_v[0]!=objetivo:
            menor_Vizinho(l_aux,menor_v[1],destino)
        else :
            menor_Vizinho(l_aux,menor_v[0],destino)
    
    return menor_v
        
def  meu_dijkstra(A,objetivo,destino):
    objetivo=str(objetivo)
    Vizinhos_percorridos=[]
    i=0
    while True:
        m=menor_Vizinho(A,objetivo,destino)
        Vizinhos_percorridos.append(m)
        if objetivo!=m[0] :
            objetivo=m[0]
        else :
            objetivo=m[1]

        if objetivo==destino:
            print(objetivo,destino)
            break
       
        if i >10:
            break
        i +=1
    
    print(Vizinhos_percorridos)
