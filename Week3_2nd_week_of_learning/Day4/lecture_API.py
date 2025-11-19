
import requests
import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))


# response = requests.get('https://api.chucknorris.io/jokes/random')

# print(response)

# data = response.json()
# print(data)
# print(data['value'])
# print(data.get('value')) # helps to avoid mistakes

# with open(dir_path + '\jokes.json', 'w') as f:
#     json.dump(data,f, indent = 2, ensure_ascii=False)
#     print('file was created')

response2 = requests.get('https://binaryjazz.us/wp-json/genrenator/v1/genre/5')

print(response2)
data = response2.json()
print(data)