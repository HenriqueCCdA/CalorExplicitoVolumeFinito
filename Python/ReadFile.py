"""
*********************************************************************
* DATA DE CRIACAO  : 07/11/2018                                     *
* DATA DE MODIFICAO: 00/00/0000                                     *
* ----------------------------------------------------------------- *
* READFILE: leitura do arquivo de entrada                           *
* ----------------------------------------------------------------- *
* Parametros de entrada:                                            *
* ----------------------------------------------------------------- *
* length  - comprimento da barra                                    *
* nPoint - numero de pontos                                         *
* nCells - numero de divisoes (elementos)                           *
* ----------------------------------------------------------------- *
* Parametros de saida:                                              *
* ----------------------------------------------------------------- *
* x    - cordenada dos pontos                                       *
* xc   - cordenadas dos centro dos elmentos                         *
* cell - conectividade nodais do elementos                          *
* dx   - tamanho do grid                                            *
* ----------------------------------------------------------------- *
* OBS:                                                              *
* ----------------------------------------------------------------- *
*********************************************************************
"""


def readFile():

    fileName = 'input.dat'

    macros = ['output', 'length', 'ndiv', 'dt', 'nstep', 'initialt',\
              'prop', 'cce', 'ccd', 'end']

    dic = {}

    f = open(fileName, 'r')

    while True:
        word = f.readline().split()
        # ... nome do arquivo de saida
        if word[0] == macros[0]:
            dic[macros[0]] = word[1]
        # ... comprimento da barra
        elif word[0] == macros[1]:
            dic[macros[1]] = float(word[1])
        # ... numero de divisoes da barra
        elif word[0] == macros[2]:
            dic[macros[2]] = int(word[1])
        # ... delta t
        elif word[0] == macros[3]:
            dic[macros[3]] = float(word[1])
        # ... numero de passos
        elif word[0] == macros[4]:
            dic[macros[4]] = int(word[1])
        # ... temperatura inicial
        elif word[0] == macros[5]:
            dic[macros[5]] = float(word[1])
        # ... propriedades fisicas
        elif word[0] == macros[6]:
            dic[macros[6]] = [float(word[1]), float(word[2]), float(word[3])]
        # ... propriedades cce
        elif word[0] == macros[7]:
            type = int(word[1])
            if type == 3 :
                dic[macros[7]] = [int(word[1]), float(word[2]), float(word[3])]
            else:
                dic[macros[7]] = [int(word[1]), float(word[2]), 0.e0]
        # ... propriedades ccd
        elif word[0] == macros[8]:
            type = int(word[1])
            if type == 3 :
                dic[macros[8]] = [int(word[1]), float(word[2]), float(word[3])]
            else:
                dic[macros[8]] = [int(word[1]), float(word[2]), 0.e0]
        # ...
        elif word[0] == macros[-1]:
            break

    f.close()

    #  exepect
    return dic