
""" WORKOUT--------------------------------------
class workout():
    def __init__(self, nome, ex, zav, rep):
        self.nome=nome
        self.ex=ex
        self.zav=zav
        self.rep=rep

    def volume(self):
        return self.zav*self.rep
    
    def eforte(self):
        if self.zav>=50:
            return "sei forte"
        else: return "sei debole"
    
    def categoria(self):
        if self.zav>=50:
            return "HEAVY"
        elif self.zav<50&self.zav>=30: 
            return "MEDIUM"
        elif self.zav<30: 
            return "LIGHT"
        
                    
    def stampa_workout(self):
        print("Nome:", self.nome)
        print("Esercizio:", self.ex)
        print("Zavorra:", self.zav)
        print("Reps:", self.rep)
        print("Volume:", self.volume())
        print("Sei forte?", self.eforte())
        print("categoria", self.categoria())


a1=workout("Valerio", "Pull Up", 30, 10)

a1.stampa_workout()-------------------------------------"""

def crea_studente():
    nome = input("Inserisci il nome: ")
    cognome = input("Inserisci il cognome: ")
    eta = input("Inserisci l'età: ")
    matricola = input("Inserisci la matricola: ")
    """voti = list(map(int, input("Inserisci i voti con uno spazio: ").split()))"""
    voti=input("Inserisci i voti con uno spazio: ").split()

    return studente(nome, cognome, eta, matricola, voti)

class studente():
    def __init__(self, nome, cognome, eta, matricola,voti):
        self.nome=nome
        self.cognome=cognome
        self.eta=int(eta)
        self.matricola=int(matricola)
        self.voti = [int(x) for x in voti]
    def presentati(self):
        print(self.nome, self.cognome, "e' uno studente di",self.eta,"anni","di matricola",
               self.matricola, "con media:", self.media_voti())
    def aggiungi_voto(self):
        nuovi_voti= list(map(int, input("Inserisci nuovi voti: ").split()))
        self.voti.extend(nuovi_voti)
        print(self.voti)
    def media_voti(self):
        if len(self.voti) == 0:
            return 0
        else:
            mediavoti=0
            for x in self.voti:
                mediavoti+=x
                """print("La tua media è:",mediavoti/len(self.voti))"""
            return mediavoti/len(self.voti)
    def studia(self):
        totesami=0
        for x in self.voti:
            totesami+=1
        print("E finora ha studiato in media",totesami*10,"ore per",totesami,"esami" )

pippo=crea_studente()
pippo.aggiungi_voto()
pippo.presentati()
pippo.studia()

paperino=crea_studente()
paperino.aggiungi_voto()
paperino.presentati()
paperino.studia()


