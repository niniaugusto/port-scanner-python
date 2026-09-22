import socket

def testar_porta(ip, porta):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    resultado = s.connect_ex((ip, porta))
    s.close()
    return resultado == 0

def scan(ip, inicio, fim):
    abertas = []
    for porta in range(inicio, fim + 1):
        if testar_porta(ip, porta):
            print(f"[+] Porta {porta} aberta")
            abertas.append(porta)
    return abertas

if __name__ == "__main__":
    ip = "127.0.0.1"
    scan(ip, 1, 1024)