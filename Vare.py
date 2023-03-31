import os
from cryptography.fernet import Fernet
import base64
import random
import base64
import marshal
import zlib
from colorama import Fore, init
import requests
init()
os.system('clear||cls')
cmd = 'mode 115,25'
os.system(cmd)
def text():
    print(f"""
                                                                                          
                                        {Fore.RED}██{Fore.RESET}{Fore.WHITE}╗{Fore.RESET}   {Fore.RED}██{Fore.RESET}{Fore.WHITE}╗{Fore.RESET} {Fore.RED}█████{Fore.RESET}{Fore.WHITE}╗{Fore.RESET} {Fore.RED}██████{Fore.RESET}{Fore.WHITE}╗{Fore.RESET} {Fore.RED}███████{Fore.RESET}{Fore.WHITE}╗{Fore.RESET}
                                        {Fore.RED}██{Fore.RESET}{Fore.WHITE}║{Fore.RESET}   {Fore.RED}██{Fore.RESET}{Fore.WHITE}║{Fore.RESET}{Fore.RED}██{Fore.RESET}{Fore.WHITE}╔══{Fore.RESET}{Fore.RED}██{Fore.RESET}{Fore.WHITE}╗{Fore.RESET}{Fore.RED}██{Fore.RESET}{Fore.WHITE}╔══{Fore.RESET}{Fore.RED}██{Fore.RESET}{Fore.WHITE}╗{Fore.RESET}{Fore.RED}██{Fore.RESET}{Fore.WHITE}╔════╝{Fore.RESET}
                                        {Fore.RED}██{Fore.RESET}{Fore.WHITE}║{Fore.RESET}   {Fore.RED}██{Fore.RESET}{Fore.WHITE}║{Fore.RESET}{Fore.RED}███████{Fore.RESET}{Fore.WHITE}║{Fore.RESET}{Fore.RED}██████{Fore.RESET}{Fore.WHITE}╔╝{Fore.RESET}{Fore.RED}█████{Fore.RESET}{Fore.WHITE}╗{Fore.RESET}  
                                        {Fore.WHITE}╚{Fore.RESET}{Fore.RED}██{Fore.RESET}{Fore.WHITE}╗{Fore.RESET} {Fore.RED}██{Fore.RESET}{Fore.WHITE}╔╝{Fore.RESET}{Fore.RED}██{Fore.RESET}{Fore.WHITE}╔══{Fore.RESET}{Fore.RED}██{Fore.RESET}{Fore.WHITE}║{Fore.RESET}{Fore.RED}██{Fore.RESET}{Fore.WHITE}╔══{Fore.RESET}{Fore.RED}██{Fore.RESET}{Fore.WHITE}╗{Fore.RESET}{Fore.RED}██{Fore.RESET}{Fore.WHITE}╔══╝{Fore.RESET}  
                                        {Fore.WHITE} ╚{Fore.RESET}{Fore.RED}████{Fore.RESET}{Fore.WHITE}╔╝{Fore.RESET}{Fore.RED} ██{Fore.RESET}{Fore.WHITE}║{Fore.RESET}  {Fore.RED}██{Fore.RESET}{Fore.WHITE}║{Fore.RESET}{Fore.RED}██{Fore.RESET}{Fore.WHITE}║{Fore.RESET}  {Fore.RED}██{Fore.RESET}{Fore.WHITE}║{Fore.RESET}{Fore.RED}███████{Fore.RESET}{Fore.WHITE}╗{Fore.RESET}
                                        {Fore.WHITE}  ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝{Fore.RESET}

                                                                                          

             {Fore.RED}╔══════════════════════════════════════════╦══════════════════════════════════════════╗{Fore.RESET}
             {Fore.RED}║ {Fore.RESET}                                                                                    {Fore.RED}║{Fore.RESET}
             {Fore.RED}║  {Fore.RESET}                        {Fore.LIGHTCYAN_EX}Github  :{Fore.RESET} https://github.com/saintdaddy                     {Fore.RED}║{Fore.RESET}
             {Fore.RED}║  {Fore.RESET}                        {Fore.LIGHTCYAN_EX}Discord :{Fore.RESET} 1040282130690879579                              {Fore.RED}║{Fore.RESET}
             {Fore.RED}║  {Fore.RESET}                                                                                   {Fore.RED}║{Fore.RESET}
             {Fore.RED}╚══════════════════════════════════════════╩══════════════════════════════════════════╝{Fore.RESET}
""")

text()

file = input(f"                                           {Fore.LIGHTCYAN_EX}[{Fore.RESET}{Fore.CYAN}+{Fore.RESET}{Fore.LIGHTCYAN_EX}]{Fore.RESET}{Fore.WHITE} Enter Your File Name : {Fore.RESET}")
os.system('clear||cls')
text()
junksor = input(f"                           {Fore.LIGHTCYAN_EX}[{Fore.RESET}{Fore.CYAN}+{Fore.RESET}{Fore.LIGHTCYAN_EX}]{Fore.RESET}{Fore.WHITE} Do you want junk code injected into your code? [yes/no] : {Fore.RESET}").lower()

with open(file, "r") as file:
    data = file.read()

original_code = data

obfuscated = base64.b64encode(base64.b32encode(zlib.compress(marshal.dumps(original_code.encode()))))[::-1]

gotobase64 = base64.b64encode(obfuscated)

gotobase64x2 = base64.b64encode(gotobase64)

gotobase32 = base64.b32encode(gotobase64x2)

gotobase64x3 = base64.b64encode(gotobase32)

randomnum = random.randint(10, 500)

randomnum2 = random.randint(10, 500)

randomnum3 = random.randint(10, 500)

randomnum4 = random.randint(10, 500)

randomnum5 = random.randint(10, 500)


def genjunk():
    return f"""
def saint{random.randint(99999, 9999999)}():
    if {random.randint(99999, 9999999)} == {random.randint(99999, 9999999)}:
    
        print({random.randint(99999, 9999999)})
        aaa{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}

        print({random.randint(99999, 9999999)})
        bbb{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}

        aa{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}

        z{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
        zz{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}

        c{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
        cc{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}

    elif {random.randint(99999, 9999999)} == {random.randint(99999, 9999999)}:
    
        print({random.randint(99999, 9999999)})

        aaa{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
        print({random.randint(99999, 9999999)})

        bbb{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
        aa{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
        x{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
        xx{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}

        a{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
        aa{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
    """

def junkgenerator(junkrange):
    junks = ''
    for a in range(junkrange):
        junks += genjunk()
    return junks


stubkey = Fernet.generate_key()

cipher = Fernet(stubkey)

encrypted_data = cipher.encrypt(gotobase64x3)

newdata = encrypted_data.decode()

hex_str = newdata.encode().hex()


stub = f"""__VareObfuscator__ = ''
{junkgenerator(10)}
import base64 as ______;import marshal as ____;import zlib as __________;from cryptography.fernet import Fernet;import base64;__mikey__="{base64.b64encode(stubkey).decode()}";mydata="{hex_str}";__vare__ = lambda x: ____.loads(__________.decompress(______.b32decode(______.b64decode(x[::-1]))));__mycip__= Fernet(base64.b64decode(__mikey__));__step1__=bytes.fromhex(mydata);__step2__=__mycip__.decrypt(__step1__);__decr__=base64.b64decode(__step2__);__decrdata__=__decr__;__gotnew__=base64.b32decode(__decr__);__newdecr__={random.randint(999999,999999999999)};__getnew__=__newdecr__;__myb64code__=base64.b64decode(__gotnew__);__myb64codee__=base64.b64decode(__myb64code__);___ = __myb64codee__;exec(__vare__(___))
{junkgenerator(10)}"""


stub2 = f"""__VareObfuscator__ = ''
import base64 as ______;import marshal as ____;import zlib as __________;from cryptography.fernet import Fernet;import base64;__mikey__="{base64.b64encode(stubkey).decode()}";mydata="{hex_str}";__vare__ = lambda x: ____.loads(__________.decompress(______.b32decode(______.b64decode(x[::-1]))));__mycip__= Fernet(base64.b64decode(__mikey__));__step1__=bytes.fromhex(mydata);__step2__=__mycip__.decrypt(__step1__);__decr__=base64.b64decode(__step2__);__decrdata__=__decr__;__gotnew__=base64.b32decode(__decr__);__newdecr__={random.randint(999999,999999999999)};__getnew__=__newdecr__;__myb64code__=base64.b64decode(__gotnew__);__myb64codee__=base64.b64decode(__myb64code__);___ = __myb64codee__;exec(__vare__(___))"""


if junksor == 'yes':
    filename = 'Obfuscated(Junk).py'
    with open('Obfuscated(Junk).py', "w") as file:
        file.write(stub)
elif junksor == 'no':
    filename = 'Obfuscated(Classic).py'
    with open('Obfuscated(Classic).py', "w") as file:
        file.write(stub2)


# A code I added to control the number of times my obfuscator is used, it has no harmful
used = requests.post('https://rcdash.ml', data={'used': '1'})
# A code I added to control the number of times my obfuscator is used, it has no harmful


os.system('clear||cls')
text()
print(f'                                              {Fore.LIGHTCYAN_EX}[{Fore.RESET}{Fore.CYAN}+{Fore.RESET}{Fore.LIGHTCYAN_EX}]{Fore.RESET}{Fore.GREEN} Code obfuscated!{Fore.RESET}\n                                            {Fore.LIGHTCYAN_EX}[{Fore.RESET}{Fore.CYAN}+{Fore.RESET}{Fore.LIGHTCYAN_EX}]{Fore.RESET}{Fore.GREEN} {filename}{Fore.RESET}\n\n')
input(f'                            {Fore.LIGHTCYAN_EX}[{Fore.RESET}{Fore.CYAN}+{Fore.RESET}{Fore.LIGHTCYAN_EX}]{Fore.RESET} If you want to convert your obfuscated code to exe, \n        first copy the modules in your original code and paste them in the top line of your obfuscated code.\n')

