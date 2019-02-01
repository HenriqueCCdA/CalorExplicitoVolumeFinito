import matplotlib.pyplot as plt

with open('plot.in','r') as f:
    data = f.read()

lines = data.splitlines()

nameFile = lines[0]

step     = lines[1:-1]

print(nameFile,step)


with open(nameFile,'r') as f:
    data = f.read()
        
lines = data.splitlines()

x = lines[0].split()[2:]
x = [float(i) for i in x]

for i in step:
    tmp  = lines[int(i)+1].split()
    t    = tmp[1]
    temp = [float(i) for i in tmp[2:]]
    plt.plot(x,temp,label='t(s) = ' + t) 

plt.xlabel('time (s)')
plt.ylabel('Temperatua(°C)')

plt.legend()
plt.show()
