# -*- coding: utf-8 -*-
__author__="Anil Baran Yelken"
import argparse
import re
import requests
desc="Web Zafiyet Tarama Araci\n"
parser=argparse.ArgumentParser(description=desc)
parser.add_argument("action",help="Action: full xss sql fuzzing e-mail credit link")
parser.add_argument("web_URL",help="URL")
args = parser.parse_args()
url=""
def sql(url,dosyaAdi):
    sqlDosya = open("sqlpayload.txt", "r")
    sqlPayload = sqlDosya.readlines()
    sqlDosya.close()
    if "=" in url:
        deger = str(url).find('=')
        for i in sqlPayload:
            try:
                i = i.split("\n")[0]
                yazi = str(url[0:deger + 1]) + str(i)
                sonuc = requests.get(yazi)
                if int(sonuc.status_code)==200:
                    print "[+]Sqli paylaod: ", str(i)
                    print "[+]Sqli URL: ", yazi
                    rapor=open(dosyaAdi,"a")
                    raporIcerik="[+]Sqli paylaod: "+str(i)+"\n"
                    raporIcerik+="[+]Sqli URL: "+yazi+"\n"
                    rapor.write(raporIcerik)
                    rapor.close()
                else:
                    print "[-]Sqli paylaod: ", str(i)
                    print "[-]Sqli URL: ", yazi
                    rapor=open(dosyaAdi,"a")
                    raporIcerik="[-]Sqli paylaod: "+str(i)+"\n"
                    raporIcerik+="[-]Sqli URL: "+yazi+"\n"
                    rapor.write(raporIcerik)
                    rapor.close()
            except:
                pass
    else:
        print "[-]Sqli yok"
        rapor = open(dosyaAdi, "a")
        raporIcerik = "[-]Sqli yok\n"
        rapor.write(raporIcerik)
        rapor.close()
def xss(url,dosyaAdi):
    xssDosya = open("xsspayload.txt", "r")
    xssPayload = xssDosya.readlines()
    xssDosya.close()
    esittirIndis = url.find("=")
    if "=" in url:
        for i in xssPayload:
            try:
                i = i.split("\n")[0]
                istek = str(url[:esittirIndis + 1]) + str(i)
                icerik = requests.get(istek)
                if i in icerik.content:
                    print "[+]XSS payload: ", str(i)
                    print "[+]XSS URL: ", istek
                    rapor=open(dosyaAdi,"a")
                    raporIcerik="[+]XSS paylaod: "+str(i)+"\n"
                    raporIcerik+="[+]XSS URL: "+istek+"\n"
                    rapor.write(raporIcerik)
                    rapor.close()
                else:
                    print "[-]XSS payload: ", str(i)
                    print "[-]XSS URL: ", istek
                    rapor=open(dosyaAdi,"a")
                    raporIcerik="[-]XSS paylaod: "+str(i)+"\n"
                    raporIcerik+="[-]XSS URL: "+istek+"\n"
                    rapor.write(raporIcerik)
                    rapor.close()
            except:
                pass
    else:
        print "[-]XSS yok"
        rapor = open(dosyaAdi, "a")
        raporIcerik = "[-]XSS yok\n"
        rapor.write(raporIcerik)
        rapor.close()
def crawl(url,dosyaAdi):
    crawlDosya = open("crawl.txt", "r")
    crawlIcerik = crawlDosya.readlines()
    crawlDosya.close()
    for i in crawlIcerik:
        try:
            i = i.split("\n")[0]
            crawlSite = url + str(i)
            istek = requests.get(crawlSite, verify=False)
            if str(istek.status_code) == "200":
                print "[+]Url: ", crawlSite
                rapor = open(dosyaAdi, "a")
                raporIcerik = "[+]Url: "+crawlSite+"\n"
                rapor.write(raporIcerik)
                rapor.close()
            else:
                print "[-]Url: ", crawlSite
                rapor = open(dosyaAdi, "a")
                raporIcerik = "[-]Url: "+crawlSite+"\n"
                rapor.write(raporIcerik)
                rapor.close()
        except:
            pass

def mail(url,dosyaAdi):
    istek = requests.get(url, verify=False)
    sonuc = re.findall(r'[\w.-]+@[\w.-]+.\w+', istek.content)
    for i in sonuc:
        print "[+]E-mail: ", str(i)
        rapor = open(dosyaAdi, "a")
        raporIcerik = "[+]E-mail: "+str(i)+"\n"
        rapor.write(raporIcerik)
        rapor.close()

def credit(url,dosyaAdi):
    istek = requests.get(url, verify=False)
    icerik = str(istek).split()
    icerikSon = str("".join(icerik))
    AMEX = re.match(r"^3[47][0-9]{13}$", icerikSon)
    VISA = re.match(r"^4[0-9]{12}(?:[0-9]{3})?$", icerikSon)
    MASTERCARD = re.match(r"^5[1-5][0-9]{14}$", icerikSon)
    DISCOVER = re.match(r"^6(?:011|5[0-9]{2})[0-9]{12}$", icerikSon)
    try:
        if MASTERCARD.group():
            print "[+]Master Card bulundu!"
            print MASTERCARD.group()
            rapor = open(dosyaAdi, "a")
            raporIcerik = "[+]Master Card bulundu!\n"
            raporIcerik += MASTERCARD.group()+"\n"
            rapor.write(raporIcerik)
            rapor.close()

    except:
        print "[-]Mastercard bulunamadi!"
        rapor = open(dosyaAdi, "a")
        raporIcerik = "[-]Mastercard bulunamadi!\n"
        rapor.write(raporIcerik)
        rapor.close()
    try:
        if VISA.group():
            print "[+]Visa bulundu!"
            print VISA.group()
            rapor = open(dosyaAdi, "a")
            raporIcerik = "[+]Visa bulundu!\n"
            raporIcerik += VISA.group()+"\n"
            rapor.write(raporIcerik)
            rapor.close()
    except:
        print "[-]Visa bulunamadi!"
        rapor = open(dosyaAdi, "a")
        raporIcerik = "[-]Visa bulunamadi!\n"
        rapor.write(raporIcerik)
        rapor.close()
    try:
        if AMEX.group():
            print "[+]AMEX Card bulundu!"
            print AMEX.group()
            rapor = open(dosyaAdi, "a")
            raporIcerik = "[+]AMEX Card bulundu!\n"
            raporIcerik += AMEX.group()+"\n"
            rapor.write(raporIcerik)
            rapor.close()
    except:
        print "[-]AMEX bulunamadi!"
        rapor = open(dosyaAdi, "a")
        raporIcerik = "[-]AMEX bulunamadi!\n"
        rapor.write(raporIcerik)
        rapor.close()
    try:
        if DISCOVER.group():
            print "[+]DISCOVER Card bulundu!"
            print DISCOVER.group()
            rapor = open(dosyaAdi, "a")
            raporIcerik = "[+]DISCOVER Card bulundu!\n"
            raporIcerik += DISCOVER.group()+"\n"
            rapor.write(raporIcerik)
            rapor.close()
    except:
        print "[-]DISCOVER bulunamadi!"
        rapor = open(dosyaAdi, "a")
        raporIcerik = "[-]DISCOVER bulunamadi!\n"
        rapor.write(raporIcerik)
        rapor.close()
def link(url,dosyaAdi):
    isimSayi1 = url.find(".")
    isim = url[isimSayi1 + 1:]
    isimSayi2 = isim.find(".")
    isim = isim[:isimSayi2]
    istek = requests.get(url, verify=False)
    sonuc = re.findall(
        r"""(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))""",
        istek.content)
    for i in sonuc:
        if isim in i:
            print "[+]Links:", i
            rapor = open(dosyaAdi, "a")
            raporIcerik = "[+]Links:"+i+"\n"
            rapor.write(raporIcerik)
            rapor.close()

if args:
    url = getattr(args, 'web_URL')
    print str(url).split("/")[2]
    dosyaAdi=str(url).split("/")[2]+"_rapor.txt"
    rapor=open(dosyaAdi,"a")
    raporIcerik=url+"\n"
    rapor.write(raporIcerik)
    rapor.close()
    print "[+]URL:", url, "\n=========="
    if args.action=="sql":
        sql(url,dosyaAdi)

    elif args.action=="xss":
        xss(url,dosyaAdi)

    elif args.action=="crawl":
        crawl(url,dosyaAdi)

    elif args.action=="e-mail":
        mail(url,dosyaAdi)

    elif args.action=="credit":
        credit(url,dosyaAdi)

    elif args.action=="link":
        link(url,dosyaAdi)

    elif args.action=="full":
        link(url,dosyaAdi)
        crawl(url,dosyaAdi)
        sql(url,dosyaAdi)
        xss(url,dosyaAdi)
        mail(url,dosyaAdi)
        credit(url,dosyaAdi)

    else:
        print "Yanlis secim..."
        exit()
