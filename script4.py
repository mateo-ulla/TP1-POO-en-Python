class Nodo:
    def __init__(self, nombre, apellido, edad, curso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.curso = curso  

    def programar(self):
        print(f"el alumno {self.nombre} esta programando")

alumno = Nodo("pepe".lower(), "suarez".lower(), "17".lower(), "6P".lower())
alumno.programar()
