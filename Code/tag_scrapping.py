# import libraries
from bs4 import BeautifulSoup
import urllib.request
import csv
import pandas as pd


'''
url_list = ["https://www.halte-pouce.fr/ressources/lecole-et-sessad-parents-these-a-jacou-34-specialisee-dans-les-ted",
"https://www.halte-pouce.fr/ressources/association-avenir-des-possibles-a-lunel-pour-les-autistes-par-les-autistes",
"https://www.halte-pouce.fr/ressources/Les-Ateliers-de-Bentenac",
"https://www.halte-pouce.fr/ressources/lecole-amethyste-une-ecole-privee-atypique-a-palavas-les-flots",
"https://www.halte-pouce.fr/actualites/message-du-cesu-appel-a-la-solidarite-des-particuliers-employeurs",
"https://www.halte-pouce.fr/ressources/L-association-Col-Oc-Autisme",
"https://www.halte-pouce.fr/ressources/lecole-et-sessad-parents-these-a-jacou-34-specialisee-dans-les-ted",
"https://www.halte-pouce.fr/ressources/association-avenir-des-possibles-a-lunel-pour-les-autistes-par-les-autistes",
"https://www.halte-pouce.fr/ressources/Les-Ateliers-de-Bentenac",
"https://www.halte-pouce.fr/ressources/lecole-amethyste-une-ecole-privee-atypique-a-palavas-les-flots",
"https://www.halte-pouce.fr/actualites/message-du-cesu-appel-a-la-solidarite-des-particuliers-employeurs",
"https://www.halte-pouce.fr/ressources/L-association-Col-Oc-Autisme"]
'''

url_list = ["https://www.halte-pouce.fr/ressources/lassociation-manque-pas-dair-accueille-la-difference",
"https://www.halte-pouce.fr/ressources/centre-de-pleine-nature-station-cevennes",
"https://www.halte-pouce.fr/ressources/sensas-un-lieu-unique-pour-mettre-vos-5-sens-a-lepreuve-en-famille-et-soutenir-halte-pouce",
"https://www.halte-pouce.fr/ressources/un-cafe-asperger-un-mardi-sur-deux-a-montpellier",
"https://www.halte-pouce.fr/ressources/Piscine-et-handicap-a-Montpellier",
"https://www.halte-pouce.fr/ressources/Association-Mohicans",
"https://www.halte-pouce.fr/ressources/au-pays-des-carrioles-un-parc-de-loisirs-insolite-et-accessible-a-la-boissiere",
"https://www.halte-pouce.fr/ressources/lassociation-un-sourire-en-chantant",
"https://www.halte-pouce.fr/ressources/association-saudade-des-ateliers-ouverts-a-toutes-les-differences",
"https://www.halte-pouce.fr/ressources/ateliers-adaptes-tous-handicaps-a-teyran",
"https://www.halte-pouce.fr/ressources/montpellier-club-handisport-mch-34-tous-faits-pour-le-sport",
"https://www.halte-pouce.fr/ressources/balades-adaptees-a-dos-danes-association-handiane",
"https://www.halte-pouce.fr/ressources/parentalite-34",
"https://www.halte-pouce.fr/ressources/association-yarrivarem-34",
"https://www.halte-pouce.fr/ressources/association-mozaik-danse",
"https://www.halte-pouce.fr/ressources/association-apedys-herault-association-regionale-de-parents-denfants-et-dadultes-dyslexiques",
"https://www.halte-pouce.fr/ressources/lassociation-pic-autisme-trisomie-dans-lherault",
"https://www.halte-pouce.fr/ressources/association-caravane-34",
"https://www.halte-pouce.fr/ressources/L-association-OZ-a-Sete",
"https://www.halte-pouce.fr/ressources/association-beau-nez-dAne",
"https://www.halte-pouce.fr/ressources/Equitherapie-a-gignac",
"https://www.halte-pouce.fr/ressources/des-cours-adaptes-de-cirque-avec-zepetra-a-castelnau-le-lez",
"https://www.halte-pouce.fr/ressources/handi-musique-sur-montpellier-avec-musika",
"https://www.halte-pouce.fr/ressources/association-musique-et-handicaps-mediterranee-a-montpellier",
"https://www.halte-pouce.fr/ressources/equitherapie-mediation-animale-a-gignac-34",
"https://www.halte-pouce.fr/ressources/association-dyspraxique-mais-fantastique-34-dmf34",
"https://www.halte-pouce.fr/ressources/POIL-DE-PAROLE-Mediation-animale",
"https://www.halte-pouce.fr/ressources/Association-Cap-A-Cites-a",
"https://www.halte-pouce.fr/ressources/Handicap-evasion-La-randonnee-pour",
"https://www.halte-pouce.fr/ressources/Eveil-et-partage-gites-de-vacances-pour-sejours-adaptes",
"https://www.halte-pouce.fr/ressources/vacances-adaptees-avec-lassociation-je-fais-ce-que-je-veux-jfjv",
"https://www.halte-pouce.fr/ressources/association-regains-sejours-we-pour-adulte-handicapes-mentaux",
"https://www.halte-pouce.fr/ressources/acces-aux-soins-des-personnes-en-situation-de-handicap-handiconsult34",
"https://www.halte-pouce.fr/ressources/Equipe-relais-handicaps-rares",
"https://www.halte-pouce.fr/ressources/RESEAU-MALADIES-RARES-MEDITERRANEE",
"https://www.halte-pouce.fr/ressources/sexualite-handicap-association-aparsa",
"https://www.halte-pouce.fr/ressources/letape-aides-techniques-et-perte-dautonomie",
"https://www.halte-pouce.fr/ressources/une-maison-daccueil-des-familles-de-malade-la-pasquiere",
"https://www.halte-pouce.fr/ressources/le-clos-de-la-fontaine-aide-aux-aidants",
"https://www.halte-pouce.fr/ressources/psychologue-clinicienne-et-lsf-genevieve-sancho",
"https://www.halte-pouce.fr/ressources/profitez-davantage-des-activites-en-milieu-ordinaire",
"https://www.halte-pouce.fr/ressources/les-antennes-de-la-solidarite-pres-de-chez-vous"]
i = 0
list_tag = []
list_site = []
for url in url_list:
    urlpage = url
    print("----------------deb----------------")
    print(url)
    # query the website and return the html to the variable 'page'
    page = urllib.request.urlopen(urlpage)
    # parse the html using beautiful soup and store in variable 'soup'
    soup = BeautifulSoup(page, 'html.parser')
    # find results within table
    #table = soup.find('div', attrs={'class': 'col-md-10'})
    #print(table.find("li").contents[0])
    print(soup.find('p', attrs={'class': 'article-date'}).text)
    list_site.append(url)
    list_tag.append(soup.find('p', attrs={'class': 'article-date'}).text[30:])


df = pd.DataFrame({
'Site' : list_site,
'Tag' : list_tag,
})

print(df)

fichier = df.to_csv("result_tag_2.csv")

    #for elmt in soup.find('div', attrs={'class': 'col-md-10'}):
    #    print(elmt.find('p'))



        #print(table.find_next_sibling("li"))


    #table = table.find('tbody')
    #table = table.find_
