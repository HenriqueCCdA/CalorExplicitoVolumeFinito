import matplotlib.pyplot as plt
import pandas as pd

def plotX(fileNames,nameOut,step):


   for name in fileNames:

        res1 = pd.read_table(name,sep='\s+',header=None,verbose=False)

        sufixo1=name.split('.')[0]

# ... descartando as 1 ultimas linhas
        x = res1.iloc[0].values
        x = x[2:]
        for i in step:
            temp   = res1.iloc[int(i)].values
            t      = temp[1]
            temp   = temp[2:]
            plt.plot(x,temp,linestyle='-',label=sufixo1 +' t(s) = ' + str(t)) 
 
   plt.xlabel('L (m)')
   plt.ylabel('Temperatura(°C)')

   plt.legend()
   plt.xlim(x[0],x[-1])
#    plt.savefig(nameOut)
   plt.show()

def plotT(fileNames,nameOut):

    def no(i):
        return i+1

    for name in fileNames:

        res1 = pd.read_table(name,sep='\s+',header=None,verbose=False)

        sufixo1=name.split('.')[0]

# ... descartando primeira linha
        res1 = res1[1:]
        t1   = res1[1]
        no1r1 = res1[no(1)]
        plt.plot(t1,no1r1,linestyle='-',label=sufixo1+' - no1')

#        no1r1 = res1[no(101)]
#        plt.plot(t1,no1r1,linestyle='--',label=sufixo1+' - no101')

    
    plt.legend()
#    plt.xlim(x1[0],x1[-1])
#    plt.savefig(nameOut)
    plt.show()
   

def main():


    with open('plotComp.in','r') as f:
        data = f.read()

    lines = data.splitlines()

    fileNames = lines[0].split()
    nameOut   = lines[2]

    step     = lines[2:]

    plotX(fileNames,nameOut,step)
    plotT(fileNames,nameOut)
    
main()

