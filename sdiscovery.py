import re, argparse
from argparse import BooleanOptionalAction, RawTextHelpFormatter

def menu():

    return '''
 __    ___ _                                   
/ _\  /   (_)___  ___ _____   _____ _ __ _   _ 
\ \  / /\ / / __|/ __/ _ \ \ / / _ \ '__| | | |
_\ \/ /_//| \__ \ (_| (_) \ V /  __/ |  | |_| |
\__/___,' |_|___/\___\___/ \_/ \___|_|   \__, |
                                         |___/ 
                                         v1.6
'''


class Hostdiscovery:

    def __init__(self:object,ip:str):
        self.__ip = ip

    def hostdiscovery(self):
        if re.search("^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.(0)\/(24)$", self.__ip):
            ip = self.__ip.replace(".0/24", "")
            host_discovery = "for a in $(seq 1 255);do ping -c 1 "+ip+".$a;done | grep \"64 bytes\" >> hosts"
            print(host_discovery)

        elif re.search("^[0-9]{1,3}\.[0-9]{1,3}\.(0)\.(0)\/(16)$", self.__ip):
            ip = self.__ip.replace(".0.0/16", "")
            host_discovery = "for a in $(seq 1 255); for b in $(seq 1 255);do ping -c 1 "+ip+".$a.$b;done | grep \"64 bytes\" >> hosts"
            print(host_discovery)
        else:
            print("[+] NÃO É POSSÍVEL FAZER HOST DISCOVERY SEM SER CIDR")


class Portdiscovery():

    def __init__(self:object,ip:str):
        self.__ip = ip

    def portdiscovery(self):
        port_discovery = "for port in {1..65535};do echo >/dev/tcp/"+self.__ip+"/$port && echo \"Port: $port open\" >> ports ||echo;done 2</dev/null"
        print(port_discovery)
    
parser = argparse.ArgumentParser(description=menu(), formatter_class=RawTextHelpFormatter, usage="\npython3 sdiscovery.py --ip 192.168.0.0/24\npython3 sdiscovery.py --ip 192.168.0.0/16\npython3 sdiscovery.py --ip 192.168.0.20")
parser.add_argument('--netblock','--ip', dest='ip', action='store', type=str, help='Insert IP', required=True)
parser.add_argument('--pd','--port-discovery', dest='port_discovery', action=argparse.BooleanOptionalAction)
parser.add_argument('--hd','--host-discovery', dest='host_discovery', action=argparse.BooleanOptionalAction)
parser.add_argument('-a','--all', dest='all', action=BooleanOptionalAction)
args=parser.parse_args()

if __name__ == "__main__":
    if args.host_discovery:
        Hostdiscovery(args.ip).hostdiscovery()
    elif args.port_discovery:
        Portdiscovery(args.ip).portdiscovery()
    elif args.all:
        Hostdiscovery(args.ip).hostdiscovery()
        Portdiscovery(args.ip).portdiscovery()
