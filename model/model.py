import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.g=nx.DiGraph()
        self.v=[]
        self.idMap={}
        self.archi=None
        self.s=0
        self.BP=[]
        self.pesoMax=0
    def creaGrafo(self):
        self.g.clear()
        self.v=DAO.getChromosomes()
        for v in self.v:
            self.idMap[v.chromosome]=v
        self.g.add_nodes_from(self.v)
        self.archi=DAO.getArchi()
        for arco in self.archi:
            self.g.add_edge(self.idMap[arco[0]], self.idMap[arco[1]], weight=float(arco[2]))
        print(self.g)
    def getNumNodes(self):
        return len(self.g.nodes)
    def getNumEdges(self):
        return len(self.g.edges)
    def MinMaxValues(self):
        listaTup=copy.deepcopy(self.archi)
        listaTup.sort(key=lambda x:x[2])
        min=listaTup[0][2]
        MAX=listaTup[-1][2]
        return min,MAX
    def countEdges(self,soglia):
        self.s=soglia
        sotto=0
        sopra=0
        for arco in self.archi:
            if arco[2]<soglia:
                sotto+=1
            else:
                sopra+=1
        return sotto,sopra
    def getBP(self,soglia):
        parziale=[]
        for node in self.g.nodes:
            visitabili=self.getVisitabili(node,soglia,[])
            parziale.append(node)
            self.ricorsione(parziale,visitabili,soglia,[])
            parziale.pop()
    def ricorsione(self,parziale,visitabili,soglia,visitati):
        peso=self.calcolaPeso(parziale)
        print("r")
        if peso>self.pesoMax:
            self.BP=copy.deepcopy(parziale)
            self.pesoMax=peso
        if len(visitabili)==0:
            return
        for el in visitabili:
            NEWvisitabili = self.getVisitabili(el,soglia,visitati)
            parziale.append(el)
            visitati.append((parziale[-2],parziale[-1]))
            self.ricorsione(parziale, NEWvisitabili,soglia,visitati)
            parziale.pop()
            visitati.pop()

    def calcolaPeso(self, parziale):
        return sum(self.g[parziale[x]][parziale[x+1]]["weight"] for x in range(0,len(parziale)-1))

    def getVisitabili(self, node,soglia,visitati):
        v=[]
        for s in self.g.successors(node)  :
            if (node,s) not in visitati:
                if self.g[node][s]["weight"]>soglia:
                    v.append(s)
        return v
    def tuplePrint(self):
        tt=[]
        for i in range(0,len(self.BP)-1):
            tt.append((self.BP[i],self.BP[i+1],self.g[self.BP[i]][self.BP[i+1]]["weight"]))
        return tt







