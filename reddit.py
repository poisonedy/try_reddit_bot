#!/usr/bin/python3
from re import sub
import praw
from datetime import datetime
import time
import threading
import logging
from process_text import *



class redditSubredditBot(submissionTextProcess):

    def __init__(self, subreddit, client_id, client_secret, user_agent):
        super().__init__()
        
        self.client_id = client_id
        self.client_secret = client_secret
        self.user_agent = user_agent
        self.reddit = praw.Reddit(client_id = self.client_id, client_secret = self.client_secret, user_agent = self.user_agent)
        self.subredditName = subreddit
        self.subreddit = self.reddit.subreddit(self.subredditName)
        self.lastSnapshot = []
        self.bannedSubmissions = []
        self.lastSubmission = ''
        format = "%(asctime)s " + self.subredditName + ": %(message)s"
        logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%m/%d/%Y %H:%M:%S")
        self.bannedFinder = threading.Thread(target=self._removeBannedSubmissions)
        self.bannedFinder.start()
    

    def _getLastSubmissionFromLastSnapshot(self, position=0):
        try:

            return self.lastSnapshot[position]['submissionId']

        except:

            return ""

    def _createDefaultSubmissionDictionary(self, submission):
        html = markdown(submission.selftext)
        submselftext = ''.join(BeautifulSoup(html, features="lxml").findAll(text=True))

        submissionDictionary = {'submissionId':submission.id, 'submission': self.subredditName, 'submissionUrl' : submission.url, 'submissionTime' : datetime.now(), 'submissionText' : submselftext, 'scannedSubmission' : False, 'discardedSubmission' : False, 'scannedData' : {} }

        return submissionDictionary

    def getSnapshot(self):

        
        
            while True:

                snapShot = []

                for submission in self.subreddit.new(limit=20):

                    snapShot.append(submission)

                lastSubmission = self._getLastSubmissionFromLastSnapshot()
                

                if lastSubmission != "":

                    try:

                        positionLastSubmission = snapShot.index(lastSubmission)
                        #logging.info ("last submission is: " + lastSubmission)
                        
                        for submission in reversed(snapShot[0:positionLastSubmission]):
                        
                            self.lastSnapshot.insert(0,self._createDefaultSubmissionDictionary(submission))
                    
                        break

                    except:

                        logging.info ("Self autoremove submission: " + lastSubmission + " banned.")
                        self.bannedSubmissions.append((lastSubmission))
                        self._removeSubmissionById(lastSubmission)
               


                else:
                    for submission in snapShot:
                        self.lastSnapshot.append(self._createDefaultSubmissionDictionary(submission))

    def _removeSubmissionById(self, id):
        for item in self.lastSnapshot:
            if item['submissionId'] == id:
                self.lastSnapshot.remove(item)
                break


    def returnSubredditList (self):

        subredditList = []

        for item in self.lastSnapshot:
            subredditList.append(item['submissionId'])
        return subredditList

    def _getSubmissionText(self, submissionId):
        submission = self.reddit.submission(id=submissionId).selftext
        return submission

    def _isSubmissionRemoved(self, submissionId):
        if self._getSubmissionText(submissionId) == '[removed]':
            return True
        else:
            return False

    def _getSubmission(self, submissionId):

        for submission in self.lastSnapshot:
            if submission['submissionId'] == submissionId:
                return submission
    
    def _removeBannedSubmissions(self):

        format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
        
    def _scanInfo(self, submissionId):

        submissionToScan = self._getSubmission(submissionId)

    


    def _parseSubmissionText(self, submissionText):

        while True:

            if self.lastSnapshot:

                logging.debug ('Checking for banned submissions.')

            for submission in self.lastSnapshot:
                logging.debug("checking " + submission['submissionId'])

                if self._isSubmissionRemoved(submission['submissionId']):
                    logging.info ("removing banned submission " + submission['submissionId'])
                    self.lastSnapshot.remove(submission)

subreddit = redditSubredditBot("CryptoMoonShots","0OqfMjYVmx3OJNnVk1JJtQ", "1zdf7UfjCIXfp_N65ZadFCaqSXRRaA", "my user agent")

#subreddit.printSubreddits()
subreddit.getSnapshot()
logging.info (subreddit.returnSubredditList())
for item in subreddit.lastSnapshot:
    print(subreddit._getTelegramLink(item))

    



    #subreddit.lastSnapshot.append({'submissionId':'q9k7my','submissionTime' : datetime.now(), 'submissionText' : 'text', 'scannedSubmission' : False })
    #subreddit._removeBannedSubmissions()
#print(subreddit._getSubmissionText('qa2gs8'))
    #print(subreddit._isSubmissionRemoved('q9k7my'))


