import requests
from datetime import datetime, date

tinder_api = 'https://api.gotinder.com'
token = '' # Your tinder auth-token

def getID():

    data = requests.get(tinder_api + '/v2/recs/core', \
                        headers={'X-Auth-Token': token}).json()
    data1 = data['data']['results']

    ID = data1[0]['user']['_id']

    name = data1[0]['user']['name']
    
    return [ID, name]
    
#print(getID())


while True:
    person = getID()
    data2 = requests.get(tinder_api + f'/like/{person[0]}', \
                    headers={'X-Auth-Token': token}).json()
    
    if (data2['match']) == True:
        print('There is a match with ' + person[1])
    
    if data2['likes_remaining'] == 0:
        time = data2['rate_limited_until']
        time = str(time)[:-3]
        time = int(time)
        time = datetime.fromtimestamp(time)
        print('Try again at ' + str(time))
        break
