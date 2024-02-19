class Auto:
   cantidadCreados=0
   def __init__(self, modelo, precio, asientos, marca, motor, registro):
      self.modelo = modelo
      self.precio = precio
      self.asientos = asientos
      self.marca = marca
      self.motor = motor
      self.registro = registro
      Auto.cantidadCreados +=1

def cantidadAsientos(self):
   c = 0
   for asiento in self.asientos:
        if isinstance(asiento, Asiento):
            c += 1
   return c
   
def verificarIntegridad(self):
   registro_auto = self.registro
   registro_motor = self.motor.registro if self.motor else None
   asientos_originales = True
    
   for asiento in self.asientos:
        if isinstance(asiento, Asiento) and asiento.registro != registro_auto:
            asientos_originales = False
            break

   if registro_motor is not None and registro_auto == registro_motor and asientos_originales:
        return "Auto original"
   else:
        return "Las piezas no son originales"

class Asiento:
   def __init__(self, color, precio, registro):
      self.color = color
      self.precio = precio
      self.registro = registro

def cambiarColor(self, nuevoColor):
        colores = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if nuevoColor in colores:
            self.color = nuevoColor

class Motor:    
   def __init__(self, numeroCilindros, tipo, registro):
      self.numeroCilindros = numeroCilindros
      self.tipo = tipo
      self.registro = registro

def cambiarRegistro(self, nuevoRegistro):
        self.registro = nuevoRegistro

def asignarTipo(self, nuevoTipo):
        tipos = ["electrico", "gasolina"]
        if nuevoTipo in tipos:
            self.tipo = nuevoTipo

