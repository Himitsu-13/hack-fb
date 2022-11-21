#!/usr/bin/python3


try:
    import requests, bs4, json, os, sys, random, datetime, time, re, urllib3, base64, rich
except ImportError as err:
    message = f'''
    import error : { err }
    installing requirements modules...
    '''
    print(message)
    os.system('pip install -r requirements.txt')
    
from rich.table import Table as table
from rich.console import Console
from bs4 import BeautifulSoup as Parser
from concurrent.futures import ThreadPoolExecutor as thread
from rich.console import Group
from rich.panel import Panel
from rich import print as log
from rich.markdown import Markdown as MD
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text
from datetime import datetime

# import libraries 
# from bruteforce.lib import File

# install pretty
pretty.install()

# pathFiles (result)
currentDirectory = os.path.dirname(__file__)
pathFiles = "./brute_files"
pathResults = "./brute_results"

# version
version = "0.1.0"

# COLORS

x = '\33[m' # DEFAULT

k = '\033[93m' # KUNING
kk = '\033[33m' # KUNING
h = '\x1b[1;92m' # HIJAU
hh = '\033[32m' # HIJAU
u = '\033[95m' # UNGU
b = '\33[1;96m' # BIRU
p = '\x1b[0;34m' # BIRU

# auth variabel
auth = None

# declare variabel
___PUBLIC___ = []

# session
session = requests.Session()

class Auth:
    def __init__(self, token, cookie):
        self.token = token
        self.cookie = cookie
    def user(self):
        res = requests.get('https://graph.facebook.com/me?fields=id,name&access_token=' + self.token, cookies={'cookie': self.cookie })
        return json.loads(res.text)
        
        
def save(pathfile, content):
    try:
        with open(pathfile, "w") as file:
            file.write(content)
            file.close()
    except Exception as e:
        print(f"""
        { k }Failed Save File{ x } at { pathfile }
        { p }Reference :{ x } { e }
        """)
        exit()
def clear():
    os.system('clear')
def now():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")
def warn(text):
    print(f"{ x }[{ k }*{ x }] { text }")
def inputText(text):
    return input(f'{ x }[{ b }<>{ x }] { text } : ')
def success(text):
    print(f"{ x } [{ h }•{ x }] { text }")
def info(text):
    print(f"{ x }[{ b }!{ x }] { text }")
def question(text):
    i = input(f"{ x }[{ u }?{ x }] { text } (y/n):")
    if i == "y" or i == "no":
        return True
    elif i == "n" or i == "no":
        return False
    else:
        warn("invalid answer !")
        question(text)
def login(token, cookie):
    sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':kukis})
    userName = json.loads(sy.text)['name']
    userId = json.loads(sy.text)['id']
    menu(userName, userId)
def clearCredentials():
    os.system(f'rm -rf { pathFiles }/.token')
    os.system(f'rm -rf { pathFiles }/.cookie')
    warn("logged out!")
    exit()
def logout():
    if question("You will be Logout, Are you Sure ?"):
        if question("delete cookie ?"):
            clearCredentials()
        else:
            info("logged out, without delete cookie")
            info("good bye ^_^")
            exit()
    else:
        menu()
def clear_result():
    os.system(f"rm -rf { pathResults }")
    if question("are you sure"):
        info("all results has been deleted!")
    else:
        info("canceled operation!")
        menu()
        
def banner():
    clear()
    wel='# WELCOME TO Facebook Bruteforce'
    cik2=MD(wel ,style='red')
    Console().print(cik2)
    ban=f'''
    ░█▀▀░█░█░█▀▀░▀█▀░█▀█░█▀▄░█▀█░▀█▀░█▀█░█▀▄░█▀▀
    ░▀▀█░░█░░▀▀█░░█░░█░█░█░█░█▀█░░█░░█░█░█▀▄░▀▀█
    ░▀▀▀░░▀░░▀▀▀░▀▀▀░▀░▀░▀▀░░▀░▀░░▀░░▀▀▀░▀░▀░▀▀▀   
    
    Bruteforce v{ version }
    '''
    oi = Panel(Text(ban,justify='center',style='bold'), style='yellow')
    Console().print(Panel(oi, title='[bold white] • DEVELOVER INFORMATION • [/bold white]'))

def menu():
    global auth
    try:
        ip = requests.get('https://httpbin.org/ip').json()
    except:
        ip = {'origin':'-'}
    
    banner()
    try:
        user = auth.user()
        sg = '# USER ACCOUNT INFORMATION'
        fx = MD(sg, style='red')
        Console().print(fx)
        success(f'ACTIVE USER : { user["name"] }')
        success(f'USER ID  TUMBAL : { user["id"] }')
        success(f'IP ADDRESS : { ip["origin"] }')
    except Exception as e:
        warn("login failed")
        exit()
        
    io = '''
      [bold red]
      [00] LOGOUT
      [01] PUBLIC FRIENDS	    
      [02] BRUTEFORCE TARGET
      [03] FOLLOWER		     
      [04] LIKES THE POST	     
      [05] GROUP MEMBERS           
      [06] CRACK FROM FILES
      [07] CHECKPOINT OPTIONS
      [08] CHECK CRACK RESULTS
      [09] CLEAR RESULTS
      [10] DUMP COMMENTS
      [bold red]
      '''
    oi = Panel(io, style='blue')
    Console().print(Panel(oi, title='[bold red] • MENU CRACK • [/bold red]'))
    ec = input(x+'['+p+'<>'+x+'] Pilih : ')
    if ec in ['1','01']:
    	dump_public()
    elif ec in ['2','02']:
    	hack_massal()
    elif ec in ['3','03']:
    	dump_pengikut()
    elif ec in ['4','04']:
    	dump_likes()
    elif ec in ['5','05']:
    	dump_grup()
    elif ec in ['6','06']:
    	crack_file()
    elif ec in ['7','07']:
    	file()
    elif ec in ['8','08']:
    	result()
    elif ec in ['9','09']:
    	clear_result()
    elif ec in ['0','00']:
    	logout()
    elif ec in ['10']:
    	dump_comments()
    else:
    	ric = '# OPTION NOT IN THE MENU'
    	Console().print(MD(ric, style='red'))
    	menu()

def generateUserAgent():
    arr = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
    b=random.randrange(100, 9999)
    c=random.randrange(100, 9999)
    d=random.choice(arr)
    e=random.choice(arr)
    f=random.choice(arr)
    g=random.choice(arr)
    h=random.randrange(1, 9)
    i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
    return f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'


def getProxy():
    try:
        proxy = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
        save(f"{ pathFiles }/proxy.txt", proxy)
    except Exception as e:
        with open(f"{ pathFiles }/.proxy", 'r') as file:
              proxy = file.read().splitlines()
              file.close()
    return proxy

def getCookie(option = "input"):
    global auth
    try:
        banner()
        if option == "file" and os.path.exists(f'{ pathFiles }/.cookie'):
            with open(f'{ pathFiles }/.cookie', 'r') as file:
                ___cookie___ = file.read()
                file.close()
        else:
            ___cookie___ = input(f'{ x }[{ b }>{ x }]{ p } Masukkan Cookies : { x }')
        data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":___cookie___}) 
        ___token___ = re.search("(EAAG\w+)", data.text).group(1)
        
        # save cookie and token
        save(f"{ pathFiles }/.token", ___token___)
        save(f"{ pathFiles }/.cookie", ___cookie___)
        
        # login
        auth = Auth(___token___, ___cookie___)
        
        # show menu
        menu()
    except Exception as e:
        print(e)
        warn('EXPIRED COOKIES / CP ACCOUNT ')
        exit()
def getTokens():
    token = ""
    with open(f'{ pathFiles }/.token', 'r') as file:
        token = file.read()
        file.close()
    return token

# dump massal
def dump_public():
    global auth, ___PUBLIC___
    win = 'DUMP PUBLIC ID'
    win2 = MD(win, style='red')
    Console().print(win2)
    info('TYPE "me" IF YOU WANT TO DUMP FROM YOUR FRIENDS')
    uid = inputText("INPUT TARGET ID")
    try:
        res = requests.get(f'https://graph.facebook.com/v1.0/{ uid }?fields=friends.limit(5000)&access_token={ auth.token }',cookies={'cookie': auth.cookie }).json()
        for friend in res['friends']['data']:
            try:
                data = {}
                for key in friend:
                    data[key] = friend[key]
                    success(f"{ friend['id'] }{ p }|{ x }{ friend['name'] }")
                else:
                    pass
                ___PUBLIC___.append(data)
            except:
                continue
        else:
            pass
        path = f"{ pathFiles }/dump_public_{ now() }.json"
        save(path, json.dumps(___PUBLIC___))
        info(f'TOTAL DUMP ID : { len(___PUBLIC___) }')
        info(f"Saved file at { path }")
        
        # back to menu
        if question("back to Main Menu ?"):
            menu()
        else:
            logout()
        
        # ReAssign to Null
        ___PUBLIC___ = []
        # setting()
    except requests.exceptions.ConnectionError:
        li = 'PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
        lo = MD(li, style='red')
        Console().print(lo, style='red')
        dump_public()
    except (KeyError,IOError):
        teks = 'NOT PUBLIC FRIENDSHIP OR BROKEN TOKEN'
        teks2 = MD(teks, style='red')
        Console().print(teks2)
        exit()
def hack_massal():
    pass
def dump_pengikut():
    pass
def dump_grup():
    pass
def dump_likes():
    pass
def crack_file():
    pass
def file():
    pass
def result():
    pass
def tipsx():
    pass
def dump_comments(text = ""):
    global auth, session
    if not text == "":
        postId = text
    else:
        postId = inputText("Masukan id postingan")
    url = f'https://mbasic.facebook.com/{ postId }'
    data = Parser(session.get(url).text, "html.parser")
    dump = []
    tempId = []
    # print(data.find_all("h3"))
    # exit()
    try:
        
        author = data.find("h3", {"class": "bt"}).text
        authorId = data.find("h3", {"class": "bt"}).find("a")[0].get("href").split('=')[1].replace("&eav","")
        comments = data.find_all("div", {"class": "ej"})
        for comment in comments:
            name = comment.find("h3").text
            id = comment.find("h3").find("a").get("href").split('=')[1].replace("&eav","")
            commentText = comment.find("div", {"class": "el"}).text
            commentId = comment.get("id")
            if id in tempId:
                pass
            else:
                dump.append({
                  "name": name,
                  "id": id,
                  "comment": commentText,
                  "commentId": commentId
                })
                success(f"{ name } | { id }")
            info(f"Author post : { author }")
            info(f"process dump comments ...")
        else:
            warn("comments not found!")
        if question("Back to Main Menu ?"):
            menu()
        else:
            logout()
    except Exception as e:
        warn(e)
        exit()
        
def Bruteforce():
    global userAgent, proxy, princp, session, cookie
    
    # generate folders
    if not os.path.exists(f"{ pathResults }"):
        try:
            os.makedirs(f"{ pathFiles }")
            os.makedirs(f"{ pathResults }/CP")
            os.makedirs(f"{ pathResults }/OK")
            os.makedirs(f"{ pathResults }/DUMP")
        except Exception as e:
            print(f'''
            error : { e }
            can't generate folder at { pathResults }
            ''')
            exit()
    if not os.path.exists(f"{ pathFiles }"):
        try:
            os.makedirs(f"{ pathFiles }")
        except Exception as e:
            print(f'''
            error : { e }
            can't generate folder at { pathResults }
            ''')
            exit()
    # get cookie
    try:
        # initialize variabels
        cookie = getCookie("file")
        userAgent = generateUserAgent()
        princp = []
        proxy = getProxy()
    except Exception as e:
        cookie = getCookie()
        print(e)
        exit()
    
    
  

if __name__=='__main__':
    pass