import math


class statistics(object):
    "Statistics Kill-Assist + Duracion de una partida"
    def __init__(self,kill,assist,duracion):
        self.kill=kill
        self.assist=assist
        self.duracion=duracion

    def makeKill(self):
        if(self.kill>0):
            self.kill-=1
    def makeAssist(self):
        if self.assist>0:
            self.assist-=1

class TreeNode(object):
    "Node of a Tree"
    def __init__(self,riesgo,tiempo,oro,tipo,name='incio',parent=None):
        self.riesgo=riesgo
        self.tiempo=tiempo
        self.oro=oro
        self.tipo=tipo
        self.name=name
        self.parent=parent
        self.children = []
        if self.children is not None:
            for child in self.children:
                self.add_child(child)

    def getChildren(self):
        return self.children

    def add_child(self, node):
        node.parent=self
        assert isinstance(node, TreeNode)
        self.children.append(node)

    def getParent(self):
        return self.parent

root=TreeNode(0,0,0,None)
playerStat=statistics(8.5,13.2,25.2)
generaPlayerStat=statistics(6.8 ,7.4,30)
objetivoOro=100


b1=TreeNode(9,20,300,"O","Baron",root)
b2=TreeNode(7,5,25,"O","Dragon",root)
b3=TreeNode(9,35,300,"O","Dragon Ancestral",root)
b4=TreeNode(4,None,150,"A","Asistencia",root)
b5=TreeNode(2,0.5,65,"O","Minions",root)
b6=TreeNode(3,1.25,99,"O","Escurridizo",root)
b7=TreeNode(9,8,100,"O","Heraldo",root)
b8=TreeNode(6,None,300,"K","Asesinato",root)

root.add_child(b1)
root.add_child(b2)
root.add_child(b3)
root.add_child(b4)
root.add_child(b5)
root.add_child(b6)
root.add_child(b7)
root.add_child(b8)

c1=TreeNode(9,20,300,"O","Baron",root)
c2=TreeNode(7,5,25,"O","Dragon",root)
c3=TreeNode(9,35,300,"O","Dragon Ancestral",root)
c4=TreeNode(4,None,150,"A","Asistencia",root)
c5=TreeNode(2,0.5,65,"O","Minions",root)
c6=TreeNode(3,1.25,99,"O","Escurridizo",root)
c7=TreeNode(9,8,100,"O","Heraldo",root)
c8=TreeNode(6,None,300,"K","Asesinato",root)

b1.add_child(c1)
b1.add_child(c2)
b1.add_child(c3)
b1.add_child(c4)
b1.add_child(c5)
b1.add_child(c6)
b1.add_child(c7)
b1.add_child(c8)


c9=TreeNode(9,20,300,"O","Baron",root)
c10=TreeNode(7,5,25,"O","Dragon",root)
c11=TreeNode(9,35,300,"O","Dragon Ancestral",root)
c12=TreeNode(4,None,150,"A","Asistencia",root)
c13=TreeNode(1,0.5,65,"O","Minions",root)
c14=TreeNode(3,1.25,99,"O","Escurridizo",root)
c15=TreeNode(9,8,100,"O","Heraldo",root)
c16=TreeNode(6,None,300,"K","Asesinato",root)

b2.add_child(c9)
b2.add_child(c10)
b2.add_child(c11)
b2.add_child(c12)
b2.add_child(c13)
b2.add_child(c14)
b2.add_child(c15)
b2.add_child(c16)

c17=TreeNode(9,20,300,"O","Baron",root)
c18=TreeNode(7,5,25,"O","Dragon",root)
c19=TreeNode(9,35,300,"O","Dragon Ancestral",root)
c20=TreeNode(4,None,150,"A","Asistencia",root)
c21=TreeNode(1,0.5,65,"O","Minions",root)
c22=TreeNode(3,1.25,99,"O","Escurridizo",root)
c23=TreeNode(9,8,100,"O","Heraldo",root)
c24=TreeNode(6,None,300,"K","Asesinato",root)

b3.add_child(c17)
b3.add_child(c18)
b3.add_child(c19)
b3.add_child(c20)
b3.add_child(c21)
b3.add_child(c22)
b3.add_child(c23)
b3.add_child(c24)

c25=TreeNode(9,20,300,"O","Baron",root)
c26=TreeNode(7,5,25,"O","Dragon",root)
c27=TreeNode(9,35,300,"O","Dragon Ancestral",root)
c28=TreeNode(4,None,150,"A","Asistencia",root)
c29=TreeNode(1,0.5,65,"O","Minions",root)
c30=TreeNode(3,1.25,99,"O","Escurridizo",root)
c31=TreeNode(9,8,100,"O","Heraldo",root)
c32=TreeNode(6,None,300,"K","Asesinato",root)

b4.add_child(c25)
b4.add_child(c26)
b4.add_child(c27)
b4.add_child(c28)
b4.add_child(c29)
b4.add_child(c30)
b4.add_child(c31)
b4.add_child(c32)

c33=TreeNode(9,20,300,"O","Baron",root)
c34=TreeNode(7,5,25,"O","Dragon",root)
c35=TreeNode(9,35,300,"O","Dragon Ancestral",root)
c36=TreeNode(4,None,150,"A","Asistencia",root)
c37=TreeNode(1,0.5,65,"O","Minions",root)
c38=TreeNode(3,1.25,99,"O","Escurridizo",root)
c39=TreeNode(9,8,100,"O","Heraldo",root)
c40=TreeNode(6,None,300,"K","Asesinato",root)

b5.add_child(c33)
b5.add_child(c34)
b5.add_child(c35)
b5.add_child(c36)
b5.add_child(c37)
b5.add_child(c38)
b5.add_child(c39)
b5.add_child(c40)

c41=TreeNode(9,20,300,"O","Baron",root)
c42=TreeNode(7,5,25,"O","Dragon",root)
c43=TreeNode(9,35,300,"O","Dragon Ancestral",root)
c44=TreeNode(4,None,150,"A","Asistencia",root)
c45=TreeNode(1,0.5,65,"O","Minions",root)
c46=TreeNode(3,1.25,99,"O","Escurridizo",root)
c47=TreeNode(9,8,100,"O","Heraldo",root)
c48=TreeNode(6,None,300,"K","Asesinato",root)

b6.add_child(c41)
b6.add_child(c42)
b6.add_child(c43)
b6.add_child(c44)
b6.add_child(c45)
b6.add_child(c46)

def inital():
    return root

def actionResults(TState):
    return TState.getChildren()

def isGoal(acum):
    return acum >= objetivoOro

def actionCost(e1,e2,pasoTiempo):
    tiempoValue=0;

    if e2.tipo == "O":
        aux = playerStat.duracion-e2.tiempo - pasoTiempo
        if 0 > aux:
            aux = 0
        tiempoValue = aux * 0.5

    if e2.tipo=="K":
        aux = (playerStat.duracion/playerStat.kill)-pasoTiempo
        tiempoValue=aux*0.5
    elif e2.tipo=="A":
        aux = (playerStat.duracion /playerStat.kill)-pasoTiempo
        tiempoValue = aux * 0.5

    recompensaValue = e2.oro * 0.5
    riesgoValue = e2.riesgo *5
    print(tiempoValue, recompensaValue, riesgoValue)
    print(tiempoValue + recompensaValue - riesgoValue)
    return tiempoValue + recompensaValue - riesgoValue

def heuristicCost(e,pasoTiempo):
    tiempoValue = 0;

    if e.tipo == "O":
        aux = generaPlayerStat.duracion- e.tiempo - pasoTiempo
        if 0 > aux:
            aux = 0
        tiempoValue = aux * 0.5

    if e.tipo == "K":
        aux = (generaPlayerStat.duracion / generaPlayerStat.kill)
        tiempoValue = aux * 0.5
    elif e.tipo == "A":
        aux = (generaPlayerStat.duracion / generaPlayerStat.kill)
        tiempoValue = aux * 0.5

    recompensaValue = e.oro * 0.5
    riesgoValue = e.riesgo *0.0
    print(tiempoValue ,recompensaValue , riesgoValue)
    print(tiempoValue + recompensaValue - riesgoValue)
    return tiempoValue + recompensaValue - riesgoValue

def bestNode(nodes,initialState,pasoTiempo):
    maxi=math.inf
    best=""
    for node in nodes:
        print(node.name)
        aux=actionCost(initialState,node,pasoTiempo)+heuristicCost(node,pasoTiempo)
        if aux<maxi:
            maxi=aux
            best=node
    #print(initialState+" best node "+best)
    return best




def a(e, path=[], pasoTiempo=5, acum=0):
    nodes=actionResults(e)

    print(path)
    if isGoal(acum):
        return path
    if  len(nodes)==1:
        return False
    aux = bestNode(nodes, e, pasoTiempo)
    path.append([e.name, aux.name])
    print(acum,aux.oro)
    acum+=aux.oro
    print(acum)
    return a(aux,path,pasoTiempo,acum)

a(root)