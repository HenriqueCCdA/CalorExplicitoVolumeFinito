import numpy as np

"""
*********************************************************************
* DATA DE CRIACAO  : 26/01/2019                                     *
* DATA DE MODIFICAO: 00/00/0000                                     *
* ----------------------------------------------------------------- *
* GRID: gera o gride pontos                                         *
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


def grid(length, nPoints, nCells):

    dx = length / nCells

    x = np.zeros(nPoints,dtype = float)
    # ... gerando coordenadas nodais
    for i in range(1 ,nPoints):
        x[i] = x[ i -1] + dx
    x[-1] = length
    # ......................................................................

    # ... gerando conectividade nodais
    cell = np.zeros((nCells,2),dtype = int)
    xc   = np.zeros(nCells,dtype = float)
    for i in range(0, nCells):
        cell[i][0], cell[i][1] = i+1, i+2
        xc[i] = (x[i+1]+x[i])*0.5
    # ......................................................................

    return x, xc, cell, dx


"""
c *********************************************************************
c * DATA DE CRIACAO  : 29/10/2018                                     *
c * DATA DE MODIFICAO: 00/00/0000                                     *
c * ----------------------------------------------------------------- *
c * NODALINTPERPOL: interpolacao os valores das celulas para o no     *
c * ----------------------------------------------------------------- *
c * Parametros de entrada:                                            *
c * ----------------------------------------------------------------- *
c * cells- conetividade nodal das celulas                             *
c * cc[0]  - tipo de condicao de contorno                             * 
c         1 - Temperatuta                                             *
c         2 - fluxo                                                   *
c         3 - resfriamento de newton                                  *
c * cc[1]    - valor numerico da condicao de contorno                 *
c * cellTemp - valores nas celulas                                    *
c * nodeTemp - nao definido                                           *
c * nCells   - numero de celulas                                      *
c * nPoints  - numero de pontos                                       *
c * ----------------------------------------------------------------- *
c * Parametros de saida:                                              *
c * ----------------------------------------------------------------- *
c * nodeTemp - valores nos pontos                                     *
c * ----------------------------------------------------------------- *
c * OBS:                                                              *
c * ----------------------------------------------------------------- *
c *********************************************************************
"""


def nodalInterpol(cells, cc, cellTemp, nodeTemp, nCells, nPoints):

    # ...
    for i in range( 0, nPoints):
        nodeTemp[i] = 0.0
    # ...
    for i in range( 0, nCells):
        no1 = cells[i][0] - 1
        no2 = cells[i][1] - 1
        tmp = cellTemp[i]
        nodeTemp[no1] += tmp
        nodeTemp[no2] += tmp
    # ......................................................................

    # ...
    for i in range( 1, nPoints -1):
        nodeTemp[i] *= 0.5e0
    # ......................................................................

    # ...
    if cc[0][0] == 1:
        nodeTemp[0] = cc[0][1]
    if cc[1][0] == 1:
        nodeTemp[-1] = cc[1][1]
# ......................................................................


"""
*********************************************************************
* DATA DE CRIACAO  : 29/10/2018                                     *
* DATA DE MODIFICAO: 00/00/0000                                     *
* ----------------------------------------------------------------- *
* RES : escreve os resultados                                       *
* ----------------------------------------------------------------- *
* Parametros de entrada:                                            *
* ----------------------------------------------------------------- *
* step - passo de tempo                                             *
* t    - tempo                                                      *
* u    - vetor a ser escrito                                        *
* n    - numero de pontos em u                                      *
* nout - arquivo de saida                                           *
* ----------------------------------------------------------------- *
* Parametros de saida:                                              *
* ----------------------------------------------------------------- *
* ----------------------------------------------------------------- *
* OBS:                                                              *
* ----------------------------------------------------------------- *
*********************************************************************
"""


def res(istep, t, u, n, f):
    f.write("{0:8} {1:8} ".format(istep ,t))
    for i in range(0, n):
        f.write(" {0:.14E} ".format(u[i]))
    f.write("\n")
