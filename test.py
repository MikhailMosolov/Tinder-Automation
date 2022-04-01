import requests

fetchMatchesEndpoint = "https://api.gotinder.com/v2/matches?locale=en&count=60&message=0&is_tinder_u=false"
messageMatchEndpoint = "https://api.gotinder.com/user/matches/"

fetchParams = {'count': 100, 'is_tinder_u': 'false', 'message': 1}
headers = { 'Accept':'application/json',
            'Content-Type': 'application/json',
            'Origin': 'https://tinder.com',
            'app-version':'1020321',
            'platform':'web',
            'Referer':'https://tinder.com/',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'X-Auth-Token':'....................................', #***Your tinder auth-token***
            'x-supported-image-formats':'webp,jpeg'
        }

matchesApiResponse = requests.get(url = fetchMatchesEndpoint, params = fetchParams, headers = headers)
data = matchesApiResponse.json()
data=data['data']['matches'][:]


names = []
ids = []

for i in data:
    id = i['id']
    name = i['person']['name']
    
    ids.append(id)
    names.append(name)

j=0
for i in range(0, len(ids)):

    print('Sending message to ' + names[j] + ' ................')
    body={}
    body['matchId'] = ids[i]
    body['message'] = ';)'
    body['tempMessageId'] = '0.07054938870864036' # Any random number
    body['userId'] = '........................' # Your tinder user-id

    url = messageMatchEndpoint + ids[i] + '?locale=en-GB'
    messageApiResponse = requests.post(url = url, json = body, headers = headers)
    print('Message successfully sent ................')
    j+=1;

print('Completed')
