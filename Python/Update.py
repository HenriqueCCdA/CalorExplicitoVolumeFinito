"""
c *********************************************************************
c * DATA DE CRIACAO  : 07/11/2018                                     *
c * DATA DE MODIFICAO: 00/00/0000                                     *
c * ----------------------------------------------------------------- *
c * UPDATE : atualiza o campo de velocidade explicitamente            *                                     *
c * ----------------------------------------------------------------- *
c * Parametros de entrada:                                            *
c * ----------------------------------------------------------------- *
c * temp   - nao definido                                             *
c * temp0  - temperatura do passo anteior                             *
c * sQ     - fonte de calor                                           *
c * k      - coeficiente de conducao termica                          *
c * ro     - massa especidica                                         *
c * cp     - calor espefifico                                         *
c * dt     - delta t                                                  *
c * cc[0]  - tipo de condicao de contorno                             *
c         1 - Temperatuta                                             *
c         2 - fluxo                                                   *
c         3 - resfriamento de newton                                  *
c * cc[1]  - valor numerico da condicao de contorno                   *
c * cc[2]  - valor de h                                               *
c * dx     - delta x                                                  *
c * nCells - numero de celulas (elementos)                            *
c * ----------------------------------------------------------------- *
c * Parametros de saida:                                              *
c * ----------------------------------------------------------------- *
c * temp - nova campo de temperatura                                  *
c * ----------------------------------------------------------------- *
c * OBS:                                                              *
c * ----------------------------------------------------------------- *
c *********************************************************************
"""


def update(temp,temp0, sQ, k, ro, cp, dt , cc, dx , nCells):


    h = cc[0][2], cc[1][2]
    # ... temperatura pescrita
    aP0 = ro[0]*cp[0]*dx/dt
    kf  = (k[0] + k[1])*0.5e0
    aE  = kf/dx
    if cc[0][0] == 1:
        sP  = -2.0e0*k[0]/dx
        sU  = -sP*cc[0][1]
    # ... fluxo prescrito
    elif cc[0][0] == 2:
        sP  = 0.e0
        sU  = -cc[0][1]
    # ... lei de resfriamento
    elif cc[0][0] == 3:
        tmp = 1.e0 + (h[0]*2.e0*dx)/k[0]
        tmp = h[0]/tmp
        sP  = -tmp
        sU  = tmp*cc[0][1]
    # .................................................................

    temp[0] = (aE*temp0[1] + (aP0 - aE + sP)*temp0[0] + sU)/aP0

    # ... temperatura pescrita
    aP0 = ro[-1]*cp[-1]*dx/dt
    kf  = (k[-2] + k[-1])*0.5e0
    aW  = kf/dx
    if cc[1][0] == 1:
        sP  = -2.0e0*k[-1]/dx
        sU  = -sP*cc[1][1]
    # ... fluxo prescrito
    elif cc[1][0] == 2:
        sP  = 0.e0
        sU  = -cc[1][1]
    # ... lei de resfriamento
    elif cc[1][0] == 3:
        tmp = 1.e0 + (h[1]*2.e0*dx)/k[-1]
        tmp = h[1]/tmp
        sP  = -tmp
        sU  = tmp*cc[1][1]
    # .................................................................

    temp[-1] = (aW*temp0[-2] + (aP0 - aW + sP)*temp0[-1] + sU)/aP0
    # .................................................................

    # ...
    for i in range(1, nCells-1):
        aP0 = ro[i]*cp[i]*dx/dt
        # ... w
        kf = (k[i-1] + k[i])*0.5e0
        aW = kf/dx
        # ... w
        kf = (k[i] + k[i+1])*0.5e0
        aE = kf/dx
        # ...
        temp[i] = (aW*temp0[i-1] + aE*temp0[i+1]+ (aP0 - aE - aW)*temp0[i])/aP0
    # .................................................................

    # temp0 <- temp
    for i in range(0, nCells):
      temp0[i] = temp[i]


      
