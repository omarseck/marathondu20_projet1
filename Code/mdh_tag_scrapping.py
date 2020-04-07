# import libraries
from bs4 import BeautifulSoup
import urllib.request
import csv
import pandas as pd



# specify the url
url_list_enfant = ["http://www.mdph34.fr/annuaire-des-structures/annuaire-esms/liste-de-toutes-les-structures/camsp.html?no_cache=1&cHash=9c7328e9d844bb3f229b44e5f83cd4a3",
"http://www.mdph34.fr/annuaire-des-structures/annuaire-esms/liste-de-toutes-les-structures/cmpp.html?no_cache=1&cHash=eb5fa0e196015164a6f0ae6929647ea0",
"http://www.mdph34.fr/annuaire-des-structures/annuaire-esms/liste-de-toutes-les-structures/ime.html?no_cache=1&cHash=75d0a2e05a005941293227e69c1dd062",
"http://www.mdph34.fr/annuaire-des-structures/annuaire-esms/liste-de-toutes-les-structures/itep.html?no_cache=1&cHash=bda77cb9975c3222688e9dbd72c458c8",
"http://www.mdph34.fr/annuaire-des-structures/annuaire-esms/liste-de-toutes-les-structures/autres-etablissements-medico-sociaux.html?no_cache=1&cHash=e228df410c50023cf6ace7ce1a55a460",
"http://www.mdph34.fr/annuaire-des-structures/annuaire-esms/liste-de-toutes-les-structures/sessad.html?no_cache=1&cHash=515a17a81b41a3e8ea091194246c2e74",
"http://www.mdph34.fr/annuaire-des-structures/annuaire-esms/liste-de-toutes-les-structures/ulis-ecole.html?no_cache=1&cHash=c033aefd173c3b893d55233e5a3bc300",
"http://www.mdph34.fr/annuaire-des-structures/annuaire-esms/liste-de-toutes-les-structures/ulis-college.html?no_cache=1&cHash=917c3b8285a47ba1f9679414236f1cdf",
"http://www.mdph34.fr/annuaire-des-structures/annuaire-esms/liste-de-toutes-les-structures/ulis-lycee.html?no_cache=1&cHash=bcef58263bdedb6fdfffed3e30e248b5", ]

url_list = ["http://www.mdph34.fr/annuaire-des-structures/annuaire-esms/liste-de-toutes-les-structures/mas.html?no_cache=1&cHash=738fc36d7f0a887a9cd9a107052532f1",
"http://www.mdph34.fr/annuaire-des-structures/annuaire-esms/liste-de-toutes-les-structures/fam.html?no_cache=1&cHash=df567f28c547e67c8ef75315fffd1ed8",
"http://www.mdph34.fr/annuaire-des-structures/annuaire-esms/liste-de-toutes-les-structures/foyers-de-vie.html?no_cache=1&cHash=b3bea455a3f0ad14d2dc4c275c3b37df",
"http://www.mdph34.fr/annuaire-des-structures/annuaire-esms/liste-de-toutes-les-structures/foyers-dhebergement.html?no_cache=1&cHash=57ab7e71459ad328e37614534aa42005",
"http://www.mdph34.fr/annuaire-des-structures/annuaire-esms/liste-de-toutes-les-structures/esat.html?no_cache=1&cHash=4169afd82ed38a782a8975702f9139ca",
"http://www.mdph34.fr/annuaire-des-structures/annuaire-esms/liste-de-toutes-les-structures/sections-annexes-esat.html?no_cache=1&cHash=b4e9c0d94c08657d0bfbf5c2a5be57a8",
"http://www.mdph34.fr/annuaire-des-structures/annuaire-esms/liste-de-toutes-les-structures/entreprises-adaptees.html?no_cache=1&cHash=8ed8c04e18806d91821d57e019fecff5",
"http://www.mdph34.fr/annuaire-des-structures/annuaire-esms/liste-de-toutes-les-structures/autres-structures-professionnelles.html?no_cache=1&cHash=0f2b6bb31747a250eea5858361ceb525",
"http://www.mdph34.fr/annuaire-des-structures/annuaire-esms/liste-de-toutes-les-structures/autres-structures-professionnelles.html?no_cache=1&cHash=0f2b6bb31747a250eea5858361ceb525",
"http://www.mdph34.fr/annuaire-des-structures/annuaire-esms/liste-de-toutes-les-structures/autres-structures-professionnelles.html?no_cache=1&cHash=0f2b6bb31747a250eea5858361ceb525",
"http://www.mdph34.fr/annuaire-des-structures/annuaire-esms/liste-de-toutes-les-structures/savs.html?no_cache=1&cHash=38d030b85ffa543974db0bcfdc8a475d",
"http://www.mdph34.fr/annuaire-des-structures/annuaire-esms/liste-de-toutes-les-structures/samsah.html?no_cache=1&cHash=234edd22cd262be3b43421d00a100b0e",
"http://www.mdph34.fr/annuaire-des-structures/annuaire-esms/liste-de-toutes-les-structures/gem.html?no_cache=1&cHash=8a7c1c2bd84a9cee9b284aa640fb811d"]


i = 0
list_tag = []
list_site = []
for url in url_list:
    i += 1
    urlpage = url
    # query the website and return the html to the variable 'page'
    page = urllib.request.urlopen(urlpage)
    # parse the html using beautiful soup and store in variable 'soup'
    soup = BeautifulSoup(page, 'html.parser')
    # find results within table
    table = soup.find('table', attrs={'class': 'liste_structure'})
    #table = table.find('tbody')
    #table = table.find_all('td', attrs={'class': 'titre'})


    for name in table.find_all('td', attrs={'class': 'titre'}):
        #print(name)
        #nom_etab.append(name.find("a").text)
        for a in name.find_all('a', href=True):
            url = "http://www.mdph34.fr/" + a['href']
            lien = urllib.request.urlopen(url)
            soup_2 = BeautifulSoup(lien, 'html.parser')
            div = soup_2.find('div', attrs={'class':'details'})
            #print(div)
            try:
                #print("aaaaaaaaaa")
                for tag in div.find('fieldset').find_next_siblings():
                    print(url)
                    print(tag.find_all('li')[3].text)
                    list_tag.append(tag.find_all('li')[3].text)
                    list_site.append(url)
                #print("bbbbbbbbbb")
            except :
                #list_tag.append("None")
                #list_site.append(url)
                pass
            #aaaa print(div.find('ul').findChildren()[1])
            #for tag in div.find('ul'):

                #print(tag.find('li').findChildren()[1])

df = pd.DataFrame({
'Site' : list_site,
'Tag' : list_tag,
})

print(df)

fichier = df.to_csv("result_tag_mdh.csv")


'''
    current_list_adr = [adr.renderContents().strip() for adr in table.find_all("td", class_="adresse")]
    current_list_tel = [adr.renderContents().strip() for adr in table.find_all("td", class_="tel")]
    list_adr.extend(current_list_adr)
    list_tel.extend(current_list_tel)
#good print(list_adr)

df = pd.DataFrame({
'Nom' : nom_etab,
'Adresse' : list_adr,
'Telephone' : list_tel
})

fichier = df.to_csv("result2.csv")

print(df.tail())
'''
