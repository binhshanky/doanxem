import requests
import random
import string

def randomStringDigits(stringLength=1000):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits)+'\r\n' for i in range(stringLength))
headers = {
    'authority': 'docs.google.com',
    'cache-control': 'max-age=0',
    'origin': 'https://docs.google.com',
    'upgrade-insecure-requests': '1',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'x-client-data': 'CIy2yQEIo7bJAQjEtskBCNG3yQEIqZ3KAQioo8oBCLelygEI4qjKAQiXrcoBCMytygEIvq/KAQ==',
    'sec-fetch-site': 'same-origin',
    'referer': 'https://docs.google.com/forms/d/e/1FAIpQLScKihVViS8rNhfXjfQfX0ExXIpbfP849c4-WEfUNVyrxkB-eg/viewform?fbzx=-6777715044802703220',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'S=spreadsheet_forms=bNhz3UG-gQ2p6KiSIq0x7Zpm33MsSA8I; NID=188=YtdkT2hZNveW-jZfNsx7wHHffjt9GIBavCtE17XGOwVzxzGo9Gy0jReM-0cFSas2blp-NTNzTVTDrOGnVEukry8wBWQuJpT0wahztfxfecF75yMEnJ3k9vo2jy334Iyh8z1TIv5MHykT4KTltKUZbW1i4Htwx5t7iFTu26JTXvE; 1P_JAR=2019-08-25-10',
}
cauChui = ['DoAn TrUaonG TuOsi Losn','DOaN Trusaong tuosai lon', 'di lon ma biet code web' 'asDasOAsdNa Truong Tui Lon']
datasend = cauChui[random.randint(0,3)]+randomStringDigits()

data = {
  'entry.473918781': datasend,
  'fvv': '1',
  'draftResponse': '[null,null,"-6777715044802703220"]\r\n',
  'pageHistory': '0',
  'fbzx': '-6777715044802703220'
}
n = 1000
for i in range(n):
  print(str(i)+'.',' ',' ')
  response = requests.post('https://docs.google.com/forms/d/e/1FAIpQLScKihVViS8rNhfXjfQfX0ExXIpbfP849c4-WEfUNVyrxkB-eg/formResponse', headers=headers, data=data)
  print(response)
 
