import time
import os
import winsound


print('Digite o horario para despertar')
hora = input('Hora : ')
min = input('Minuto: ')
seg = input('Segundos: ')
for h in range(1, 24):
    for m in range(1, 60):
        for s in range(1, 60):
            print("h: ", h, "m: ", m, "s: ", s)
            time.sleep(1)
            os.system("cls")
            if int(hora) == h and int(min) == m and int(seg) == s:
                frequency = 2500  # Set Frequency To 2500 Hertz
                duration = 1000  # Set Duration To 1000 ms == 1 second
                winsound.Beep(frequency, duration)
                winsound.Beep(frequency, duration)
                winsound.Beep(frequency, duration)
