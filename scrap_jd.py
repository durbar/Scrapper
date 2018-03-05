import json, time, re, requests, urllib
from bs4 import BeautifulSoup
import time

head = {'accept-language': 'en-US,en;q=0.8,es;q=0.6', 'accept-encoding': 'gzip, deflate, sdch, br', 'accept': '*/*',
        'cookie': 'ppc=; PHPSESSID=n20i6uemfo5f5dfc2m5mejrmf6; TKY=1cce994f83888ec4c21a74e1e6a8beccd1cb5fa271a5fa482c4146fe63fc7b37; _ctk=0b6adf913c7f4ab4388df8df5b4a3c91b30ad7b0132d92fc49cdfa2dd70d9a7e; ppc=/; f5avrbbbbbbbbbbbbbbbb=DCCJGOAKDJDJJMHCMIIHDMLGNHGAPACBNOCOPLMBIAEDOKOFFJIBNHPAIKIAKEBJGEFIEEOHANFMFIPJOHEKJPJENPCBOJDKPICCLDDFFDIBOJHEEHGNHNOHIPDDIJGF; ak_bmsc=3363BAD513AFAF179D24D0BF4089F02A170F21245A26000031754B5A400F953D~plEU4sbcxRQ1to0EXo6ZGGjO53r1dAoWBNxhdxIBJ5kfcpECd53oFlv3ttEnzgcidlmkk4KaIZ+Ruk7aYAJQSskIU0XpdXHZ7ywVj9JNZmKtbtGx+XwHR9v8kbG7e+b5DrVIZzs8EuVf56gx4ZHXgWaiotqLJuObVoucNXWezgeDy4BSCKpRpWopv0i08WOZLpGpkIMrNM1Qtuty0kCSEHw15DOz63j5OnBu6IsinULcI89AWV8FOFDB09VQDg5MsytEd+Hg4iIVbECIXjnwUQcVsD2nOsQNutoZeA+8pFLbLV/IKvxjbL8rKrDZXPtSztgOHTIB+tXQng0rVPjp+w4A==; _ga=GA1.2.1112868149.1514894654; _gid=GA1.2.80582433.1514894654; _gat=1; scity=Chandigarh; usrcity=Chandigarh; inweb_city=Chandigarh; dealBackCity=Chandigarh; main_city=Chandigarh; bm_sv=8ECA266C990F677DBAEBCF4966ED623C~Ou5ni5JdM/lLQ81b82AS+EQ5Ts9TdZUEAQnN0vinL9l6dTLMRs4IZiMtuUSI69CWu9puFls3BrXtL6dLVvhGeOszIMF5QTOcpSwDAxMaS1tCEELo31Vq4STKNkgm/r6DAgIS3+szN/QbGik4AXucF0Wj2D5BDq9BNj1Y5UDcXt4=',
        'authority': 'www.justdial.com',
        'path': '/functions/getRelatedKeywords.php?catid=10212874&type=1&text=Flower%20Shops&area=&key=Florists&city=Chandigarh',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest', 'referer': 'https://www.justdial.com/Chandigarh/Flower-Shops',
        'scheme': 'https', 'method': 'GET'}
url = [
    'http://www.justdial.com/Surat/Flower-Shops/page-',
    'http://www.justdial.com/Surat/Hardware-Shops/page-',
    'http://www.justdial.com/Surat/Hardware-Dealers/page-',
    'http://www.justdial.com/Surat/Hardware-Wholesalers/page-',
    'http://www.justdial.com/Surat/Hardware-Material-Dealers/page-',
    'http://www.justdial.com/Surat/Mineral-Water-Distributors/page-',
    'http://www.justdial.com/Surat/Pharmaceutical-Distributors/page-',
    'http://www.justdial.com/Surat/Coco-Cola-Soft-Drink-Distributors/page-',
    'http://www.justdial.com/Surat/Soft-Drink-Distributors/page-',
    'http://www.justdial.com/Surat/Newspaper-Distributors/page-',
    'http://www.justdial.com/Surat/Medicine-Distributors/page-',
    'http://www.justdial.com/Surat/FMCG-Product-Distributors/page-',
    'http://www.justdial.com/Surat/Standy-Wholeseller/page-',
    'http://www.justdial.com/Surat/Shoe-Dealers/page-',
    'http://www.justdial.com/Surat/Grocery-Stores/page-',
    'http://www.justdial.com/Surat/Grocery-Wholesalers/page-',
    'http://www.justdial.com/Surat/Grocery-Home-Delivery-Services/page-',
    'http://www.justdial.com/Surat/Grocery-Distributors/page-',
    'http://www.justdial.com/Surat/Printers/page-',
    'http://www.justdial.com/Surat/Printer-Dealers/page-',
    'http://www.justdial.com/Surat/Stationery-Wholesalers/page-',
    'http://www.justdial.com/Surat/Vegetable-Wholesalers/page-',
    'http://www.justdial.com/Surat/Dry-Fruit-Wholesalers/page-',
    'http://www.justdial.com/Surat/Gift-Retailers/page-',
    'http://www.justdial.com/Surat/Homeopathic-Medicine-Retailers/page-',
    'http://www.justdial.com/Surat/Allopathic-Medicine-Retailers/page-',
    'https://www.justdial.com/Surat/Sports-Goods-Dealers/page-',
    'https://www.justdial.com/Surat/Pet-Shops/page-',
    'https://www.justdial.com/Surat/Book-Shops/page-'
]
# city = ['Delhi-NCR', 'Chandigarh', 'Bengaluru', 'Bhopal', 'Bhubaneshwar', 'Coimbatore', 'Faridabad', 'Guwahati',
#         'Indore', 'Jaipur', 'Jodhpur', 'Mysore', 'Nagpur', 'Pune', 'Surat', 'Vadodara']
city = ['Hyderabad', 'Delhi-NCR', 'Pune', 'Chandigarh']
sol = []

number_mapping = {
    "icon-dc": "+",
    "icon-fe": "(",
    "icon-hg": ")",
    "icon-ba": "-",
    "icon-yz": "1",
    "icon-wx": "2",
    "icon-vu": "3",
    "icon-ts": "4",
    "icon-rq": "5",
    "icon-po": "6",
    "icon-nm": "7",
    "icon-lk": "8",
    "icon-ji": "9",
}

#'Delhi, Noida, Ghaziabad, Gurgaon, Hyderabad and Pune'
for c in city:
    for li in url:
        nurl = li.split('Surat')
        nurl = nurl[0]+str(c)+nurl[1]

        for page in range(1, 3):

            tempUrl = nurl + str(page)
           
            r = requests.get(tempUrl, headers=head)

            soup = BeautifulSoup(r.content, "html.parser")
            g_data = soup.find_all("div", {"class": "store-details"})

            if not len(g_data):
                continue

            for element in range(len(g_data)):
                temp = {}

                temp['vendor_name'] = g_data[element].find_all("h4", {"class": "store-name"})[0].find_all("a")[0].text

                try:
                    ven_phone = ""
                    ven_phone_spans = g_data[j].find_all("p", {"class": "contact-info "})[0].find_all('span', {'class': 'mobilesv'})

                    for sp in ven_phone_spans:
                        ven_phone += number_mapping[sp.attrs['class'][1]]

                except Exception :
                    ven_phone = 'NA'
                temp['phone'] = str(ven_phone)

                try:
                    addr = g_data[element].find_all("span", {"class": "desk-add jaddt"})[0].find_all("a", {'class':'morehvr'})[0].text
                    addr = re.sub("\s\s+", " ", addr)
                    #addr = addr.encode('utf-8').split('.')
                    temp['address'] = addr[-1]
                except Exception:
                    temp['address'] = 'NA'

                try:
                    a = g_data[element].find_all("span", {"class": "margin0 addrinftxt"})[0].find_all("a")
                    catList = []
                    for cat in range(len(a)):
                        if (a[cat].get("title")) is not None:
                            catList.append(a[cat].get("title"))

                    temp['category'] = catList
                except Exception:
                    temp['types'] = 'NA'

                temp['city'] = str(c)
                temp['Source'] = 'JustDial'
                temp['category'] = li.split('/')[-2]
                sol.append(temp)
        time.sleep(1)
        with open('justdial_csv/justdial_' + str(c) + str(li.split('/')[-2]) + '.json', 'w') as outfile:
            json.dump(sol, outfile)
        sol = []


        break

with open('justdial' + '.json', 'w') as outfile:
    json.dump(sol, outfile)

