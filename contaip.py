#Based on Joshua Wright original script : https://gist.github.com/joswr1ght/595d49d5a7914cf7305b73512f37186a
#Adapted by Diego Piffaretti
#!/usr/bin/env python

import sys

def countips(netblock):
    cidr = int(netblock.split('/')[1])
    return 2**(32 - cidr)

if (len(sys.argv) != 2):
    print(f"Usage: {sys.argv[0]} <file with CIDR masks>")
    sys.exit(0)


ipcount=0
with open(sys.argv[1]) as infile:
    for netblock in infile:
        ipcount += countips(netblock)
    filename = sys.argv[1]
    print("O arquivo",filename,"possui ao todo" ,ipcount,"IPs")