# -*- coding: utf-8 -*-
import logging
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
from facts import randFact
from trivia import generateQuestions
from models import ThroneFacts
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
app = Flask(__name__)

ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

tree = {
    1: {
        "question": "Is your favorite season Winter, or Summer?",
        "responses": {
            "winter": 2,
            "summer": 3
        }
    },
    2: {
        "question": "Is loyalty important to you?",
        "responses": {
            "no": 4,
            "yes": 5,
        }
    },
    3: {
        "question": "Do you like to travel by air, by land, or by sea?",
        "responses": {
            "air": 6,
            "land": 7,
            "sea": 8,
        }
    },
    4: {
        "question": "Do you enjoy torturing people for fun?",
        "responses": {
            "yes": 9,
            "no": 10,
        }
    },
    5: {
        "question": "Do most of your clothes lack any color?",
        "responses": {
            "yes": 11,
            "no": 12,
        }
    },
    6: {
        "question": "Do you like playing with fire?",
        "responses": {
            "yes": 13,
            "no": 14,
        }
    },
    7: {
        "question": "Are you insanely wealthy?",
        "responses": {
            "yes": 15,
            "no": 16,
        }
    },
    8: {
        "question": "Do you generally put your family's\
         needs before your own?",
        "responses": {
            "yes": 17,
            "no": 18,
        }
    },
    9: {
        "house": "House Bolton of the Dreadfort",
        "desc": "House Bolton of the Dreadfort is a noble house from the\
        Dreadfort in the north. They are an old line descended from the First\
        Men and dating back to the Age of Heroes. The Boltons are known for\
        their practice of flaying their enemies.",
    },
    10: {
        "house": "House Karstark of Karhold",
        "desc": "House Karstark of Karhold is a noble house from Karhold in the\
        north. They are a cadet branch of their overlords, the Starks of\
        Winterfell, and are among their principal bannermen. Karstarks are\
        big, fierce men, bearded and long-haired, with brown hair and\
        blue-grey eyes, and favor wearing cloaks made of the pelts of seals,\
        bears, and wolves."
    },
    11: {
        "question": "Are you a dog person?",
        "responses": {
            "yes": 19,
            "no": 20,
        }
    },
    12: {
        "question": "Do you have prophetic tendencies?",
        "responses": {
            "yes": 21,
            "no": 22,
        }
    },
    13: {
        "house": "House Targaryen of Valyria",
        "desc": "House Targaryen is a noble family of Valyrian descent, and is\
        the only family of dragonlords who survived the Doom of Valyria. They\
        left Valyria twelve years before the Doom occurred and resided for\
        more than a century on the island of Dragonstone, until Aegon\
        the Conqueror and his sister-wives began their conquest in 2 BC. House\
        Targaryen ruled as the kings on the Iron Throne and as the Great House\
        of the crownlands for nearly three hundred years."
    },
    14: {
        "house": "House Arryn of The Eyrie",
        "desc": "House Arryn of the Eyrie is one of the Great Houses of\
        Westeros, and is the principal noble house in the Vale of Arryn. Their\
        main seat is the Eyrie, which is considered impregnable. House Arryn\
        has at least one other holding, their winter castle at the Gates of\
        the Moon, which was once their main seat."
    },
    15: {
        "question": "Are you a cat person?",
        "responses": {
            "yes": 23,
            "no": 24,
        }
    },
    16: {
        "question": "Do you like horse back riding?",
        "responses": {
            "yes": 25,
            "no": 26,
        }
    },
    17: {
        "house": "House Tully of Riverrun",
        "desc": "House Tully of Riverrun is one of the Great Houses of the\
        Seven Kingdoms. Lord Hoster Tully, the Lord Paramount of the Trident,\
        rules over the riverlands from the Tully seat of Riverrun."
    },
    18: {
        "house": "House Greyjoy of The Iron Islands",
        "desc": "House Greyjoy of Pyke is one of the Great Houses of Westeros.\
        It rules over the Iron Islands, a harsh and bleak collection of\
        forbidding islands off the west coast of Westeros, from the Seastone\
        Chair in the castle of Pyke on the island of the same name."
    },
    19: {
        "house": "House Stark of Winterfell",
        "desc": "House Stark of Winterfell is one of the Great Houses of\
        Westeros and the principal noble house of the north. In days of old\
        they ruled as Kings of Winter, but since Aegon's Conquest they have\
        been Wardens of the North and ruled as Lords of Winterfell."
    },
    20: {
        "house": "The Night's Watch of Castle Black",
        "desc": "The Night's Watch is a military order dedicated to holding\
        the Wall, the immense fortification on the northern border of the\
        Seven Kingdoms, defending the realms of men from what lies beyond the\
        Wall. The order's foundation dates back to the Age of Heroes, at the\
        time when the Others were pushed back. The men of Night's Watch wear\
        only black, and they are known as black brothers. Recruits who join\
        the Watch are said to take the black."
    },
    21: {
        "house": "House Reed of Greywater Watch",
        "desc": "House Reed of Greywater Watch is a noble house from Greywater\
        Watch, and one of the principal families in the north. They rule the\
        crannogmen, small men who live in swamps and marshes in the Neck."
    },
    22: {
        "house": "House Manderly of White Harbor",
        "desc": "House Manderly of White Harbor is a noble family in the north\
        whose seat is the New Castle in the city of White Harbor. They are\
        among the most powerful and loyal vassals of House Stark as well as\
        the richest northern family due to their control of the only city in\
        the region."
    },
    23: {
        "house": "House Lannister of Casterly Rock",
        "desc": "House Lannister of Casterly Rock is one of the Great Houses\
        of Seven Kingdoms, and the principal house of the westerlands.\
        Fair-haired, tall, and handsome, the Lannisters are the blood of\
        Andal adventurers who carved out a mighty kingdom in the western hills\
        and valleys. Through the female line they boast of descent from Lann\
        the Clever, the legendary trickster of the Age of Heroes who tricked\
        the members of House Casterly into giving him Casterly Rock during the\
        era of the First Men."
    },
    24: {
        "house": "House Tyrell of Highgarden",
        "desc": "House Tyrell of Highgarden is one of the Great Houses of the\
        Seven Kingdoms, being Lords Paramount of the Mander and the liege\
        lords of the Reach. A large, wealthy house, its wealth is only\
        surpassed among the Great Houses by House Lannister. Highgarden is an\
        ancient seat of rule and the heart of chivalry in the Seven Kingdoms."
    },
    25: {
        "house": "The Dothraki in the grasslands of the Dothraki Sea",
        "desc": "The Dothraki people are a culture of nomadic warriors in\
        Essos who range across the vast grasslands of the Dothraki sea in\
        hordes known as khalasars. The Dothraki are large people with\
        copper-toned skin, dark almond eyes, and black hair."
    },
    26: {
        "question": "Do you prefer the music of David Bowie, or Toby Keith?",
        "responses": {
            "david bowie": 27,
            "toby keith": 28,
        }
    },
    27: {
        "house": "House Martell of Sunspear in Dorne",
        "desc": "House Nymeros Martell of Sunspear is one of the Great Houses\
        of Westeros, and is the ruling house of Dorne. True to their house\
        words, unboued, unbent, unbroken, they were the only house never\
        conquered by the Targaryens."
    },
    28: {
        "house": "House Baratheon of Storm's End",
        "desc": "House Baratheon of Storm's End is one of the Great Houses of\
        Westeros, and is the principal house in the stormlands. Members of the\
        family tend to be tall and powerfully built, with black hair and blue\
        eyes, as well as strong, square jawlines. Their seat, Storm's End, is\
        an ancient castle raised by the Storm Kings from the now-extinct House\
        Durrandon."
    },
    29: {
        "question": "",
        "answer": ""
    },
    30: {
        "question": "",
        "answer": ""
    },
    31: {
        "question": "",
        "answer": ""
    },
    32: {
        "question": "",
        "answer": ""
    },
    33: {
        "question": "",
        "answer": ""
    },
    34: {
        "question": "",
        "answer": ""
    },
}


@ask.launch
def launch():
    greeting = render_template('hello')
    return question(greeting)


@ask.intent('GetNewFactIntent')
def get_new_fact():
    return statement(randFact())


@ask.intent('StartHouseQuiz')
def start_house_quiz():
    if 'node' not in session.attributes:
        session.attributes['node'] = 1
        session.attributes['quiz'] = True
        return question(tree[session.attributes['node']]['question'])


@ask.intent('StartTrivia')
def start_trivia():
    if 'node' not in session.attributes:
        generateQuestions(tree)
        session.attributes['node'] = 29
        session.attributes['correct'] = 0
        session.attributes['turn'] = 1
        return question("Let's get started!\
        First Question. " + tree[session.attributes['node']]['question'])


@ask.intent('PlayGame', mapping={'response': 'Response'})
def play_game(response):
    node = session.attributes['node']
    # check if the response is right
    if node < 29:
        responsebool = False
        print response
        for resp in tree[node]['responses']:
            if response.lower() in resp.lower() or resp.lower() in response.lower():
                responsebool = True
                rKey = resp.lower()
        # if there is a response
        if response is not None:
            # repeat the question if they say repeat
            if 'repeat' in response:
                repeat_q = tree[node]['question']
                return question(repeat_q)
            elif responsebool:
                session.attributes['node'] = tree[node]['responses'][rKey]
                node = session.attributes['node']
                if 'question' in tree[node]:
                    return question(tree[node]['question'])
                else:
                    house = tree[node]['house']
                    desc = tree[node]['desc']
                    try:
                        user = ThroneFacts.get(session.user.userId)
                    except ThroneFacts.DoesNotExist:
                        user = ThroneFacts(session.user.userId)
                    user.update_item('house', desc, action='put')
                    session.attributes.pop('node')
                    return statement("You are a member of " + house)
            # an incorrect response
            else:
                repeat = render_template('repeat_response')
                return question(repeat)
            # use the correct response to go to the next node
        # no response, prompt for a repeated response
        elif response is None:
            return question(repeat)
    else:
        correct_answer = tree[node]['answer']
        answerbool = (correct_answer.lower() in response.lower() or
                      response.lower() in correct_answer.lower())
        if node == 34:
            if answerbool:
                session.attributes['correct'] += 1
                end_statement = "Good job! You got \
                " + str(session.attributes['correct']) + " correct!"
            else:
                end_statement = "No. I'm sorry, that's not right. The correct\
                answer was " + correct_answer + ". You got \
                " + str(session.attributes['correct']) + " correct!"
            try:
                user = ThroneFacts.get(session.user.userId)
            except ThroneFacts.DoesNotExist:
                user = ThroneFacts(session.user.userId)
            user = ThroneFacts.get(session.user.userId)
            correct = user.num_correct
            total = user.num_total
            new_score = (correct + session.attributes['correct']) *\
                        (correct + session.attributes['correct']) / (total + 6)
            user.update({
                'num_correct': {
                    'value': session.attributes['correct'],
                    'action': "add"
                },
                'num_total': {
                    'value': 6,
                    'action': "add"
                },
                'score': {
                    'value': new_score,
                    'action': "put"
                },
            })
            return statement(end_statement)
        elif answerbool:
            session.attributes['correct'] += 1
            session.attributes['node'] += 1
            session.attributes['turn'] += 1
            return question("That is correct! Good Job!\
            Question " + str(session.attributes['turn']) + ": \
            " + tree[session.attributes['node']]['question'])
        else:
            session.attributes['turn'] += 1
            session.attributes['node'] += 1
            return question("No. I'm sorry that's not right. The correct\
            answer was " + correct_answer + ". Next question! \
            " + tree[session.attributes['node']]['question'])


@ask.intent('TellMeMore')
def tell_me_more():
    if 'node' not in session.attributes:
        try:
            user = ThroneFacts.get(session.user.userId)
        except ThroneFacts.DoesNotExist:
            user = ThroneFacts(session.user.userId)
        if user.house is not "None":
            return statement(user.house)
        else:
            return statement("You are not a member of any House. Take the quiz to\
            find out what house you are in!")
    else:
        return question("Please complete this game first!")


@ask.intent('AMAZON.StopIntent')
def stop():
    return statement("Goodbye")


@ask.intent('AMAZON.CancelIntent')
def cancel():
    return statement("Goodbye")


@ask.intent('AMAZON.HelpIntent')
def help():
    help_text = render_template('help')
    return question(help_text)


@ask.session_ended
def session_ended():
    if 'quiz' in session.attributes:
        session.attributes.pop('quiz')
    if 'node' in session.attributes:
        session.attributes.pop('node')
    if 'quiz' in session.attributes:
        session.attributes.pop('quiz')
    return "", 200


if __name__ == '__main__':
    app.run(debug=True)
