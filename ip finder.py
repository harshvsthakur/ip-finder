import socket
import csv

for i in range(0,11):
    IP = '192.168.0.'+str(i)
    try:
        x = socket.gethostbyaddr(IP)
        t = list(x[0],x[2][0])
        with open(r'test.csv','rb') as out:
            csv_out=csv.writer(out)
            csv_out.writerow(['name','ip'])
            csv_out.writerow(t)
    except:
        print('{} NA'.format(IP))
