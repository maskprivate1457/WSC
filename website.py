import requests,os,re,bs4,sys,json,string,random
from rich.panel import Panel as panel
from rich.panel import Panel as nel
from rich import print as cetak

Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

warna = ['[#FF0000]','[#00FF00]','[#00C8FF]','[#AF00FF]','[#FF00FF]','[#00FFFF]','[#FFFFFF]','[#FF8F00]','[#AAAAAA]']
for i in range(10):
    jadi_aungthor = random.choice(warna)
    
def tutorial():
        cetak(panel(f"""{jadi_aungthor}\t\t         __      __  __________________  
{jadi_aungthor}\t\t        /  \    /  \/   _____/\_   ___ \ 
{jadi_aungthor}\t\t        \   \/\/   /\_____  \ /    \  \/ 
{jadi_aungthor}\t\t         \        / /        \\     \____
{jadi_aungthor}\t\t          \__/\  / /_______  / \______  /
{jadi_aungthor}\t\t               \/          \/         \/ 
\t\t              {K2}Website {H2}Scraper {M2}Contacts
             """,width=100,padding=(0,8),title=f"{M2}▪︎{K2}▪︎{H2}▪︎{K2}LOGO AUNGTHOR{H2}▪︎{K2}▪︎{M2}▪︎",title_align='center',style=f"bold green"))

def menjadi_aungthor():
	try:
		os.system('xdg-open https://youtube.com/@TutorialTermux?si=_cE6fr-T2xCq_FCR')
		os.system('clear')
		tutorial()
		url = "https://website-contacts-scraper.p.rapidapi.com/scrape-contacts"
		cetak(panel(f"\t      {K2}MASUKKAN {H2}DOMAIN {K2}ATAU {H2}SUBDOMAIN {K2}, CONTOH = {H2}google.com {P2}atau {H2}dpr.go.id",width=100,style="bold green"))
		doma = input("\33[m[\x1b[1;92m?\33[m] MASUKKAN DOMAIN > \x1b[1;92m")
		querystring = {"query":doma,"match_email_domain":"false","external_matching":"false"}
		headers = {"X-RapidAPI-Key": "8080d931f8msh91f3d34ca32c57ep1b295ajsnd444f721d918","X-RapidAPI-Host": "website-contacts-scraper.p.rapidapi.com"}
		response_aungthor = requests.get(url, headers=headers, params=querystring).text
		begal = json.loads(response_aungthor)
		try:facebook = begal['data'][0]['facebook']
		except KeyError:facebook = ('-')
		try:instagram = begal['data'][0]['instagram']
		except KeyError:instagram = ('-')
		try:tiktok = begal['data'][0]['tiktok']
		except KeyError:tiktok = ('-')
		try:snapchat = begal['data'][0]['snapchat']
		except KeyError:snapchat = ('-')
		try:twitter = begal['data'][0]['twitter']
		except KeyError:twitter = ('-')
		try:linkedin = begal['data'][0]['linkedin']
		except KeyError:linkedin = ('-')
		try:github = begal['data'][0]['github']
		except KeyError:github = ('-')
		try:youtube = begal['data'][0]['youtube']
		except KeyError:youtube = ('-')
		try:pinterest = begal['data'][0]['pinterest']
		except KeyError:pinterest = ('-')
		try:emails0 = begal['data'][0]['emails'][0]['value']
		except KeyError:emails0 = ('-')
		try:source0 = begal['data'][0]['emails'][0]['sources'][0]
		except KeyError:source0 = ('-')
		try:source1 = begal['data'][0]['emails'][0]['sources'][1]
		except KeyError:source1 = ('-')
		try:source2 = begal['data'][0]['emails'][0]['sources'][2]
		except KeyError:source2 = ('-')
		try:emails1 = begal['data'][0]['emails'][1]['value']
		except KeyError:emails1 = ('-')
		try:source3 = begal['data'][0]['emails'][1]['sources'][0]
		except KeyError:source3 = ('-')
		try:emails2 = begal['data'][0]['emails'][2]['value']
		except KeyError:emails2 = ('-')
		try:source4 = begal['data'][0]['emails'][2]['sources'][0]
		except KeyError:source4 = ('-')
		try:emails3 = begal['data'][0]['emails'][3]['value']
		except KeyError:emails3 = ('-')
		try:source5 = begal['data'][0]['emails'][3]['sources'][0]
		except KeyError:source5 = ('-')
		try:emails4 = begal['data'][0]['emails'][4]['value']
		except KeyError:emails4 = ('-')
		try:source6 = begal['data'][0]['emails'][4]['sources'][0]
		except KeyError:source6 = ('-')
		try:emails5 = begal['data'][0]['emails'][5]['value']
		except KeyError:emails5 = ('-')
		try:source7 = begal['data'][0]['emails'][5]['sources'][0]
		except KeyError:source7 = ('-')
		try:emails6 = begal['data'][0]['emails'][6]['value']
		except KeyError:emails6 = ('-')
		try:source8 = begal['data'][0]['emails'][6]['sources'][0]
		except KeyError:source8 = ('-')
		try:emails7 = begal['data'][0]['emails'][7]['value']
		except KeyError:emails7 = ('-')
		try:source9 = begal['data'][0]['emails'][7]['sources'][0]
		except KeyError:source9 = ('-')
		try:emails8 = begal['data'][0]['emails'][8]['value']
		except KeyError:emails8 = ('-')
		try:source10 = begal['data'][0]['emails'][8]['sources'][0]
		except KeyError:source10 = ('-')
		try:emails9 = begal['data'][0]['emails'][9]['value']
		except KeyError:emails9 = ('-')
		try:source11 = begal['data'][0]['emails'][9]['sources'][0]
		except KeyError:source11 = ('-')
		try:emails10 = begal['data'][0]['emails'][10]['value']
		except KeyError:emails10 = ('-')
		try:source12 = begal['data'][0]['emails'][10]['sources'][0]
		except KeyError:source12= ('-')
		try:phone0 = begal['data'][0]['phone_numbers'][0]['value']
		except KeyError:phone0 = ('-')
		try:value0 = begal['data'][0]['phone_numbers'][0]['sources'][0]
		except KeyError:value0 = ('-')
		try:phone1 = begal['data'][0]['phone_number'][1]['value']
		except KeyError:phone1 = ('-')
		try:value1 = begal['data'][0]['phone_numbers'][1]['sources'][0]
		except KeyError:value1 = ('-')
		try:phone2 = begal['data'][0]['phone_numbers'][2]['value']
		except KeyError:phone2 = ('-')
		try:value2 = begal['data'][0]['phone_numbers'][2]['sources'][0]
		except KeyError:value2 = ('-')
		try:phone3 = begal['data'][0]['phone_numbers'][3]['value']
		except KeyError:phone3 = ('-')
		try:value3 = begal['data'][0]['phone_numbers'][3]['sources'][0]
		except KeyError:value3 = ('-')
		try:phone4 = begal['data'][0]['phone_numbers'][4]['value']
		except KeyError:phone4 = ('-')
		try:value4 = begal['data'][0]['phone_numbers'][4]['sources'][0]
		except KeyError:value4 = ('-')
		try:phone5 = begal['data'][0]['phone_numbers'][5]['value']
		except KeyError:phone5 = ('-')
		try:value5 = begal['data'][0]['phone_numbers'][5]['sources'][0]
		except KeyError:value5 = ('-')
		try:phone6 = begal['data'][0]['phone_numbers'][6]['value']
		except KeyError:value5 = ('-')
		try:value6 = begal['data'][0]['phone_numbers'][6]['sources'][0]
		except KeyError:value6 = ('-')
		try:phone7 = begal['data'][0]['phone_numbers'][7]['value']
		except KeyError:phone7 = ('-')
		try:value7 = begal['data'][0]['phone_numbers'][7]['sources'][0]
		except KeyError:value7 = ('-')
		try:phone8 = begal['data'][0]['phone_numbers'][8]['value']
		except KeyError:phone8 = ('-')
		try:value8 = begal['data'][0]['phone_numbers'][8]['sources'][0]
		except KeyError:value8 = ('-')
		try:phone9 = begal['data'][0]['phone_numbers'][9]['value']
		except KeyError:phone9 = ('-')
		try:value9 = begal['data'][0]['phone_numbers'][9]['sources'][0]
		except KeyError:value9 = ('-')
		try:phone10 = begal['data'][0]['phone_numbers'][10]['value']
		except KeyError:phone10 = ('-')
		try:value10 = begal['data'][0]['phone_numbers'][10]['sources'][0]
		except KeyError:value10 = ('-')
		cetak(panel(f"\t\t\t                 {K2}MEDIA SOSIAL",width=100,title_align='center',title=f"{M2}▪︎{K2}▪︎{H2}▪︎{K2}{doma}{H2}▪︎{K2}▪︎{M2}▪︎",style=f"bold green"))
		print(f"\x1b[1;92m╔═\33[m[\x1b[1;92m+\33[m] FACEBOOK : \x1b[1;92m{facebook}")
		print(f"\x1b[1;92m╠═\33[m[\x1b[1;92m+\33[m] INSTAGRAM : \x1b[1;92m{instagram}")
		print(f"\x1b[1;92m╠═\33[m[\x1b[1;92m+\33[m] TIKTOK : \x1b[1;92m{tiktok}")
		print(f"\x1b[1;92m╠═\33[m[\x1b[1;92m+\33[m] SNAPCHAT : \x1b[1;92m{snapchat}")
		print(f"\x1b[1;92m╠═\33[m[\x1b[1;92m+\33[m] TWITTER : \x1b[1;92m{twitter}")
		print(f"\x1b[1;92m╠═\33[m[\x1b[1;92m+\33[m] LINKEDIN : \x1b[1;92m{linkedin}")
		print(f"\x1b[1;92m╠═\33[m[\x1b[1;92m+\33[m] GITHUB : \x1b[1;92m{github}")
		print(f"\x1b[1;92m╠═\33[m[\x1b[1;92m+\33[m] YOUTUBE : \x1b[1;92m{youtube}")
		print(f"\x1b[1;92m╚═\33[m[\x1b[1;92m+\33[m] PINTEREST : \x1b[1;92m{pinterest}")
		cetak(panel(f"\t\t\t                 {K2}CONTACT EMAILS",width=100,style=f"bold green"))
		print(f"\x1b[1;92m╔═\33[m[\x1b[1;92m+\33[m] EMAILS \x1b[1;92m0 \33[m: \x1b[1;92m{emails0}")
		print(f"\x1b[1;92m╚═\33[m[\x1b[1;92m+\33[m] SOURCE \x1b[1;92m0 \33[m: \x1b[1;92m{source0}")
		print(f"    \x1b[1;92m╠═\33[m[\x1b[1;92m+\33[m] SOURCE \x1b[1;92m1 \33[m: \x1b[1;92m{source1}")
		print(f"    \x1b[1;92m╠═\33[m[\x1b[1;92m+\33[m] SOURCE \x1b[1;92m2 \33[m: \x1b[1;92m{source2}")
		print(f"\x1b[1;92m╔═\33[m[\x1b[1;92m+\33[m] EMAILS \x1b[1;92m1 \33[m: \x1b[1;92m{emails1}")
		print(f"\x1b[1;92m╚═\33[m[\x1b[1;92m+\33[m] SOURCE \x1b[1;92m1 \33[m: \x1b[1;92m{source3}")
		print(f"\x1b[1;92m╔═\33[m[\x1b[1;92m+\33[m] EMAILS \x1b[1;92m2 \33[m: \x1b[1;92m{emails2}")
		print(f"\x1b[1;92m╚═\33[m[\x1b[1;92m+\33[m] SOURCE \x1b[1;92m2 \33[m: \x1b[1;92m{source4}")
		print(f"\x1b[1;92m╔═\33[m[\x1b[1;92m+\33[m] EMAILS \x1b[1;92m3 \33[m: \x1b[1;92m{emails3}")
		print(f"\x1b[1;92m╚═\33[m[\x1b[1;92m+\33[m] SOURCE \x1b[1;92m3 \33[m: \x1b[1;92m{source5}")
		print(f"\x1b[1;92m╔═\33[m[\x1b[1;92m+\33[m] EMAILS \x1b[1;92m3 \33[m: \x1b[1;92m{emails4}")
		print(f"\x1b[1;92m╚═\33[m[\x1b[1;92m+\33[m] SOURCE \x1b[1;92m3 \33[m: \x1b[1;92m{source6}")
		print(f"\x1b[1;92m╔═\33[m[\x1b[1;92m+\33[m] EMAILS \x1b[1;92m3 \33[m: \x1b[1;92m{emails5}")
		print(f"\x1b[1;92m╚═\33[m[\x1b[1;92m+\33[m] SOURCE \x1b[1;92m3 \33[m: \x1b[1;92m{source7}")
		print(f"\x1b[1;92m╔═\33[m[\x1b[1;92m+\33[m] EMAILS \x1b[1;92m3 \33[m: \x1b[1;92m{emails6}")
		print(f"\x1b[1;92m╚═\33[m[\x1b[1;92m+\33[m] SOURCE \x1b[1;92m3 \33[m: \x1b[1;92m{source8}")
		print(f"\x1b[1;92m╔═\33[m[\x1b[1;92m+\33[m] EMAILS \x1b[1;92m3 \33[m: \x1b[1;92m{emails7}")
		print(f"\x1b[1;92m╚═\33[m[\x1b[1;92m+\33[m] SOURCE \x1b[1;92m3 \33[m: \x1b[1;92m{source9}")
		print(f"\x1b[1;92m╔═\33[m[\x1b[1;92m+\33[m] EMAILS \x1b[1;92m3 \33[m: \x1b[1;92m{emails8}")
		print(f"\x1b[1;92m╚═\33[m[\x1b[1;92m+\33[m] SOURCE \x1b[1;92m3 \33[m: \x1b[1;92m{source10}")
		print(f"\x1b[1;92m╔═\33[m[\x1b[1;92m+\33[m] EMAILS \x1b[1;92m3 \33[m: \x1b[1;92m{emails9}")
		print(f"\x1b[1;92m╚═\33[m[\x1b[1;92m+\33[m] SOURCE \x1b[1;92m3 \33[m: \x1b[1;92m{source11}")
		print(f"\x1b[1;92m╔═\33[m[\x1b[1;92m+\33[m] EMAILS \x1b[1;92m3 \33[m: \x1b[1;92m{emails10}")
		print(f"\x1b[1;92m╚═\33[m[\x1b[1;92m+\33[m] SOURCE \x1b[1;92m3 \33[m: \x1b[1;92m{source12}")
		cetak(panel(f"\t\t\t             {K2}CONTACT PHONE NUMBERS",width=100,style=f"bold green"))
		print(f"\x1b[1;92m╔═\33[m[\x1b[1;92m+\33[m] PHONE NUMBERS \x1b[1;92m0 \33[m: \x1b[1;92m{phone0}")
		print(f"\x1b[1;92m╚═\33[m[\x1b[1;92m+\33[m] SOURCE \x1b[1;92m0 \33[m: \x1b[1;92m{value0}")
		print(f"\x1b[1;92m╔═\33[m[\x1b[1;92m+\33[m] PHONE NUMBERS \x1b[1;92m1 \33[m: \x1b[1;92m{phone1}")
		print(f"\x1b[1;92m╚═\33[m[\x1b[1;92m+\33[m] SOURCE \x1b[1;92m1 \33[m: \x1b[1;92m{value1}")
		print(f"\x1b[1;92m╔═\33[m[\x1b[1;92m+\33[m] PHONE NUMBERS \x1b[1;92m2 \33[m: \x1b[1;92m{phone2}")
		print(f"\x1b[1;92m╚═\33[m[\x1b[1;92m+\33[m] SOURCE \x1b[1;92m2 \33[m: \x1b[1;92m{value2}")
		print(f"\x1b[1;92m╔═\33[m[\x1b[1;92m+\33[m] PHONE NUMBERS \x1b[1;92m3 \33[m: \x1b[1;92m{phone3}")
		print(f"\x1b[1;92m╚═\33[m[\x1b[1;92m+\33[m] SOURCE \x1b[1;92m3 \33[m: \x1b[1;92m{value3}")
		print(f"\x1b[1;92m╔═\33[m[\x1b[1;92m+\33[m] PHONE NUMBERS \x1b[1;92m4 \33[m: \x1b[1;92m{phone4}")
		print(f"\x1b[1;92m╚═\33[m[\x1b[1;92m+\33[m] SOURCE \x1b[1;92m4 \33[m: \x1b[1;92m{value4}")
		print(f"\x1b[1;92m╔═\33[m[\x1b[1;92m+\33[m] PHONE NUMBERS \x1b[1;92m5 \33[m: \x1b[1;92m{phone5}")
		print(f"\x1b[1;92m╚═\33[m[\x1b[1;92m+\33[m] SOURCE \x1b[1;92m5 \33[m: \x1b[1;92m{value5}")
		print(f"\x1b[1;92m╔═\33[m[\x1b[1;92m+\33[m] PHONE NUMBERS \x1b[1;92m6 \33[m: \x1b[1;92m{phone6}")
		print(f"\x1b[1;92m╚═\33[m[\x1b[1;92m+\33[m] SOURCE \x1b[1;92m6 \33[m: \x1b[1;92m{value6}")
		print(f"\x1b[1;92m╔═\33[m[\x1b[1;92m+\33[m] PHONE NUMBERS \x1b[1;92m7 \33[m: \x1b[1;92m{phone7}")
		print(f"\x1b[1;92m╚═\33[m[\x1b[1;92m+\33[m] SOURCE \x1b[1;92m7 \33[m: \x1b[1;92m{value7}")
		print(f"\x1b[1;92m╔═\33[m[\x1b[1;92m+\33[m] PHONE NUMBERS \x1b[1;92m8 \33[m: \x1b[1;92m{phone8}")
		print(f"\x1b[1;92m╚═\33[m[\x1b[1;92m+\33[m] SOURCE \x1b[1;92m8 \33[m: \x1b[1;92m{value8}")
		print(f"\x1b[1;92m╔═\33[m[\x1b[1;92m+\33[m] PHONE NUMBERS \x1b[1;92m9 \33[m: \x1b[1;92m{phone9}")
		print(f"\x1b[1;92m╚═\33[m[\x1b[1;92m+\33[m] SOURCE \x1b[1;92m9 \33[m: \x1b[1;92m{value9}")
		print(f"\x1b[1;92m╔═\33[m[\x1b[1;92m+\33[m] PHONE NUMBERS \x1b[1;92m10 \33[m: \x1b[1;92m{phone10}")
		print(f"\x1b[1;92m╚═\33[m[\x1b[1;92m+\33[m] SOURCE \x1b[1;92m10 \33[m: \x1b[1;92m{value10}")
		cetak(panel(f"{K2}                                APAKAH ANDA INGIN KELUAR ? [bold white]({K2}Y{H2}/{M2}T[bold white])",width=100,style=f"bold green"))
		woy = input(f"\33[m[\x1b[1;92m?\33[m] PILIH.> \x1b[1;92m")
		if woy in ['y','Y']:
			menjadi_aungthor()
		elif woy in ['t','T']:
			os.system('xdg-open https://youtube.com/@TutorialTermux?si=_cE6fr-T2xCq_FCR')
			exit()
	except requests.exceptions.ConnectionError:
		print('\33[m[\x1b[1;91mX\33[m] INTERNET ANDA KURANG BAGUS NIH !')
		exit()
	except Exception as e:
		print(f"\33[m[\x1b[1;91mX\33[m] SYNTAX : \x1b[1;92m{str(e).title()}")
		exit()
		
if __name__=='__main__':
	menjadi_aungthor()