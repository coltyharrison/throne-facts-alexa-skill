# -*- coding: utf-8 -*-
import requests
import random
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

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


def sigilClean(sigil_str):
    new_str = ''
    for i in range(len(sigil_str)):
        if sigil_str[i] == '(':
            break
        else:
            new_str += sigil_str[i]
    return new_str


def aka():
    charid = random.randint(1, 2138)
    char = requests.get(
        'http://www.anapioficeandfire.com/api/characters/' + str(charid)
    ).json()
    if char['name'] == "":
        return aka()
    elif len(char['aliases']) == 0:
        return aka()
    else:
        alias = random.sample(char['aliases'], 1)
        fact = "The character " + char['name'] + ", is also\
         known as " + alias[0]
        return fact


def playedBy():
    charid = random.choice(charList)
    char = requests.get(
        'http://www.anapioficeandfire.com/api/characters/' + str(charid)
    ).json()
    if len(char['playedBy']) == 0:
        return playedBy()
    else:
        return "In the show, the character \
        " + str(char['name']) + ", is played by \
        " + str(char['playedBy'][0])


def houseSigil():
    houseid = random.randint(1, 444)
    house = requests.get(
        'http://www.anapioficeandfire.com/api/houses/' + str(houseid)
    ).json()
    if house['coatOfArms'] == "":
        return houseSigil()
    else:
        newsigil = sigilClean(house['coatOfArms'])
        return "The sigil of " + house['name'] + ", is " + newsigil


def houseWords():
    houseid = random.randint(1, 444)
    house = requests.get(
        'http://www.anapioficeandfire.com/api/houses/' + str(houseid)
    ).json()
    if house['words'] == "":
        return houseWords()
    else:
        return "The words of " + house['name'] + ", are " + house['words']


def curatedFact():
    factlist = [
        "A Game of Thrones was published on August 1st, 1996",
        "A Clash of Kings was published on November 16th, 1998",
        "A Storm of Swords was published on August 8th, 2000",
        "A Feast for Crows was published on October 17th, 2005",
        "A Dance With Dragons was published on July 12th, 2011",
        "Bran Stark's direwolf is named Summer",
        "Rickon Stark's direwolf is named Shaggydog",
        "Robb Stark's direwolf is named Greywind",
        "Jon Snow's direwolf is named Ghost",
        "Sansa Stark's direwolf is named Lady",
        "Arya Stark's direwolf is named Nymeria",
        "The seat of the crannogmen is Greywater Watch",
        "Ellaria Sand, the paramour of Oberyn Martell, is the natural daughter\
        of Lord Harmen Uller",
        "House Templeton may be distantly related to House\
        Stark through Jocelyn Stark, a sister of Eddard Stark's\
        grandfather, Edwyle",
        "The first Clegane was knighted because he saved Lord Tytos\
        Lannister from a lioness and lost a leg and three dogs in the effort",
        "Robert Baratheon's warhammer was made by Donal Noye, the armorer in\
        the Night's Watch",
        "The Brave Companions are a band of sellswords comprised of criminals\
        and outcasts from many nations",
        "The religion of the Drowned God dates from before the Andal invasion",
        "The deserter of the Night's Watch that Eddard Stark executes in the\
        beginning of A Game of Thrones is Gared, one of the men who was with\
        Ser Waymar Royce in the prologue",
        "Anguy, Thoros, and Sandor Clegane—the respective winners of the\
        archery, melee, and jousting competitions within the Hand's\
        tourney—are all present when Arya Stark visits the hollow hill",
        "When Sansa Stark was betrothed to Joffrey Baratheon, Petyr\
        Baelish proposed betrothing Robb Stark to Myrcella Baratheon when she\
        came of age",
        "Eddard Stark's grandfather was named Edwyle Stark",
        "The Lannisters once owned a Valyrian sword called Brightroar",
        "Quhuru Mo, the captain of the Cinnamon Wind which transports Samwell\
        Tarly and Maester Aemon from Braavos to Oldtown, is the same person\
        who told Daenerys Targaryen the news of Robert Baratheon's death",
        "The Sand Snakes are the cousins of Rhaegar Targaryen's son, Aegon,\
        a daughter, Rhaenys",
        "The heir of a Dothraki khal is named the khalakka",
        "Tywin Lannister's wife, Lady Joanna, was also his cousin. Tywin's\
        father Tytos was the older brother of Joanna's father Jason ",
        "Princess Rhaenys Targaryen named her little black kitten Balerion",
        "The lords of House Arryn only live in the Eyrie during the summer, but\
        move down to the Gates of the Moon before winter",
        "Since Aegon's Conquest three hundred years ago Harrenhal has been the\
        seat of nine different noble houses",
        "House Tarly's seat is called Horn Hill",
        "Daemon Blackfyre, a Great Bastard, was Targaryen on both sides. His\
        mother was Princess Daena Targaryen, the wife of King Baelor Targaryen\
        the First, and his father was King Aegon Targaryen the Fourth",
        "The Port of Ibben, an icy port in the Shivering Sea, is lit by beacons\
        burning whale oil",
        "Brienne of Tarth found a shield in the armory of Evenfall\
        Hall displaying the same arms as that of Ser Duncan the Tall",
        "Bronze Yohn Royce, Lord of Runestone, wears bronze armor, reputedly\
        thousands of years old and worked with runes that are supposed to ward\
        him from harm",
        "The former ruling Princess of Dorne planned to wed her children,\
        Princess Elia and Prince Oberyn Martell, to one or both of Lord Tywin\
        Lannister's twins, Cersei and Jaime",
        "Brienne of Tarth had three siblings, none of whom survived childhood.\
        Her brother Galladon drowned, and her sisters Arianne and Alysanne\
        died as infants",
        "Mance Rayder used to be a ranger of the Night's Watch",
        "Petyr Baelish fought for the hand of Catelyn Tully when he was\
        scarcely fifteen, challenging her betrothed, Brandon Stark, who was\
        twenty",
        "Valar morghulis is a well-known phrase in High Valyrian, and means\
        All men must die. A common reply is Valar dohaeris, meaning All men\
        must serve",
        "Renly Baratheon and Loras Tyrell were lovers",
        "The Dothraki emerged from the Dothraki sea, about four hundred years\
        ago, following the Doom of Valyria",
        "Three thousand years ago the free folk, led by Gendel and Gorne,\
        managed to evade the Night's Watch and infiltrate the north in great\
        numbers using a network of tunnels that extended under the Wall",
        "The dwarf siblings Penny and Oppo make their living as entertainers\
        who ride atop a pig (Pretty Pig) and a dog (Crunch) while mock\
        fighting each other as Groat and Penny after the two smallest coins",
        "Wyman Manderly has the titles Lord of White Harbor, Warden of the\
        White Knife, Shield of the Faith, Defender of the Dispossessed, Lord\
        Marshal of the Mander, and Knight of the Order of the Green Hand",
        "Construction of the Red Keep was finished by Maegor the Cruel, who\
        rounded up everyone involved in its construction and had them killed,\
        to preserve its secrets",
        "The Iron Throne, made from the swords of those defeated in Aegon's\
        Conquest, was melted by Aegon Targaryen's dragon, Balerion, the Black\
        Dread",
        "The ancient books of Asshai prophesy the return of Azor Ahai,\
        following a long summer marked by bleeding stars",
        "Aegon the Conqueror dated the beginning of his reign from the day\
        the High Septon anointed him as king in Oldtown. That calendar is used\
        to this day",
        "Everything written about the Age of Heroes, the Dawn Age, and the\
        Long Night originates from stories written down by septons\
        thousands of years later",
        "George R. R. Martin intended to have a five or six year gap between\
        the events of A Storm of Swords and A Feast for Crows, but he\
        eventually scrapped the plan",
        "Brienne of Tarth was once betrothed to Ser Ronnet Connington",
        "Ser Loras Tyrell and Ser Lancel Lannister were born in the same year",
        "Grand Maester Pycelle was appointed to the small council during the\
        reign of King Aegon Targaryen the Fifth",
        "Grand Maester Pycelle saw the reigns of eight kings, for six of\
        which he served in the small council as Grand Maester",
        "King Robert, Stannis, and Renly Baratheon were second cousins\
        to Rhaegar, Viserys and Daenerys Targaryen",
        "There are in fact three Houses Baratheon. While originally there was\
        only House Baratheon of Storm's End, since Robert Baratheon took the\
        throne, House Baratheon of King's Landing and House Baratheon of\
        Dragonstone were created",
        "Sansa Stark fell madly in love with Ser Waymar Royce, the leading\
        ranger in the prologue of A Game of Thrones, whom she met when he was\
        on his way to the Wall",
        "Waymar Royce is the third son of Bronze Yohn Royce, one of the Lord\
        Declarants that Sansa meets in the Vale",
        "Circe (which is pronounced the same as Cersei) is a witch in Greek\
        mythology who murdered her husband",
        "Roy Dotrice, who holds a Guinness World Record for his reading of the\
        audiobook of A Game of Thrones, played Hallyne the pyromancer in\
        Season 2 of HBO's Game of Thrones",
        "Illyrio Mopatis and Varys were childhood friends in Pentos",
        "The Red Wedding is inspired by two similar events in Scottish\
        history, the Black Dinner and the Glencoe Massacre",
        "George R.R. Martin’s inspiration for the Wall of Westeros\
        was Hadrian's Wall in Northern England",
        "The Faith of the Seven, in which a single god has seven aspects, was\
        inspired by the Christian Trinity, in which God has three\
        aspects: the father, the son and the holy ghost",
        "The Others can be killed with dragonglass, whereas their undead\
        thralls, the wights, cannot",
        "Wights retain some memories from before they died",
        "Prince Aemon the Dragonknight was held captive in a crow cage,\
        located above a pit filled with vipers, after Dornish rebels betrayed\
        and killed King Daeron Targaryen the First",
        "Lord Tytos Lannister, the father of Lord Tywin Lannister, was a\
        thirdborn son, and was thus never expected to rule",
        "Ser Duncan the Tall met the future Lord Walder Frey when Walder was\
        only four years old",
        "The first seat from where Aegon Targaryen ruled was called\
        the Aegonfort. Aegon eventually decided it was unsuited to be the\
        seat of power for a king, so he temporarily moved his family\
        from King's Landing back to Dragonstone. The Aegonfort was razed to\
        the ground and construction of the Red Keep began",
        "The dwarfs Quentyn Martell and Gerris Drinkwater saw performing\
        their folly in Volantis were Penny and her brother Oppo, on their\
        dog and pig, Crunch and Pretty Pig",
        "A member of House Frey named Rhaegar has a son named Robert",
        "Mance Rayder was present during the feast held at Winterfell to\
        welcome King Robert Baratheon to the North at the start of A Game of\
        Thrones",
        "There have been eleven Targaryens who were named Aegon Targaryen over\
        the past four hundred years",
        "More people died during the rebellion that followed King Daeron\
        Targaryen's conquest of Dorne, than during the actual conquest",
        "Lord Luthor Tyrell and Lady Olenna Redwyne, the parents of Lord Mace\
        Tyrell, were, at one point, both betrothed to a Targaryen",
        "King Jaehaerys I and Queen Alysanne Targaryen were married for\
        forty-six years",
        "Most consider Highgarden to be the most beautiful castle in the Seven\
        Kingdoms. Only the lords of the Vale challenge this claim, preferring\
        the Eyrie",
        "The last of the Targaryen dragons died in 153 AC, the same year as\
        future King Daeron Targaryen was born",
        "Dorne officially joined the Seven Kingdoms 187 years after Aegon's\
        Conquest",
        "The mother of King Aegon Targaryen the Fifth was a Dayne",
        "King Aerys Targaryen the Second, and Queen Rhaella suffered three\
        miscarriages, two stillbirths and three deaths in the cradle between\
        the births of Princes Rhaegar and Viserys",
        "Eddard Stark's mother was called Lyarra Stark. She and Eddard's\
        father Rickard were cousins",
        "Braavos is not only the youngest, but also the wealthiest of the\
        nine Free Cities",
        "Aegon the Conqueror's crown was lost when King Daeron Targaryen died\
        in Dorne in 161 AC",
        "House Manderly originates from the Reach",
        "Casterly Rock is two leagues long, and three times as high as\
        the Wall",
        "Pyke might be the oldest castle in Westeros",
        "Following the conclusion of the Dance of the Dragons, Dowager\
        Queen Alicent Hightower spent the remainder of her life imprisoned,\
        until she died during the outbreak of the Winter Fever in 133 AC",
        "Maester Aemon was named by his grandfather, King Daeron Targaryen",
        "The Dothraki Sea, from the Forest of Qohor to the Bone Mountains,\
        stretches more than seven hundred leagues",
        "The wealth of Tyrosh originates from a rare species of sea snails",
        "In the forest of Qohor, lemurs can be found which are said to have\
        silver-white fur and purple eyes. They are sometimes called Little\
        Valyrians",
        "Meria Martell, the Princess of Dorne during Aegon's Conquest, died\
        in 13 AC in her early nineties. She had ruled Dorne for more than\
        seventy years",
        "Norvoshi women, both highborn and lowborn, shave off all their body\
        hair",
        "When the Lorathi King Qarlon the Great laid siege on Norvos,\
        the Valyrian Freehold rose to defend her daughter, resulting in\
        the Scouring of Lorath. No man, woman, or child survived, and Lorath\
        was uninhabited for more than a century thereafter",
        "King Daeron Targaryen intended to wed one of his sisters to\
        the Sealord of Braavos",
        "Daemon Blackfyre the Second had a prophetic dream in which he\
        saw Duncan the Tall as a member of the Kingsguard, long before Duncan\
        actually joined the order",
        "During the past two centuries, no less than six wars were fought\
        between Pentos and Braavos. The Braavosi victory of this conflict\
        resulted in a ban on slavery in Pentos",
        "Daemon Blackfyre the First was named by his mother for her\
        grandfather, Prince Daemon Targaryen, who lived during the Dance of\
        the Dragons",
        "Any foreigner who spends too much time on Naath contracts a\
        mysterious, deadly illness. The Naathi themselves are not affected",
    ]
    return unicode("Did you know? " + random.choice(factlist), "utf-8")


def randFact():
    factlist = [
        aka,
        houseSigil,
        houseWords,
        playedBy,
        curatedFact,
    ]
    return random.choice(factlist)()
