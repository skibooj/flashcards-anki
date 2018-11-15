import json
import urllib.parse
import requests

x = ['ass', 'bird', 'dog']


def CreateFlashcard(word):

    # setup api
    main_api = 'https://googledictionaryapi.eu-gb.mybluemix.net/?'
    define = word
    url = main_api + urllib.parse.urlencode({'define': define}) + '&lang=en'
    json_data = requests.get(url).json()
    json_status = json_data['meaning']

    # creating list
    partOfSpeech = ['', 'noun', 'adverb', 'adjective', 'verb']
    out = []
    n = 0

    for element in partOfSpeech:
        out.append([element])
        try:
            for i in range(10):
                try:
                    out[n].append("definition: " + json_status[element][i]['definition'])
                    out[n].append('example: ' + json_status[element][i]['example'])
                except:
                    pass
        except:
            pass
        n += 1

    return out
