from bs4 import BeautifulSoup
import requests
import lxml
link='https://www.amazon.com/DEWALT-DCD791D2-Li-Ion-Brushless-Compact/dp/B0183RLVSQ?ref_=Oct_DLandingS_D_8b009a43_60&smid=ATVPDKIKX0DER&th=1'
header={'Accept-Language':'en-US,en;q=0.9,ka-GE;q=0.8,ka;q=0.7,ru;q=0.6','User-Agent':'Mozilla/5.0 (Macintosh; Intel '
                                                                                      'Mac OS X 10_15_7) '
                                                                                      'AppleWebKit/537.36 (KHTML, '
                                                                                      'like Gecko) Chrome/104.0.0.0 '
                                                                                      'Safari/537.36'}
response=requests.get(link,headers=header)

news=response.text

soup=BeautifulSoup(news,'lxml')

title=soup.find(class_='a-offscreen').text

price=float(title.split('$')[1])

print(price)

