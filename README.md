# Revshell

<h1 align="center">
  <img src="img/sdiscovery.png" alt="sdiscovery" width="200px"></a>
  <br>
</h1>

<h4 align="center">Host and Port Discovery - Cheatsheets </h4>


<p align="center">
  <a href="#características">Features</a> •
  <a href="#instalação">Install</a> •
  <a href="#forma-de-utilização">How to use</a> •
  <a href="#executando-sdiscovery">Usage</a>
</p>

---

O Sdiscovery é uma ferramenta que gera scripts para descoberta de hosts e portas válidas na rede. Possui uma arquitetura modular simples e otimizada para velocidade. Sdiscovery é construído para fazer apenas uma coisa gera scripts, e faz isso muito bem.

Projetei o `Sdiscovery` mantive um modelo consistentemente passivo para torná-lo útil para testadores de penetração.

# Características

 - Gera scripts para a realização de descoberta de **Hosts** na rede interna (Linux e Windows)
 - Gera scripts para a realização de descoberta de **Portas** válidas no host (Linux e Windows)

# Forma de utilização

```sh
python3 sdiscovery.py --ip 192.168.4.0/24 --hd
python3 sdiscovery.py --ip 192.168.4.160 --pd
python3 sdiscovery.py --ip 192.168.4.0/24 --all
```
Isso exibirá a ajuda para a ferramenta. Aqui estão todos os switches que ele suporta:
```yaml
 __    ___ _                                   
/ _\  /   (_)___  ___ _____   _____ _ __ _   _ 
\ \  / /\ / / __|/ __/ _ \ \ / / _ \ '__| | | |
_\ \/ /_//| \__ \ (_| (_) \ V /  __/ |  | |_| |
\__/___,' |_|___/\___\___/ \_/ \___|_|   \__, |
                                         |___/ 
                                         v1.6

options:
  -h, --help            show this help message and exit
  --netblock IP, --ip IP
                        Insert IP
  --pd, --no-pd         Perform port discovery
  --hd, --no-hd         Perform host discovery
  -a, --all, --no-all   Perform post and host discovery
```

# Instalação

Sdiscovery requer **python3** e para baixá-lo só usar:

```sh
git clone https://github.com/joaoviictorti/sdisovery
```

# Executando Sdiscovery

```console
python3 sdiscovery.py --ip 192.168.4.0/24 --hd

 __    ___ _                                   
/ _\  /   (_)___  ___ _____   _____ _ __ _   _ 
\ \  / /\ / / __|/ __/ _ \ \ / / _ \ '__| | | |
_\ \/ /_//| \__ \ (_| (_) \ V /  __/ |  | |_| |
\__/___,' |_|___/\___\___/ \_/ \___|_|   \__, |
                                         |___/ 
                                         v1.6

for a in $(seq 1 255);do ping -c 1 192.168.4.$a;done | grep "64 bytes" >> hosts
```


