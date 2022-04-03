import requests


tinder_api = 'https://api.gotinder.com'

fetchMatchesEndpoint = tinder_api + \
                       '/v2/matches?locale=en&count=60&message=0&is_tinder_u=false'
messageMatchEndpoint = tinder_api + '/user/matches/'

fetchParams = {'count': 100, 'is_tinder_u': 'false', 'message': 1}

headers = {
    #***Your tinder auth-token***
    'X-Auth-Token':'',
    }

matchesApiResponse = requests.get(
    url = fetchMatchesEndpoint, params = fetchParams, headers = headers)


def getPerson():
    data = requests.get(fetchMatchesEndpoint, headers=headers).json()
    data1 = data['data']['matches']
    if data1 == []:
        return 0
    else:
        person = data1[0]
        ID = person['_id']
        name = person['person']['name']
        return[ID, name]


while True:   
    person = getPerson()
    if person == 0:
        print('Completed')
        break

    else:
        print(person)
        print('Sending message to ' + person[1] + ' ................')

        body={}
        body['matchId'] = person[0]
        body['message'] = ';)'
        body['tempMessageId'] = '0.07054938870864036' # Any random number
        body['userId'] = '' # Your tinder user-id

        url = messageMatchEndpoint + person[0] + '?locale=en-GB'
        messageApiResponse = requests.post(url = url, json = body, headers = headers)
        print('Message successfully sent ................')
