class Perros:
    def __init__(self, nombre, edad, enfermedad):
        self.nombre = nombre
        self._edad= edad ## significa que a edad solo se deberia de poder acceder desde la propia clase ---> peligroso
        self.__enfermedad = enfermedad or '' ## si es privado, no se puede acceder directamente y menos modificar directamente, solo desde la clase
        self.patas = 4
        self.cola = True
        self.contento = False
    
    def ladrar(self):
        print(f"{self.nombre} esta ladrando")
    
    def contento(self):
        print(f"{self.nombre} esta moviendo la cola")
    
    def jugar(self):
        print('le lanzas la pelota')
        print(f"{self.nombre} fue a buscar la pelota y te la trajo")
        self.contento=True
        print(f"{self.nombre} esta {self.contento}")
    
    def chequearContentura(self):
        print(self.contento)
    
    def sanar(self):
        self.__enfermedad = False
        print(f"{self.nombre} estaba enfermo pero ahora esta curado --> {self.__enfermedad}")
