class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.alive = True
        self.comer = 'come algo....'

    def hablar(self):
        print('esto tiene que sonar de algun modo')
    
    def responder(self, msg):
        print(f"dice {self.nombre} que tu {msg} pues.. mira... que no lo entiende")



#clase que hereda de Animal y no modifica los atributos del inicializador de la clase de la que hereda
class Molusco(Animal):

    def hablar(self):
        print(f"no estoy seguro que los moulscos digan algo.... ")
        
    def existir(self):
        print(f"{self.nombre} dice que esto no es existir")



#clase que hereda de Animal y MODIFICA los atributos del inicializador de la clase de la que hereda
class Vaca(Animal):
    def __init__(self, nombre):
        super().__init__(nombre) #el super hace referencia al padre (de donde estamos heredando)
        self.comer = 'hierba'

    def hablar(self):
        print(f"{self.nombre} dice 'muuuuuuu'")

    def darLeche(self):
        print(f"{self.nombre} esta dando leche")



#clase que hereda de Animal y MODIFICA los atributos del inicializador de la clase de la que hereda
class Grillo(Animal):
    def __init__(self, nombre):
        super().__init__(nombre) #el super hace referencia al padre (de donde estamos heredando)
        self.comer = 'hormigas'

    def hablar(self):
        print(f"{self.nombre} dice 'kri-kri'")

    def cantar(self):
        print('kri kri kriiiiiii kri kri....')



