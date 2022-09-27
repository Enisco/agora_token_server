
import sys
import os
import time
from random import randint
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agora_token_builder import RtcTokenBuilder
from flask import Flask, jsonify
app = Flask(__name__)

Role_Attendee = 0 # depreated, same as publisher
Role_Publisher = 1 # for live broadcaster
Role_Subscriber = 2 # default, for live audience

appId = "aaaaaaaaaaaaaaaaaaaaaaaaaaaa"
appCertificate = "aaaaaaaaaaaaaaaaaaaaaaaaaaaa"
expireTimeInSeconds = 86400
currentTimestamp = int(time.time())
privilegeExpiredTs = currentTimestamp + expireTimeInSeconds


@app.route("/")
def home():
    return "Welcome to my Flask App for Agora Token Client."

#---------------------------------------------------------------------

@app.route('/get-token/<myquery>')
def getNewAgoraToken(myquery):
    print(myquery)
    data = myquery.split ("~", 1)
    print(data[0])
    print(data[1])
    channelName = data[0]
    uid = data[1]
    
    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, 1, privilegeExpiredTs)
    print(token)
    return token

#---------------------------------------------------------------------

if __name__ == '__main__':
    app.run()
