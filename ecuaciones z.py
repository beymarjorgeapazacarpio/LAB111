segundos = int(input("Escriba la cantidad en segundos: "))
dias = segundos // (24 * 60 * 60)
segundos = segundos % (24 * 60 * 60)
horas = segundos // (60 * 60)
segundos = segundos % (60 * 60)
minutos =  segundos // 60
segundos =  segundos % 60
segundos =  segundos + 1
print("Dias: {} - Hora: {} - Minutos: {} - Segundos: {}".format(dias, horas, minutos, segundos + 1))
