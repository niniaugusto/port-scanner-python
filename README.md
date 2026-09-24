# port-scanner-python
# Port Scanner em Python

Scanner de portas TCP simples, feito em Python puro (sem bibliotecas externas), como parte do meu portfólio de estudos em cibersegurança e pentest.

## O que faz

Recebe um IP e um intervalo de portas, e testa quais estão abertas usando sockets TCP. Usa múltiplas threads para escanear várias portas em paralelo, o que torna o processo muito mais rápido do que um scan sequencial.

## Como funciona

- `socket.connect_ex()` tenta abrir uma conexão TCP com cada porta; se o retorno for `0`, a porta está aberta.
- Cada porta é testada em uma thread separada, com um `Lock` para evitar conflitos ao salvar os resultados.
- Os argumentos são passados via linha de comando com `argparse`.

## Como usar

Requer Python 3.

```bash
python scanner.py -ip <IP_ALVO> -p <INICIO>-<FIM>
```

**Exemplo:**
```bash
python scanner.py -ip 127.0.0.1 -p 1-1024
```

**Saída esperada:**

```
Escaneando 127.0.0.1 de 1 a 1024...
[+] Porta 135 aberta
[+] Porta 445 aberta

Portas abertas: [135, 445]
```

## Próximos passos

- Adicionar detecção do serviço rodando em cada porta (banner grabbing)
- Exportar resultado em JSON/CSV
- Adicionar suporte a scan de UDP

## Aviso legal

Este projeto foi criado **apenas para fins educacionais**, como parte dos meus estudos em cibersegurança. Use somente em redes e sistemas próprios ou com autorização explícita do responsável. Escanear sistemas de terceiros sem permissão é crime previsto na Lei nº 12.737/2012 (Lei Carolina Dieckmann) e no Marco Civil da Internet.

## Autor

Nicolas — em transição de carreira para cibersegurança, com foco em ethical hacking e pentest.