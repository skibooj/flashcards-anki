import requests


def CreateFlashcard(word):
    # setup request
    url = 'https://googledictionaryapi.eu-gb.mybluemix.net/?define=' + word + '&lang=en'
    json_data = requests.get(url).json()

    flashcard = []  # create flashchard
    try:
        flashcard.append(json_data[0]['word'])  # add word
    except:
        pass
    try:
        flashcard.append(json_data[0]['phonetic'])  # add phonetic
    except:
        flashcard.append("#N/A")
    try:
        flashcard.append(list(json_data[0]['meaning'].keys())[0])  # add part of speech
    except:
        flashcard.append("#N/A")
    try:
        flashcard.append(list(json_data[0]['meaning'].values())[0][0]['definition'])  # add definition of word
    except:
        flashcard.append("#N/A")
    try:
        flashcard.append(list(json_data[0]['meaning'].values())[0][0]['example'])  # add example
    except:
        flashcard.append("#N/A")

    return flashcard
