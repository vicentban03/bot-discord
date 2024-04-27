import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<hufejsoi8239r7ualwpknpq>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)
    return password
def ping():
    return ('pong')
def money():
    for i in range(2):
        g = random.randint(0,2)
        if g == 0:
            return ('cara')

        elif g == 1:
            return ('cruz')
        else:
            return ('empate')
def help():
    lis = ['!hello','!ping','!pass','!mone','!help','!trivia']
    return lis

def quiz():
    # Lista de preguntas y respuestas
    preguntas_respuestas = {
        'mc': [
            ('¿Quién es el creador original de Minecraft?', ['a) Daniel Rosenfeld ', 'b) Notch', 'c) Jeb', 'd) Dinnerbone'], 'b) Notch'),
            ('¿Qué tipo de mob o criatura se quema con la luz del día?', ['a) Zombi', 'b) Esqueleto', 'c) Creeper', 'd) Zombi Pigman'], 'a) Zombi'),
            ('¿Qué bloque se utiliza comúnmente para crear portales al Nether?', ['a) Obsidiana', 'b) Piedra', 'c) Arena', 'd) Bloque de hierro'], 'a) Obsidiana')
        ],
        'hk': [
            ('¿Cómo se llama el mapa del mundo que el jugador puede ir completando a medida que explora Hallownest?', ['a) Hollow Map', 'b) Explorer\'s Map', 'c) Map of Wonders', 'd) Atlas of Hallownest'], 'd) Atlas of Hallownest'),
            ('¿Cuál es el nombre de la ciudad en ruinas que los jugadores exploran en el juego?', ['a) Hallownest', 'b) Dirtmouth', 'c) Greenpath', 'd) Crystal Peak'], 'a) Hallownest'),
            ('¿Quién es el desarrollador principal del juego Hollow Knight?', ['a) Team Cherry', 'b) Mojang Studios', 'c) Naughty Dog', 'd) Rockstar Games'], 'a) Team Cherry')
        ],
        'ak': [
            ('¿Cómo puedes domar a los dinosaurios en ARK?', ['a) Dándoles comida', 'b) Acariciándolos', 'c) Montándolos', 'd) Usando un arma de doma'], 'd) Usando un arma de doma'),
            ('¿En qué tipo de entorno se desarrolla ARK?', ['a) En el espacio', 'b) En una isla desierta', 'c) En el fondo del mar', 'd) En un mundo post-apocalíptico'], 'b) En una isla desierta'),
            ('¿Qué necesitas hacer para sobrevivir en ARK?', ['a) Construir una casa', 'b) Cazar', 'c) Nadar', 'd) Plantar árboles'], 'b) Cazar')
        ]
    }
    
    # Seleccionar una categoría aleatoria
    categoria = random.choice(list(preguntas_respuestas.keys()))
    # Seleccionar una pregunta y respuestas de la categoría seleccionada
    pregunta, opciones = random.choice(preguntas_respuestas[categoria])
    
    return pregunta, opciones
