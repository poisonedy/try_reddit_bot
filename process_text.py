import spacy
from spacy.matcher import Matcher
from requests_html import HTML, HTMLSession
from bs4 import BeautifulSoup
from markdown import markdown



class submissionTextProcess:

    def __init__(self):
        self.nlp = spacy.load('en_core_web_lg')
        self.matcher = Matcher(self.nlp.vocab)
        

    def _getTelegramLink(self, item):
        results = []
        patternurl = [
            [
                {"TEXT":{"REGEX": "t\.me\/([a-zA-Z0-9\.\&\/\?\:@\-_=#])"}}
                ],
            [
                {"TEXT":{"REGEX": "(?i)(tg).?"}}, {"TEXT": {"REGEX":"@.*"}}
            ],
                ]
        self.matcher.add("TELEGRAMLINK_PATTERN", patternurl)
       
        doc = self.nlp(item['submissionText'])
        matches = self.matcher(doc)
        for match_id, start, end in matches:
            
            matched_span = doc[start:end]
            
            if self.subredditName not in matched_span.text:
            
                results.append(matched_span.text)
            
        if results == []:
            session = HTMLSession()
            trueString = ""
            page=session.get(item['submissionUrl'])
            mylist = list(page.html.links)
        
            for item in mylist:
        
                trueString += item + "\n"
        
            doc = self.nlp(trueString)
            matches = self.matcher(doc)
        
            for match_id, start, end in matches:
        
                matched_span = doc[start:end]
        
                if self.subredditName not in matched_span.text:
        
                    results.append(matched_span.text)
    
        if len(results) > 1:
            results = list(dict.fromkeys(results))



        return results