class Tempo:

    def __init__(self):
        self.dia = 1
        self.hora = 8
        

    def getDia(self):
        return self.dia

    def getHora(self):
        return self.hora    


    def passarHora(self, valor):
        self.hora += valor
        h = self.hora - 24
        if self.hora >= 24:
            self.hora = h
            self.avancarDia()
            
        return self.hora


    def avancarDia(self):
        self.dia += 1 

    
       
       
        

