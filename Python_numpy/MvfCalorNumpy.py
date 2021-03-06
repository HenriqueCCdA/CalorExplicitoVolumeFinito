import ReadFile as rf
import Update as up
import GridNumpy as gr
import time as tm
import numpy as np


def main():

    filesInf = rf.readFile()

    # ...
    nCells = filesInf['ndiv']
    nPoints = filesInf['ndiv'] + 1
    length = filesInf['length']
    preName = filesInf['output']
    nStep = filesInf['nstep']
    # ......................................................................

    # ... gera o grid
    x, xc, cells, dx = gr.grid(length, nPoints, nCells)
    # ......................................................................

    # ...
    timeWres = timeUpdate = 0.e0

    # ...
    t = 0.0
    dt = filesInf['dt']

    k  = np.full(nCells,filesInf['prop'][0],dtype = float)
    ro = np.full(nCells,filesInf['prop'][1],dtype = float)
    cp = np.full(nCells,filesInf['prop'][2],dtype = float)
    
    cc = np.array([filesInf['cce'], filesInf['ccd']])
    sQ = np.zeros(nCells, dtype = float)

    nodeTemp = nPoints * [0.0]
    cellTemp  = nCells * [0.0]
    cellTemp0 = nCells * [filesInf['initialt']]

    nodeTemp  = np.zeros(nPoints, dtype = float)
    cellTemp0 = np.full(nCells,filesInf['initialt'],dtype = float)
    cellTemp  = np.zeros(nCells, dtype = float)
    # .................................................................

    # ...
    fileResCell = open(preName +'_cell.python', 'w')
    fileResNode = open(preName +'_node.python', 'w')
    # .................................................................

    # ...
    gr.nodalInterpol(cells, cc, cellTemp0, nodeTemp, nCells, nPoints)
    # ................................1.................................

    # ...
    time0 = tm.time()
    gr.res(0, 0.0, xc,  nCells, fileResCell)
    gr.res(0, 0.0,  x, nPoints, fileResNode)
    timeWres += tm.time() - time0
    # .................................................................

    # ... temperatura inicial
    time0 = tm.time()
    gr.res(0, 0.0, cellTemp0, nCells, fileResCell)
    gr.res(0, 0.0, nodeTemp, nPoints, fileResNode)
    timeWres += tm.time() - time0
    # .................................................................

    # ... delta critico
    dtCrit = (min(ro)*min(cp)*dx**2)/(2.0*min(k))
    print("DeltaT Critico = {0}\n"\
          "DeltaT         = {1}".format(dtCrit, dt))
    # .................................................................

    # ...
    print("Running ...")
    for j in range(1,nStep+1):

        # ...
#        print("Step : {0}\nTime(s) : {1}".format(j, t))
        t += dt
        # .............................................................

        # ... atualizada temp n
        time0 = tm.time()
        up.update(cellTemp, cellTemp0, sQ, k, ro, cp, dt , cc,\
                  dx, nCells)
        timeUpdate += tm.time() - time0
        # .............................................................

        # ...
        gr.nodalInterpol(cells, cc, cellTemp, nodeTemp, nCells, nPoints)
        # .............................................................

        # ... temperatura inicial
        time0 = tm.time()
        gr.res(j, t, cellTemp, nCells, fileResCell)
        gr.res(j, t, nodeTemp, nPoints, fileResNode)
        timeWres += tm.time() - time0
        # .............................................................

    # .................................................................

    # ...
    print("done.")
    # .................................................................

    # ...
    print("Time Update(s) : {0:.4f}\n"\
          "Time Wres(s)   : {1:.4f}".format(timeUpdate, timeWres))
    # .................................................................


    # ...
    fileResCell.close()
    fileResNode.close()
# ......................................................................


if __name__ == '__main__':
    main()
