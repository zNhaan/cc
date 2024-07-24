import os
import sys,re
import datetime
from datetime import datetime, timedelta
import json
import random
import platform
try:
  import requests
except ImportError:
  os.system('pip install requests')
  import requests
try:
  from colorama import Back, Fore, Fore, Style, init
except ImportError:
  os.system('pip install colorama')
  from colorama import Back, Fore, Fore, Style, init
try:
  from bs4 import BeautifulSoup
except ImportError:
  os.system('pip3 install beautifulsoup4')
  from bs4 import BeautifulSoup





import time
from time import sleep
import json,ast
os.system('clear')

init(autoreset=True)



def pr3(text):
  lines = text.split('\n')
  for line in lines:
      sys.stdout.write(line+'\n')
      sys.stdout.flush()
      sleep(0.1)
def pr(text):
  for i in range(len(text)+1):
      sys.stdout.write("\r" + text[:i])
      sys.stdout.flush()
      sleep(0.01)
  print()

def time():
  current_time = datetime.now()

  time = current_time.strftime("%M:%S")
  return time

def cint(number):
  while True:
    try:
      numbers = int(input(number))
      return numbers
    except ValueError:
      print(f'{red}Vui lòng chỉ nhập số')






def changetoken(red,green,white):
  if os.path.exists("cache_golike_auth.txt"):
    text=f'''{green}BẠN MUỐN DÙNG AUTH CŨ HAY ĐỔI AUTH
{red}[{white}1{red}] ĐỔI AUTH
{red}[{white}2{red}] DÙNG AUTH CŨ'''
    pr3(text)
    changetoken=cint(f'{red}NHẬP LỰA CHỌN: {green}')
    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    if changetoken==1:
      file_name = 'cache_golike_auth.txt'
      if os.path.exists(file_name):
          os.remove(file_name)
    else:
      pass








def banner(red,green,blue,yellow,cyan,pink):
  text=f'''    {Fore.LIGHTWHITE_EX},████████╗███╗   ███╗
     {cyan}╚══██╔══╝██      ██║
     {cyan}   ██║   ██╔████╔██║
     {cyan}   ██║   ██║ ╚═╝ ██║
     {cyan}   ╚═╝   ╚═╝     ╚═╝
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
          ━━━━━━━━━━━━━━━━━━━━━━━━━━━
  {red}CODER:{green}TRINH HUONG      {red}YOUTUBE:{green}Hướng Dev
 {red} FACEBOOK:{green}TRỊNH HƯỚNG     {red}Name:{green}Hướng Đẹp Trai
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'''

  pr3(text)
  text=f'''{red}            ┌───────────────────────┐
{red}            ║ {green}   GOLIKE - TIKTOK  {red}  ║
{red}            └───────────────────────┘
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{red}MỌI NGƯỜI {cyan}CHÚ Ý!!!!
 ~[+]{green}TIỀN SAU KHI LÀM NVỤ SẼ ĐƯỢC CỘNG SAU VÀI PHÚT
 ~[+]{blue}KIỂM TRA KHÔNG THẤY LÊN XU KO PHẢI DO TOOL LỖI
 ~[+]{pink}MÀ DO HỆ THỐNG GOLIKE CHƯA LOAD!!!
 ~[+]{cyan}https://www.facebook.com/profile.php?id=100014053117503
 ~[+]{yellow}CHÚC MỌI NGƯỜI SỬ DỤNG VUI VẺ😘
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'''
  pr3(text)






def checkver():
  url='https://dameconghe7749.blogspot.com/2023/11/version-golike.html'
  ver=bes4(url)
  return ver












def newtool():
    print(f"{magenta}Version 1.3.0")
    url='https://dameconghe7749.blogspot.com/2023/11/newtool-golike.html'
    inversionlink =bes4(url)
    text=f'''{red}~[+]TOOL ĐÃ CÓ PHIÊN BẢN MỚI {green}VERSION 1.3.0!!!!!!
{red}HÃY LÊN CÁC TRANG MXH CỦA{green} Hướng Dev {red}ĐỂ LẤY TOOL
{red}TikTok:{green}Dame Conghe    {red}YOUTUBE:{green}Hướng Dev - Kiếm Tiền Online
  {red}Facebook:{green}Trịnh Hướng
{yellow}HOẶC {red}TRUY CẬP {green}LINK {red}DƯỚI ĐỂ TRỰC TIẾP LẤY TOOL:
🔹🔹🔹🔹{inversionlink}🔸🔸🔸🔸'''
    pr3(text)
    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    text=f'''~[+]{red}XEM VIDEO CÓ TOOL MỚI NHẤT :
~[+]{red}[1] : {green}Youtube
~[+]{red}[2] : {green}TikTok
~[+]{red}[3] : {green}Facebook
~[+]{red}[4] : {green}LẤY TOOL TRỰC TIẾP'''
    pr3(text)

    selec=cint('NHẬP LỰA CHỌN CỦA BẠN:')
    if selec==1:
      url='https://dameconghe7749.blogspot.com/2023/11/yt-golike.html'
      link=bes4(url)
      os.system(f'termux-open-url {link}')
    elif selec==2:
      url='https://dameconghe7749.blogspot.com/2023/11/tiktok-golike.html'
      link=bes4(url)
      os.system(f'termux-open-url {link}')
    elif selec==3:
      url='https://dameconghe7749.blogspot.com/2023/11/fb-golike.html'
      link=bes4(url)
      os.system(f'termux-open-url {link}')
    elif selec==4:
      os.system(f'termux-open-url {inversionlink}')







def bes4(url):
  html_source = requests.get(url).text
  soup = BeautifulSoup(html_source, 'html.parser')
  og_description = soup.find('meta', {'property': 'og:description'})
  if og_description:
      text =og_description['content']
      return text
  else:
      print("Không tìm thấy thẻ meta với thuộc tính property='og:description'")





def checkauth(red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):
 while True :
  while True :
    if not os.path.exists("cache_golike_auth.txt"):
      auth=str(input(f'~[+]{red}NHẬP AUTH:{green} '))
      if auth[:6] != "Bearer":
        auth="Bearer" + auth
      headers ={
    'Authorization'     :auth,
    't':        'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
    'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
 }
      check=json.loads(requests.get('https://gateway.golike.net/api/tiktok-account',headers=headers).text)
      if check['status']==200:
        name=check['data'][0]['username']
        hea={
'Authorization':auth,
't':    'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
}
# Chuỗi JSON đầu vào
        data=requests.get('https://gateway.golike.net/api/statistics/report',headers=hea).text
        try:
          data=json.loads(data)
        except :
          break
        # Tính tổng pending coin
        total_pending_coin = 0
        for key, value in data.items():
            if isinstance(value, dict) and 'pending_coin' in value:
                total_pending_coin += value['pending_coin']
        xht=data['current_coin']
        text=f'~[+]{red}SUCCESS'
        text=f'{red}TÊN TÀI KHOẢN: {green} {name}'
        pr(text)
        text=f'{green}${red} HIỆN TẠI :{green}{xht}đ'
        pr(text)
        # In tổng pending coin
        text=f'{green}${red} CHỜ DUYỆT:{green}{total_pending_coin}đ'
        pr(text)
        print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        text=f'~[+]{red}SELECT {green}ACC CHẠY NHIỆM VỤ '
        pr(text)
        nicknames = [item['nickname'] for item in check['data'] if 'nickname' in item]
        for i, nickname in enumerate(nicknames, start=1):
            globals()[f'{i}'] = nickname
        # In giá trị của các biến
        for i, nickname in enumerate(nicknames, start=1):
            text=f'{red}[{green}{i}{red}]: {globals()[f"{i}"]}'
            pr(text)
        with open("cache_golike_auth.txt", "w") as state_file:
          state_file.write(auth)
        return auth,check
      else:
        text=f'~[+]{red}FAIL AUTH KHÔNG CHÍNH XÁC>>{green}VUI LÒNG NHẬP LẠI'
        continue
    else:
     with open('cache_golike_auth.txt') as f:
        lines = f.readlines()
        auth=lines[0]
        headers ={
      'Authorization'   :auth,
      't':      'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
      'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
      }
        check=json.loads(requests.get('https://gateway.golike.net/api/tiktok-account',headers=headers).text)
        if check['status']==200:
          name =check['data'][0]['username']
          hea={
                'Authorization':auth,
                't':    'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
                'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
                  }


          data=requests.get('https://gateway.golike.net/api/statistics/report',headers=hea).text
          try:
            data=json.loads(data)
          except :
            break
          # Tính tổng pending coin
          total_pending_coin = 0
          for key, value in data.items():
              if isinstance(value, dict) and 'pending_coin' in value:
                  total_pending_coin += value['pending_coin']
          xht=data['current_coin']
          text=f'{red}TÊN TÀI KHOẢN: {green} {name}'
          pr(text)
          text=f'{green}${red} HIỆN TẠI :{green}{xht}đ'
          pr(text)
          # In tổng pending coin
          text=f'{green}${red} CHỜ DUYỆT:{green}{total_pending_coin}đ'
          pr(text)
          nicknames = [item['nickname'] for item in check['data'] if 'nickname' in item]
          for i, nickname in enumerate(nicknames, start=1):
              globals()[f'{i}'] = nickname
          print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
          text=f'~[+]{red}SELECT {green}ACC CHẠY NHIỆM VỤ '
          pr(text)
          # In giá trị của các biến
          for i, nickname in enumerate(nicknames, start=1):
              text=f'{red}[{green}{i}{red}]: {globals()[f"{i}"]}'
              pr(text)

        return auth, check




def get_id_from_nickname_number(ranmau,check,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):
  while True :

    user_input=input(f'~[+]{random.choice(ranmau)}>{random.choice(ranmau)}>{random.choice(ranmau)}> {green}CHỌN ACC TIKTOK MUỐN CHẠY JOB:{green} ')
    try:
      n = int(user_input)
      if 'data' in check and len(check['data']) >= n:
          idtiktok = check['data'][n-1]['id']
          if idtiktok :
              text=f"{red}ID CỦA NICKNAME SỐ {n} LÀ: {green}{idtiktok}"
              pr(text)
              print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
              return idtiktok
          else:
              text=f"{red}KHÔNG TÌM THẤY NICKNAME TƯƠNG ỨNG."
              pr(text)
      else:
          continue
    except ValueError:
          pr(f"{red}VUI LÒNG CHỈ NHẬP SỐ.")
          continue





def getjob(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):
  startmaxjob=1
  job_success=0
  while True :
    while True :
      hea={
      'Authorization':  auth,
     't':       'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
    'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
}

      try:
        a=requests.get(f'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs?account_id={idtiktok}&data=null',headers=hea).json()
      except :
        break
      try:
        link=a['data']['link']
        id=a['data']['id']
        object_id=a['lock']['object_id']
        os.system(f'termux-open-url {link}')
      except :
        break
      for k in range(delay,-1,-1):
        mau=random.choice(ranmau)
        print(f'{green}JOB SUCCESS:{red}[{job_success}/{startmaxjob-1}]{random.choice(ranmau)}LOADING  {random.choice(ranmau)}>> {yellow}NVỤ MỚI SAU {random.choice(ranmau)}>> {random.choice(ranmau)}[{k}s] ',end='\r')
        sleep(1)
      headers = {
          'authorization': auth,
     't':       'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
    'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
}

      json_data = {
          'ads_id': id,
          'account_id': idtiktok ,
          'async': True,
          'data': None,
      }

      g = requests.post(
          'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',
          headers=headers,
          json=json_data,
      ).text
      try:
        g=json.loads(g)
      except :
        break
      if g['status']==200:
        job_success+=1
        print(f'{green}JOB SUCCESS:{red}[{job_success}/{startmaxjob-1}] {cyan}[{time()}] | {random.choice(ranmau)}SUCCESS | {green}FOLLOW | +{g["data"]["prices"]}')
        startmaxjob+=1
        if startmaxjob == maxjob+1:
          print(f'~[+]{pink}ĐÃ ĐẠT MAX JOB. ')
          return
      else:
        print(f'{green}ĐANG KIỂM TRA LẠI TRẠNG THÁI JOB        ',end="\r")
        sleep(1)
        g = requests.post(
          'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',
          headers=headers,
          json=json_data,
      ).text
        try:
          g=json.loads(g)
        except :
          break
        if g['status']==200:
          job_success+=1
          print(f'{green}JOB SUCCESS:{red}[{job_success}/{startmaxjob-1}] {cyan}[{time()}] | {random.choice(ranmau)}SUCCESS | {green}FOLLOW | +{g["data"]["prices"]}')
          startmaxjob+=1
          if startmaxjob == maxjob+1:
            print(f'~[+]{pink}ĐÃ ĐẠT MAX JOB. ')
            return
        if g['status'] !=200:
          print(f'{red}ĐANG BỎ QUA NHIỆM VỤ                   ',end='\r')
          headers = {
              'authorization': auth,
    't':        'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
    'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
}

          json_data = {
              'description': 'Báo cáo hoàn thành thất bại',
              'users_advertising_id': id,
              'type': 'ads',
              'provider': 'tiktok',
              'fb_id': idtiktok ,
              'error_type': 3,
          }

          requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data)


          headers = {
              'authorization': auth,
    't':        'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
    'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
}

          json_data = {
              'ads_id': id,
              'object_id': object_id,
              'account_id': idtiktok ,
              'type': 'follow',
          }
          skipjob=requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',
              headers=headers,
              json=json_data,
          )
          startmaxjob+=1
          if startmaxjob == maxjob+1:
            print(f'~[+]{green}ĐÃ ĐẠT MAX JOB')
            return

def getjob_follow(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):
  startmaxjob=1
  job_success=0
  while True :
    while True :
      hea={
      'Authorization':  auth,
    't':        'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
    'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
}

      try:
        a=requests.get(f'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs?account_id={idtiktok}&data=null',headers=hea).json()
      except :
        break
      try:
        link=a['data']['link']
        id=a['data']['id']
        object_id=a['lock']['object_id']
        if 'video' in link:
          print(f"{red}ĐANG LỌC JOB LIKE                             ",end='\r')
          headers = {
              'authorization': auth,
    't':        'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
    'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
}

          json_data = {
    'description': 'Tôi không muốn làm Job này',
    'users_advertising_id': id,
    'type': 'ads',
    'provider': 'tiktok',
    'fb_id': idtiktok,
    'error_type': 0,
}

          response = requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data)


          json_data = {
    'ads_id': id,
    'object_id': object_id,
    'account_id': idtiktok,
    'type': 'like',
}
          response = requests.post(
    'https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',
    headers=headers,
    json=json_data,
)
        else:
          os.system(f'termux-open-url {link}')
          for k in range(delay,-1,-1):
            mau=random.choice(ranmau)
            print(f'{green}Thành công:{red}[{job_success}/{startmaxjob-1}]{random.choice(ranmau)}LOADING  {random.choice(ranmau)}>> {yellow}NVỤ MỚI SAU {random.choice(ranmau)}>> {random.choice(ranmau)}[{k}s] ',end='\r')
            sleep(1)
          print(f'{red}Đang kiểm tra trạng thái job                ',end='\r')
          headers = {
              'authorization': auth,
        't':    'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
        'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
    }

          json_data = {
              'ads_id': id,
              'account_id': idtiktok ,
              'async': True,
              'data': None,
          }
          try:

            g =requests.post(
            'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',headers=headers,json=json_data).json()
            if g['status']==200:
              job_success+=1
              print(f'{green}JOB SUCCESS:{red}[{job_success}/{startmaxjob-1}] {cyan}[{time()}] | {random.choice(ranmau)}SUCCESS | {green}FOLLOW | +{g["data"]["prices"]}')
              startmaxjob+=1
              if startmaxjob == maxjob+1:
                print(f'~[+]{pink}ĐÃ ĐẠT MAX JOB. ')
                return

            else:
              print(f'{green}ĐANG KIỂM TRA LẠI TRẠNG THÁI JOB                     ',end="\r")
              sleep(1)

              try:
                g = requests.post(
                'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',
                headers=headers,
                json=json_data,
            ).json()
                if g['status']==200:
                  job_success+=1
                  print(f'{green}JOB SUCCESS:{red}[{job_success}/{startmaxjob-1}] {cyan}[{time()}] | {random.choice(ranmau)}SUCCESS | {green}FOLLOW | +{g["data"]["prices"]}')
                  startmaxjob+=1
                  if startmaxjob == maxjob+1:
                    print(f'~[+]{pink}ĐÃ ĐẠT MAX JOB. ')
                    return
                else:
                  print(f'{red}ĐANG BỎ QUA NHIỆM VỤ                   ',end='\r')
                  headers = {
                      'authorization': auth,
            't':        'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
            'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
        }

                  json_data = {
                      'description': 'Báo cáo hoàn thành thất bại',
                      'users_advertising_id': id,
                      'type': 'ads',
                      'provider': 'tiktok',
                      'fb_id': idtiktok ,
                      'error_type': 3,
                  }

                  requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data)


                  headers = {
                      'authorization': auth,
            't':        'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
            'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
        }

                  json_data = {
                      'ads_id': id,
                      'object_id': object_id,
                      'account_id': idtiktok ,
                      'type': 'follow',
                  }
                  skipjob=requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',
                      headers=headers,
                      json=json_data,
                  )
                  startmaxjob+=1
                  if startmaxjob == maxjob+1:
                    print(f'~[+]{green}ĐÃ ĐẠT MAX JOB')
                    return
              except :
                print('Đang thử lại......')
                sleep(1)
          except :
            break
      except:
         break














def creat_key():
  current_time = datetime.now()
  time = current_time.strftime("%F")
  characters_to_choose_from = 'qưertyuiopasdghjklzxcvbnmQWERTYUIOPASDGHJKLZXCVBNM123456789'
  characters = 'qưertyuiopasdghjklzxcvbnmQWERTYUIOPASDGHJKLZXCVBNM123456789'
    # Tạo một chuỗi ngẫu nhiên gồm 5000 ký tự từ danh sách trên
  randoma = ''.join(random.choice(characters_to_choose_from) for _ in range(10))
  end_link = ''.join(random.choice(characters) for _ in range(10))
  dulieu=f'Key-{time}-{randoma}'
  note= f'https://laylinkngon.000webhostapp.com/?text={dulieu}'
  shortlink=requests.get(f"https://web1s.com/api?token=75417134-6914-48a7-a300-36b368de5b46&url={note}").json()
  shortlink=shortlink['shortenedUrl']
  return shortlink,dulieu





#biến
#green='\033[38;5;10m'
blue='\033[38;5;12m'
cyan='\033[38;5;14m'
white='\033[1;39m'
magenta='\033[38;5;5m'
orange='\033[38;5;202m'
xanhnhat = "\033[1;36m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
xduong = "\033[1;34m"
pink = "\033[1;35m"
trang = "\033[1;39m"
whiteb="\033[1;39m"
redb="\033[1;31m"
end='\033[0m'
ranmau=(red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)



def tinhngay(songay):
    time = datetime.now()
    start=time.strftime("%d/%m/%Y")
    end = (time + timedelta(days=int(songay))).strftime("%d/%m/%Y")
    return start, end




def activefile(start,end):

  if not os.path.exists("vipkey.txt"):
   data={
       "start":start,
       "end":end
   }
   with open("vipkey.txt", "w") as state_file:
                  state_file.write(json.dumps(data))

  else:
        with open('vipkey.txt', 'r') as file:
            data_txt = file.read()

        # Phân tích dữ liệu JSON
        try:
            data_json = json.loads(data_txt)
            start_date = data_json.get('start')
            end_date = data_json.get('end')
            return start_date,end_date
        except json.JSONDecodeError:
            print("Dữ liệu không hợp lệ. Vui lòng kiểm tra lại định dạng JSON trong tệp.")

# Tinh ngay va lay la
def ghichu():

    # Sử dụng thư viện requests để tải trang web
    response1 = requests.get('https://ghichu.vn/share/a2d603edc')

    # Kiểm tra xem tải trang thành công hay không (HTTP status code 200 là thành công)
    if response1.status_code == 200:
        # Parse nội dung HTML bằng BeautifulSoup
        soup1 = BeautifulSoup(response1.text, 'html.parser')

        # Tìm thẻ <textarea> bằng class 'content'
        textarea = soup1.find('textarea', {'class': 'content'})

        # Lấy nội dung bên trong thẻ <textarea>
        if textarea:
            data_devices = textarea.string.strip()
            return data_devices
    else:
        print(f'{red}KIỂM TRA KEY CỦA BẠN')

def ngay(chuoi):


    # Tìm vị trí của "vipkey-" trong chuỗi
    vi_tri_vipkey = chuoi.find("Vipkey-")

    if vi_tri_vipkey != -1:
        # Cắt chuỗi từ vị trí sau "vipkey-"
        so_sau_vipkey = chuoi[vi_tri_vipkey + len("Vipkey-"):]

        # Tìm vị trí của "-" trong chuỗi cắt được
        vi_tri_gach_ngang = so_sau_vipkey.find("-")

        if vi_tri_gach_ngang != -1:
            # Lấy số từ chuỗi cắt được
            so = so_sau_vipkey[:vi_tri_gach_ngang]
            return so
        else:
            print("Không tìm thấy ký tự '-' sau 'vipkey-'")
    else:
        print("Không tìm thấy chuỗi 'vipkey-' trong chuỗi")

def input_vipkey(key,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):

        data_devices=ghichu()
          # Sử dụng .string để lấy nội dung và .strip() để loại bỏ khoảng trắng thừa
        if key in data_devices :
           start,end=tinhngay(ngay(key))
           activefile(start,end)
           device_info={
        'system':platform.system(),
        'name':platform.node(),
        "release":platform.release(),
        "machine":platform.machine(),
        "processor":platform.processor() ,
        "time":{
            "start":start,
            "end":end

        }
    }
           headers = {
            'cookie': 'PHPSESSID=ecb3843bfac5ec2c7ba1ee4ed65abc22',

        }

           data = {
            't': data_devices.replace(key,'')+"\n"+str(device_info),
        }

           response = requests.post('https://ghichu.vn/79ng5', headers=headers, data=data)
           print(f'{green}Thành công .Key vip của bạn có thời hạn đến {cyan}{end}')
        else:
           print(f'{red}Kiểm tra key của bạn')
           sleep(9999999999999)




def check_keyvip():
   start,end=activefile('a','b')
   if datetime.now().date() > datetime.strptime(end, "%d/%m/%Y").date():
    print(f"{red}Vip key đã hết hạn")
    print(f'{red}Hãy khởi động lại tool để lấy key free hoặc key vip mới')
    headers = {
    'cookie': 'PHPSESSID=ecb3843bfac5ec2c7ba1ee4ed65abc22',

}
    device_info_dict={
            'system':platform.system(),
            'name':platform.node(),
            "release":platform.release(),
            "machine":platform.machine(),
            "processor":platform.processor() ,
            "time":{
                "start":start,
                "end":end

            }
        }
    data = {
    't': ghichu().replace(str(device_info_dict),''),
}

    response = requests.post('https://ghichu.vn/79ng5', headers=headers, data=data)
    os.remove('vipkey.txt')
    return False
   else:
    device_info_dict={
            'system':platform.system(),
            'name':platform.node(),
            "release":platform.release(),
            "machine":platform.machine(),
            "processor":platform.processor() ,
            "time":{
                "start":start,
                "end":end

            }
        }

    devices_info=ghichu()
    if str(device_info_dict) not in devices_info:
        print(f"{red}Thiết bị của bạn không nằm trong danh sách vip key")
        print(f'{red}Hãy khởi động lại tool để nhập key free hoặc key vip mới')
        os.remove("vipkey.txt")
        return False
    else:
       conlai=(datetime.strptime(end, "%d/%m/%Y").date() - datetime.now().date()).days
       print(f'{green}Bạn còn {cyan}{conlai}{green} ngày để sử dụng key vip')












banner(red,green,blue,yellow,cyan,pink)
  







print(f'{pink}VERSION 1.4.0')
changetoken(red,green,white)
auth,check =checkauth(red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
while True:
      if not os.path.exists("setting_golike.txt"):
        idtiktok =get_id_from_nickname_number(ranmau,check,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
        print(f'''~[+]{red}BẠN CÓ MUỐN LỌC JOB LIKE KHÔNG:
{red}[1]:{green}CÓ
{red}[2]:{green}KHÔNG''')
        select_job=cint(f'{red}NHẬP LỰA CHỌN:{green}')
        delay =cint(f'~[+]{red}NHẬP DELAY: {green}')
        maxjob= cint(f'~[+]{red}NHẬP MAX JOB: {green}')
        setting={
          "loaijob":select_job,
          "delay":delay,
          "maxjob":maxjob
        }
        with open("setting_golike.txt", "w") as file:
    # Ghi dữ liệu vào tệp tin
              file.write(json.dumps(setting))
        print(f'{cyan}KHỞI CHẠY NHIỆM VỤ',end='\r')
        print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        sleep(1)
        if select_job==1:
          getjob_follow(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
        else:
          getjob(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
      else:
          idtiktok =get_id_from_nickname_number(ranmau,check,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
          select_setting=input(f'{green}Bạn có muốn sử dụng setting cũ không?[y/n]{cyan}:' )
          if select_setting == 'n':
             os.remove('setting_golike.txt')
             os.system('clear')
             break

          try:
              with open("setting_golike.txt", "r") as file:
                data_txt=file.read()
                data_json = json.loads(data_txt)
              select_job = int(data_json.get('loaijob'))
              delay = int(data_json.get('delay'))
              maxjob= int(data_json.get('maxjob'))
              print(f'{cyan}KHỞI CHẠY NHIỆM VỤ',end='\r')
              print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
              sleep(1)
              if select_job==1:
                getjob_follow(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
              else:
                getjob(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
          except json.JSONDecodeError:
              print("Dữ liệu không hợp lệ. Vui lòng kiểm tra lại định dạng JSON trong tệp.")

