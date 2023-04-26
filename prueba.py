
#Se importa el modulo subprocess
import subprocess

#Se define un par de variables con los comandos a pasar:
cmd = ['xrandr']
cmd2 = ['grep', '*']

#Se ejecuta el comando xrandr y luego se abre una tuberia.
p = subprocess.Popen(cmd, stdout=subprocess.PIPE)

#Se ejecuta el segundo comando
p2 = subprocess.Popen(cmd2, stdin=p.stdout, stdout=subprocess.PIPE)

#Se cierra la salida estandar.
p.stdout.close()


#Obteccion de la resolucion
resolution_string, junk = p2.communicate()
resolution = resolution_string.split()[0]
print(resolution)
