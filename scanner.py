import socket
import argparse
import threading

abertas = []
lock = threading.Lock()

def testar_porta(ip, porta):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    resultado = s.connect_ex((ip, porta))
    s.close()
    if resultado == 0:
        with lock:
            print(f"[+] Porta {porta} aberta")
            abertas.append(porta)

def scan(ip, inicio, fim):
    threads = []
    for porta in range(inicio, fim + 1):
        t = threading.Thread(target=testar_porta, args=(ip, porta))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return abertas

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scanner simples de portas TCP")
    parser.add_argument("-ip", required=True, help="IP alvo, ex: 127.0.0.1")
    parser.add_argument("-p", required=True, help="Intervalo de portas, ex: 1-1024")
    args = parser.parse_args()

    inicio, fim = map(int, args.p.split("-"))
    print(f"Escaneando {args.ip} de {inicio} a {fim}...")
    scan(args.ip, inicio, fim)
    print(f"\nPortas abertas: {sorted(abertas)}")