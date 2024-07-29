import datetime

class Vehiculo:
    def __init__(self, placa):
        self.placa = placa

    def tiene_pico_y_placa(self, fecha):
        
        ultimo_digito = int(self.placa[-1])
        dia_semana = fecha.weekday()  
        if dia_semana < 5:
            if ultimo_digito in (6, 7, 8, 9, 0) and dia_semana % 2 == 0:
                return True
            elif ultimo_digito in (1, 2, 3, 4, 5) and dia_semana % 2 == 1:
                return True
        return False
mi_carro = Vehiculo("ABC1234")
hoy = datetime.date.today()

if mi_carro.tiene_pico_y_placa(hoy):
    print("Tu vehículo tiene pico y placa hoy.")
else:
    print("Tu vehículo no tiene pico y placa hoy.")
