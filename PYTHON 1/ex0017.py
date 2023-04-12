'''import math
angulo = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(angulo))
print('O ângulo é {} e o SENO é {:.2f}.'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O ângulo é {} e o COSSENO é {:.2f}.'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo é {} e a tangente é {:.2f}'.format(angulo, tangente))'''

from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo: '))
seno = sin(radians(angulo))
print('O ângulo é {} e o SENO é {:.2f}.'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo é {} e o COSSENO é {:.2f}.'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O ângulo é {} e a tangente é {:.2f}'.format(angulo, tangente))