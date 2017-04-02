# -*- coding: utf-8 -*-
import requests
import random

# question, answer

houseList = [
    7, 17, 34, 66, 169, 195,
    202, 215, 229, 244, 271, 285,
    328, 362, 378, 379, 395, 398
]

charList = [
    12, 16, 20, 27, 28, 54, 60, 79, 125, 142, 148, 150, 168, 181, 190, 208,
    216, 217, 223, 232, 238, 313, 325, 326, 339, 341, 346, 364, 397, 400, 421,
    439, 506, 521, 529, 533, 547, 565, 571, 572, 583, 595, 605, 613, 640, 649,
    667, 688, 691, 692, 735, 743, 752, 775, 784, 806, 823, 827, 829, 832, 849,
    850, 862, 884, 887, 891, 894, 901, 903, 912, 933, 937, 955, 957, 975, 1008,
    1022, 1029, 1033, 1043, 1052, 1068, 1079, 1084, 1093, 1104, 1106, 1131,
    1132, 1165, 1166, 1222, 1242, 1293, 1298, 1303, 1306, 1319, 1340, 1346,
    1418, 1427, 1442, 1445, 1471, 1501, 1508, 1520, 1532, 1559, 1560, 1577,
    1594, 1626, 1630, 1649, 1650, 1666, 1703, 1708, 1709, 1749, 1766, 1768,
    1770, 1781, 1787, 1814, 1821, 1825, 1826, 1839, 1848, 1861, 1880, 1903,
    1925, 1935, 1938, 1939, 1963, 1972, 1979, 1994, 2002, 2024, 2040, 2041,
    2069, 2118, 2122, 2126
]


def generateHouseLord():
    houseid = random.choice(houseList)
    house = requests.get(
        'http://www.anapioficeandfire.com/api/houses/' + str(houseid)
    ).json()
    if house['currentLord'] == "":
        return generateHouseLord()
    else:
        lord = requests.get(house['currentLord']).json()
        return (
            "Who is the current lord of " + house['name'] + "?",
            lord['name'],
        )


def generateHouseWords():
    houseid = random.choice(houseList)
    house = requests.get(
        'http://www.anapioficeandfire.com/api/houses/' + str(houseid)
    ).json()
    if house['words'] == "":
        return generateHouseWords()
    else:
        return (
            "Which house has, as its words, " + house['words'] + "?",
            house['name'],
        )


def generatePlayedBy():
    charid = random.choice(charList)
    char = requests.get(
        'http://www.anapioficeandfire.com/api/characters/' + str(charid)
    ).json()
    if len(char['playedBy']) == 0:
        return generatePlayedBy()
    else:
        return (
            "What character did " + char['playedBy'][0] + " play in \
            the Game of Thrones TV series?",
            char['name'],
        )


def generateCurated():
    curated_list = [
        (
            "What is name of Jon Snow's Direwolf?",
            "Ghost",
        ),
        (
            "What is name of Rickon Stark's Direwolf?",
            "Shaggydog",
        ),
        (
            "What is name of Arya Stark's Direwolf?",
            "Nymeria",
        ),
        (
            "What is name of Sansa Stark's Direwolf?",
            "Lady",
        ),
        (
            "What city is the Iron Bank located in?",
            "Braavos",
        ),
        (
            "Which character's sigil is of a stag inside of a fiery heart?",
            "stannis",
        ),
        (
            "What is the name of Samwell Tarly's brother?",
            "dickon tarly",
        ),
        (
            "Which house has the banner of a falcon and a moon?",
            "house arryn",
        ),
        (
            "What is name of Jon Snow's sword?",
            "Longclaw",
        ),
        (
            "What is name of Ned Stark's sword?",
            "Ice",
        ),
        (
            "What does khaleesi mean in Dothraki?",
            "queen",
        ),
        (
            "What is the largest castle in Westeros?",
            "harrenhal",
        ),
        (
            "Which house has the banner of a giant in chains?",
            'house umber',
        ),
    ]
    return random.choice(curated_list)


def generateQuestions(tree):
    questionlist = [
        generateHouseLord,
        generateHouseWords,
        generatePlayedBy,
        generateCurated,
    ]
    node = 29
    new_q = random.choice(questionlist)()
    tree[node]['question'] = new_q[0]
    tree[node]['answer'] = new_q[1]
    node += 1
    for i in range(5):
        new_q = random.choice(questionlist)()
        repeatQ = True
        while repeatQ:
            repeatQ = False
            for i in range(29, 35):
                if new_q[0] == tree[i]['question']:
                    repeatQ = True
                    new_q = random.choice(questionlist)()
        tree[node]['question'] = new_q[0]
        tree[node]['answer'] = new_q[1]
        node += 1
