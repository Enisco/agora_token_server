
import sys
import os
import time
from random import randint
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agora_token_builder import RtcTokenBuilder

Role_Attendee = 0 # depreated, same as publisher
Role_Publisher = 1 # for live broadcaster
Role_Subscriber = 2 # default, for live audience
Role_Admin = 101 # deprecated, same as publisher

appId = "ae5fd2a5833c4da5937bbd3a5d01b646"
appCertificate = "b6e2d56a64f7436d829db594fc0d51ce"
myquery = 'mychannel1~012'
data = myquery.split ("~", 1)
print(data[0])

channelName = data[0]
uid = data[1]
expireTimeInSeconds = 86400
currentTimestamp = int(time.time())
privilegeExpiredTs = currentTimestamp + expireTimeInSeconds
# role = RtcTokenBuilder.RolePublisher

token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, 0, 1, privilegeExpiredTs)

print('Token generted for channel ' + channelName + ' is: ' + token)