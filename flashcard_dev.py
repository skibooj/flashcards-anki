import json
import urllib.parse
import requests


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

            out[n].append("definition: " + json_status[element][0]['definition'])
            out[n].append('example: ' + json_status[element][0]['example'])

        except:
            pass
        n += 1

    return out
