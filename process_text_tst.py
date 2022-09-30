from textblob.classifiers import NaiveBayesClassifier as NBC
from textblob import TextBlob
import spacy
from spacy.matcher import Matcher
from nltk import word_tokenize, pos_tag
from requests_html import HTML, HTMLSession
from bs4 import BeautifulSoup, SoupStrainer

training_corpus = [
                   ('Telegram: https://t.me/TetherPrint', 'Class_Telegram'),
                   ('📱TG : @ShibaPuppyToken', 'Class_Telegram'),
                   ('💎Join the Community!\nhttps://t.me/matrix_protocol', 'Class_Telegram'),
                   ('Official Telegram chat: https://t.me/Ocean_Token', 'Class_Telegram'),
                   ('Telegram: https://t.me/degemofficial', 'Class_Telegram'),
                   ('Telegram: https://t.me/urgamingtoken', 'Class_Telegram'),
                   ('☎️ Telegram: https://t.me/Squidanomics ', 'Class_Telegram'),
                   ("SOCIALS\nhttps://t.me/satoshibetstoken", 'Class_Telegram'),
                   ("✅ Telegram: https://t.me/nftmusicstream", 'Class_Telegram'),
                   (' See TG Post.', 'Class_Telegram')]
test_corpus = [
                ("Telegram: https://t.me/LiquidCollectibles", 'Class_Telegram'), 
                ("Discord: https://discord.gg/tR8hMsDhQh", 'Class_Discord'), 
                ('Twitter: https://twitter.com/LiqCollectibles', 'Class_Twitter'), 
                ("Telegram: https://t.me/NFTFundArtChat", 'Class_Telegram'), 
                (' https://t.me/pocmoncom ', 'Class_Telegram'), ('Twitter: https://twitter.com/NFTFundArt', 'Class_Twitter')]

model = NBC(training_corpus) 
phrase1 = "Check out my channel and talk to other users, and enjoy Telegram @cryptermain   this very thing"
phrase2 = '''🎮@UltiArena 500$ COMPETITION🎮
🏆 Five winners(100$/each)
🔥 See More Info on Twitter
(https://twitter.com/UltiArena/status/1449004937107709966)

(Compete here)
👉🏻 (https://giveaways.ultiarena.com/)
☘️ Feeling Lucky? Good luck!

What is UltiArena?
👾Ulti Arena is aiming to be the largest Gaming and NFT Market space of 2021. It will be a big community involving gamers, NFT game artists, developers and freelancers. A community where people connect with each other through discussion boards, showcase their work and earn to play!A true revolutionary ecosystem, made by gamers, for gamers!

Already listed exchanges
PancakeSwap V2 ✅
Cointiger✅
LBANK✅
HOTBIT✅
BITMART ✅

👾Are you excited for the upcoming Beta for the NFT Marketplace? For sure we do!
👾See our latest AMA with the devs to discuss about the launch of one of our most awaited products ❤️(NFT MARKETPLACE)
( https://www.twitch.tv/videos/1177331412 )

What are $ULTI use-cases?

* A possibility for Game Artists to showcase their work, provide them with the tools to kickstart their projects, enable sales through NFT Market space, find job offers from developers or producers and much more!

* A way for Developers to discover artists/designers, collaborate and form future partnerships, gain interest for games or projects!

* An option for Gamers to buy/sell NFT's, view portfolios of game assets/UI's/musics from their favourite games, join discussion boards, participate in tournaments and win prizes!

**EARNING ULTI TOKENS**

Users will have multiple ways to earn $ULTI

* Through a whole new concept "Proof-Of-Gaming" which allows users to earn while playing games

* Earn through community mining

* Staking

* Showcase assets, UI's, music, NFT's, prints and 2D/3D artworks

**AFFILIATE PROGRAM**

* Affiliate Program will focus on high-traffic crypto websites and marketplaces to take part in the sale of NFT’s on ULTI Arena

**SPECIAL TREATS FOR HOLDERS**

* 30% of all Ulti Arena's revenue goes to buy-back and burn

* By participating in the community discussion boards, events, competitions and tournaments you will earn ULTI tokens

* Commission discount on each purchase and sale on our platform

* Discounts on products and services when paying with ULTI tokens

**TOKENOMICS**

* Total supply is 250 Billion tokens (Now reduced to ***204Bil*** after burn events)

* Private sale and Pre-sale make up 18% of total supply which will be locked for the period of 2 months after the Public Sale date (***September 12, 2021***)

* Remaining supply will be released as public sale

* For each sale there will be %6 transaction fee

* 30% of platform revenues will go to buy-back & burn to ensure price stability and increase the value of $Ulti's

* For more detailed information and token supply allocation table refer to our whitepaper

* Ulti Arena Medium: [ulti-arena.medium.com](https://ulti-arena.medium.com/3d-industry-market-report-part-1-4908bf15d061)

**ROADMAP**

🏆*Q2 2021:* Testnet Launch, Smart Contracts, Wallet Integration, Token PreSale, Start of Development

🏆*Q3 2021:* IDO, Public Security Audit, Creation & Trade Features, Token Staking, Beta NFT Marketplace Lauch(invitational-only), Unity + Unreal Engine Plugins

🏆*Q4 2021:* Mainnet Launch, NFT Marketplace Release, Job Matching Marketplace, Discussion Board, Artist Storefront and Portfolio, Social Features, 2D/3D Collaboration Tool

🏆*Q1 2022:* Proof-Of-Gaming, Binance and Other Major Exchange Listings, Game Client + Analytics, eSports Tournaments, Community Moderation

🏆*Q2 2022:* Metaverse Integrations, Social Channels, Donations, Mobile Support, Collections

🏆*Q3 2022:* ULTI Metaverse Game Engine, Metaverse Onboarding of Game, Creators and Influencers, Growth of All ULTI Products

🏆*Q4 2022:* Coinbase Listing, ULTI Metaverse Engine v2.0, ULTI Metaverse Games made by Creators

THE SINGULARITY: Ulti Arena's goal is to become the centre point for all things gaming. Be part of revolution!

**OUR WEBSITE:** [https://ultiarena.com/](https://ultiarena.com/)

༄ [Team Ulti](https://ultiarena.com/team-ulti/) \- Find out our **Team Members** and **Advisors**

༄ [Whitepaper](https://ultiarena.com/wp-content/uploads/2021/09/Ulti-Arena-Whitepaper-2.0-1.pdf)

༄ [Pitchdeck](https://ultiarena.com/wp-content/uploads/2021/05/Ulti-Arena-Pitchdeck.pdf)
'''

'''
print(model.classify(phrase1))
print(model.classify(phrase2))
tokens = word_tokenize(phrase2)
print (pos_tag(tokens)) 

print(model.accuracy(test_corpus))

nlp = spacy.load('en_core_web_lg')
 
# load data
sentence = "Apple is looking at buying U.K. startup for $1 billion"
doc = nlp(phrase2)
 
# print entities
for ent in doc.ents:
    print(ent.text, ent.label_)
    #ent.start_char, ent.end_char, ent.ents.label_)
for ent in doc:
    print(ent.text, ent.pos_)
    #ent.start_char, ent.end_char, ent.ents.label_)


matcher = Matcher(nlp.vocab)
patternurl = [
    
[
    {"TEXT":{"REGEX": "t.me([a-zA-Z0-9\.\&\/\?\:@\-_=#])"}}
    ]

]
matcher.add("TELEGRAM_PATTERN_URL", patternurl)

print ("-------------")
doc = nlp(phrase2)

matches = matcher(doc)

for match_id, start, end in matches:
    matched_span = doc[start:end]
    print (matched_span.text)


for item in matches:
    print (doc[0:0].text)

page = 'https://www.reddit.com/r/CryptoMoonShots/comments/q9xj69/windoge95_is_about_trustworthiness_and_nostalgia/'

def _getTelegramLink(text):
    nlp = spacy.load('en_core_web_lg')

    matcher = Matcher(nlp.vocab)

     
    patternurl = [[{"TEXT":{"REGEX": "t\.me([a-zA-Z0-9\.\&\/\?\:@\-_=#])"}}]]
    matcher.add("TELEGRAMLINK_PATTERN", patternurl)
    doc = nlp(text)
    matches = matcher(doc)
    return matches


matx = _getTelegramLink(phrase2)

for match_id, start, end in matx:
        matched_span = doc[start:end]
        print (matched_span.text)

'''
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_lg
nlp = en_core_web_lg.load()
doc = nlp(phrase2)
print([(X.text, X.root.dep_, X.root.text) for X in doc.ents])
items = [x.text for x in doc.ents]

print(Counter(items).most_common(3))