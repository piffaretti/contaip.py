# contaip.py
Lê uma lista de ranges de IP, um range por linha e conta quantos IPs tem ao total.

O script pode ser útil quando receber um escopo de IPs em um pentest ou em um scan de vulnerabilidades e quiser saber ao todo quantos IPs tem.

Baseado no script do Joshua Wright : https://gist.github.com/joswr1ght/595d49d5a7914cf7305b73512f37186


# Utilização:
```ps
python3 contaip.py IPs_UmPorLinha.txt
```
# Exemplo:
Supondo qe o arquivo listaIPs.txt contenha o seguinte conteudo:

10.10.10.0/24
192.168.0.1/24

Ao executar o comando:

python3 contaip.py listaIPs.txt

O output vai ser de 512 IPs, pois cada /24 possui 256 IPs.
