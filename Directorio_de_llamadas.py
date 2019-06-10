import random
from datetime import datetime, timedelta

amigos = ['juan', 'carlos', 'ana']
directory = []


# funcion para generar fecha aleatoria


def get_rnd_date(start, end, fmt):
    s = datetime.strptime(start, fmt)
    e = datetime.strptime(end, fmt)

    delta = e - s

    return s + timedelta(days=(random.random() * delta.days))


for x in range(10):
    temp = []
    temp.append(get_rnd_date("01/01/2019", "15/06/2019", "%d/%m/%Y").date())
    temp.append(random.choice(amigos))
    temp.append(random.randint(100, 1000))
    directory.append(temp)

print(*sorted(directory), sep="\n")
