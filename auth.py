import requests

username = "apiuser"
password = "cmQyDFt++hJ/Q7h9cEVkS7QmL+688vSwOsNg3KA9S1w="

BASE_URI = "https://test-web.mynet.local"
credentials = (username, password) # username and password as a tuple

def test_basic_auth():
    '''testing basic auth using '''
    response = requests.get(BASE_URI, auth=credentials)
    status = response.status_code
    print(f"\nStatus Code is {status}")
    if status == 200:
        print("Authentication successful")
    else:
        print("Authentication failed")