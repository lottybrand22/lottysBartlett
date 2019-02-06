import json

from dallinger.nodes import Source
from dallinger.models import Node, Info

class LottyNode(Node):

    __mapper_args__ = {
        "polymorphic_identity": "lotty_node"
    }

    @property
    def name(self):
        return json.loads(self.property1)["name"]

    @property
    def n_copies(self):
        return json.loads(self.property1)["n_copies"]

    @property
    def asoc_score(self):
        return json.loads(self.property1)["asoc_score"]

    @property
    def score(self):
        return json.loads(self.property1)["score"]

    @property
    def bonus(self):
        return json.loads(self.property1)["bonus"]

    @name.setter
    def name(self, val):
        p1 = json.loads(self.property1)
        p1["name"] = val
        self.property1 = json.dumps(p1)

    @n_copies.setter
    def n_copies(self, val):
        p1 = json.loads(self.property1)
        p1["n_copies"] = val
        self.property1 = json.dumps(p1)

    @asoc_score.setter
    def asoc_score(self, val):
        p1 = json.loads(self.property1)
        p1["asoc_score"] = val
        self.property1 = json.dumps(p1)

    @score.setter
    def score(self, val):
        p1 = json.loads(self.property1)
        p1["score"] = val
        self.property1 = json.dumps(p1)

    @bonus.setter
    def bonus(self, val):
        p1 = json.loads(self.property1)
        p1["bonus"] = val
        self.property1 = json.dumps(p1)

class LottyInfo(Info):

    __mapper_args__ = {
        "polymorphic_identity": "lotty_info"
    }

    @property
    def number(self):
        return json.loads(self.property1)["number"]

    @property
    def copying(self):
        return json.loads(self.property1)["copying"]

    @property
    def score(self):
        return json.loads(self.property1)["score"]

    @property
    def info_chosen(self):
        return json.loads(self.property1)["info_chosen"]

    @property
    def round(self):
        return json.loads(self.property1)["round"]

    @number.setter
    def number(self, val):
        p1 = json.loads(self.property1)
        p1["number"] = val
        self.property1 = json.dumps(p1)

    @copying.setter
    def copying(self, val):
        p1 = json.loads(self.property1)
        p1["copying"] = val
        self.property1 = json.dumps(p1)

    @score.setter
    def score(self, val):
        p1 = json.loads(self.property1)
        p1["score"] = val
        self.property1 = json.dumps(p1)

    @info_chosen.setter
    def info_chosen(self, val):
        p1 = json.loads(self.property1)
        p1["info_chosen"] = val
        self.property1 = json.dumps(p1)

    @round.setter
    def round(self, val):
        p1 = json.loads(self.property1)
        p1["round"] = val
        self.property1 = json.dumps(p1)

class QuizSource(Source):
    """A Source that reads in a question from a file and transmits it."""

    __mapper_args__ = {
        "polymorphic_identity": "quiz_source"
    }

    def _contents(self):
        """Define the contents of new Infos .... (New transmissions??)

        transmit() -> _what() -> create_information() -> _contents().
        """
        number_transmissions = len(self.infos())
        import json
        questions = [
            json.dumps({
                'question': 'How many letters are in the alphabet?',
                'number':'practice 1',
                'round': 0,
                'topic': 'Practice',
                'Wwer': '32',
                'Rwer': '26',
                'pic': False, 
                }),
            json.dumps({
                'question': 'What is the capital of France?',
                'number':'practice 2',
                'round': 0,
                'topic': 'Practice',
                'Wwer': 'Paris',
                'Rwer': 'Barcelona',
                'pic': False, 
                }),
            json.dumps({
                'question': 'How many days does February have?',
                'number':'practice 3',
                'round': 0,
                'topic': 'Practice',
                'Wwer': '30',
                'Rwer': '28',
                'pic': False, 
                }),
            json.dumps({
                'question': 'In which country is the red dot located?',
                'number':1,
                'round': 1,
                'topic': 'Geography',
                'Wwer': 'Guatemala',
                'Rwer': 'Belize',
                'pic': True, 
                }),
            json.dumps({
                'question': 'In which country is the red dot located?',
                'number':2,
                'round':1,
                'topic': 'Geography',
                'Wwer': 'Nigeria',
                'Rwer': 'The Ivory Coast',
                'pic': True, 
                }),
            json.dumps({
                'question': 'The capital of Hawaii is',
                'number':3,
                'round':1,
                'topic': 'Geography',
                'Wwer': 'Waikiki',
                'Rwer': 'Honolulu',
                'pic': False, 
                }),
            json.dumps({
                'question': 'Saint Helena is an island in',
                'number':4,
                'round':1,
                'topic':'Georgraphy',
                'Wwer': 'The Indian Ocean',
                'Rwer': 'The South Atlantic Ocean',
                'pic': False,
                }),
            json.dumps({
                'question': 'Which country shares a border with El Salvador?',
                'number':5,
                'round':1,
                'topic':'Georgraphy',
                'Wwer': 'Paraguay',
                'Rwer': 'Honduras',
                'pic': False,
                }),
            json.dumps({
                'question': 'The capital of the Philippines is?',
                'number':6,
                'round':1,
                'topic':'Georgraphy',
                'Wwer': 'Davao',
                'Rwer': 'Manila',
                'pic': False,
                }),
            json.dumps({
                'question': 'Which is closest to Finland?',
                'number':7,
                'round':1,
                'topic':'Georgraphy',
                'Wwer': 'Moscow',
                'Rwer': 'St Petersburg',
                'pic': False,
                }),
            json.dumps({
                'question': 'Which is the largest of The Canary Islands?',
                'number':8,
                'round':1,
                'topic':'Georgraphy',
                'Wwer': 'Gran Canaria',
                'Rwer': 'Tenerife',
                'pic': False,
                }),
            json.dumps({
                'question': 'Oklahoma state shares a border with?',
                'number':9,
                'round':1,
                'topic':'Georgraphy',
                'Wwer': 'Arizona',
                'Rwer': 'New Mexico',
                'pic': False,
                }),
            json.dumps({
                'question': 'Amsterdam is nearer to?',
                'number':10,
                'round':1,
                'topic':'Georgraphy',
                'Wwer': 'Antwerp',
                'Rwer': 'Rotterdam',
                'pic': False,
                }),
            json.dumps({
                'question': 'A pot of nail varnish weighs?',
                'number':11,
                'round':1,
                'topic':'Weight estimation',
                'Wwer': '162g',
                'Rwer': '62g',
                'pic': True,
                }),
            json.dumps({
                'question': 'A Rubiks cube weighs?',
                'number':12,
                'round': 1,
                'topic': 'Weight',
                'Wwer': '1.4kg',
                'Rwer': '0.14kg',
                'pic': True,
                }),
            json.dumps({
                'question': 'A blue whale weighs?',
                'number':13,
                'round': 1,
                'topic': 'Weight',
                'Wwer': '1,400kg',
                'Rwer': '140,000kg',
                'pic': False,
                }),
            json.dumps({
                'question': 'A tennis ball weighs?',
                'number':14,
                'round': 1,
                'topic': 'Weight',
                'Wwer': '5.85g',
                'Rwer': '58.5g',
                'pic': False,
                }),
            json.dumps({
                'question': 'Which weighs more, on average?',
                'number':15,
                'round': 1,
                'topic': 'Weight',
                'Wwer': 'A wood pigeon',
                'Rwer': 'A seagull',
                'pic': False,
                }),
            json.dumps({
                'question': 'A Boeing 747 (on take-off) weighs?',
                'number':16,
                'round': 1,
                'topic': 'Weight',
                'Wwer': '40,000kg',
                'Rwer': '400,000kg',
                'pic': False,
                }),
            json.dumps({
                'question': 'A skateboard weighs?',
                'number':17,
                'round': 1,
                'topic': 'Weight',
                'Wwer': '34kg',
                'Rwer': '3.4kg',
                'pic': False,
                }),
            json.dumps({
                'question': 'A newborn baby weighs?',
                'number':18,
                'round': 1,
                'topic': 'Weight',
                'Wwer': '34kg',
                'Rwer': '3.5kg',
                'pic': False,
                }),
            json.dumps({
                'question': 'A female giraffe weighs?',
                'number':19,
                'round': 1,
                'topic': 'Weight',
                'Wwer': '83kg',
                'Rwer': '830kg',
                'pic': False,
                }),
            json.dumps({
                'question': 'Which weighs more?',
                'number':20,
                'round': 1,
                'topic': 'Weight',
                'Wwer': 'The London Eye',
                'Rwer': 'The Eiffel Tower',
                'pic': False,
                }),
            json.dumps({
                'question': '\"Cal\" means \"horse\" in which language?',
                'number':21,
                'round': 1,
                'topic': 'Language',
                'Wwer': 'Hungarian',
                'Rwer': 'Romanian',
                'pic': False,
                }),
            json.dumps({
                'question': '\"Kieselstein\" means \"pebbles\" in which language?',
                'number':22,
                'round': 1,
                'topic': 'Language',
                'Wwer': 'Russian',
                'Rwer': 'German',
                'pic': False,
                }),
            json.dumps({
                'question': '\"Gobierno\" means \"government\" in which language?',
                'number':23,
                'round': 1,
                'topic': 'Language',
                'Wwer': 'Portugese',
                'Rwer': 'Spanish',
                'pic': False,
                }),
            json.dumps({
                'question': '\"Verre\" means \"glass\" in which language?',
                'number':24,
                'round': 1,
                'topic': 'Language',
                'Wwer': 'Italian',
                'Rwer': 'French',
                'pic': False,
                }),
            json.dumps({
                'question': '\"Bere\" means \"drink\" in which language?',
                'number':25,
                'round': 1,
                'topic': 'Language',
                'Wwer': 'German',
                'Rwer': 'Italian',
                'pic': False,
                }),
            json.dumps({
                'question': '\"Kabaha\" means \"shoes\" in which language?',
                'number':26,
                'round':1,
                'topic': 'Language',
                'Wwer': 'Swahili',
                'Rwer': 'Somali',
                'pic': False,
                }),
            json.dumps({
                'question': '\"Bocadillo\" means \"snack\" in which language?',
                'number':27,
                'round':1,
                'topic': 'Language',
                'Wwer': 'French',
                'Rwer': 'Spanish',
                'pic': False,
                }),
            json.dumps({
                'question': '\"Rzeka\" means \"river\" in which language?',
                'number':28,
                'round': 1,
                'topic':'Language',
                'Wwer': 'Latvian',
                'Rwer': 'Polish',
                'pic': False,
                }),
            json.dumps({
                'question': 'The above means \"fire\" in which language?',
                'number':29,
                'round':1,
                'topic': 'Language',
                'Wwer': 'Bulgarian',
                'Rwer': 'Russian',
                'pic': True,
                }),
            json.dumps({
                'question': 'The above means \"soul\" in which language?',
                'number':30,
                'round':1,
                'topic': 'Language',
                'Wwer': 'Armenian',
                'Rwer': 'Arabic',
                'pic': True,
                }),
            json.dumps({
                'question': 'The above is an image of a painting by which artist?',
                'number':31,
                'round':1,
                'topic': 'Art',
                'Wwer': 'Edouard Manet',
                'Rwer': 'Claude Monet',
                'pic': True,
                }),
            json.dumps({
                'question': 'The above is an image of a painting by which artist?',
                'number':32,
                'round':1,
                'topic': 'Art',
                'Wwer': 'Rudolf Hausner',
                'Rwer': 'Gustav Klimt',
                'pic': True,
                }),
            json.dumps({
                'question': 'Edouard Manet died in',
                'number':33,
                'round':1,
                'topic': 'Art',
                'Wwer': '1663',
                'Rwer': '1883',
                'pic': False,
                }),
            json.dumps({
                'question': '\"The starry night\" is a famous painting by',
                'number':34,
                'round':1,
                'topic': 'Art',
                'Wwer': 'Jackson Pollock',
                'Rwer': 'Vincent van Gogh',
                'pic': False,
                }),
            json.dumps({
                'question': '\"The singing butler\" is a painting by the Scottish painter:',
                'number':35,
                'round':1,
                'topic': 'Art',
                'Wwer': 'Andrew Geddes',
                'Rwer': 'Jack Vettriano',
                'pic': False,
                }),
            json.dumps({
                'question': 'Antoni Gaudi was a Spanish:',
                'number':36,
                'round':1,
                'topic': 'Art',
                'Wwer': 'Poet',
                'Rwer': 'Architect',
                'pic': False,
                }),
            json.dumps({
                'question': 'Auguste Rodin was a French:',
                'number':37,
                'round':1,
                'topic': 'Art',
                'Wwer': 'Architect',
                'Rwer': 'Sculptor',
                'pic': False,
                }),
            json.dumps({
                'question': 'Rembrandt was famous for which style of painting?',
                'number':38,
                'round':1,
                'topic': 'Art',
                'Wwer': 'Surrealism',
                'Rwer': 'Baroque',
                'pic': False,
                }),
            json.dumps({
                'question': 'Paul Gauguin was a famous post-impressionist artist from:',
                'number':39,
                'round':1,
                'topic': 'Art',
                'Wwer': 'Italy',
                'Rwer': 'France',
                'pic': False,
                }),
            json.dumps({
                'question': 'Edgar Degas famously painted',
                'number':40,
                'round':1,
                'topic': 'Art',
                'Wwer': 'water lilies',
                'Rwer': 'dancers',
                'pic': False,
                }),
            json.dumps({
                'question': 'In which city is the red dot located?',
                'number':41,
                'round':2,
                'topic': 'Geography',
                'Wwer': 'Seattle',
                'Rwer': 'Philadelphia',
                'pic': True,
                }),
            json.dumps({
                'question': 'In which country is the red dot located?',
                'number':42,
                'round':2,
                'topic': 'Geography',
                'Wwer': 'Greece',
                'Rwer': 'Bulgaria',
                'pic': True,
                }),
            json.dumps({
                'question': 'In which country is the red dot located?',
                'number':43,
                'round':2,
                'topic': 'Geography',
                'Wwer': 'Laos',
                'Rwer': 'Vietnam',
                'pic': True,
                }),
            json.dumps({
                'question': 'Which city is closer to Rome?',
                'number':44,
                'round':2,
                'topic': 'Geography',
                'Wwer': 'Florence',
                'Rwer': 'Naples',
                'pic': False,
                }),
            json.dumps({
                'question': 'Kazakhstan shares a border with?',
                'number':45,
                'round':2,
                'topic': 'Geography',
                'Wwer': 'Tajikistan',
                'Rwer': 'Kyrgyzstan',
                'pic': False,
                }),
            json.dumps({
                'question': 'The Virgin Islands are closer to:',
                'number':46,
                'round':2,
                'topic': 'Geography',
                'Wwer': 'The Indian Ocean',
                'Rwer': 'The Caribbean Sea',
                'pic': False,
                }),
            json.dumps({
                'question': 'Brussels is a city in:',
                'number':47,
                'round':2,
                'topic': 'Geography',
                'Wwer': 'Germany',
                'Rwer': 'Belgium',
                'pic': False,
                }),
            json.dumps({
                'question': 'Melbourne is a city in:',
                'number':48,
                'round':2,
                'topic': 'Geography',
                'Wwer': 'New Zealand',
                'Rwer': 'Australia',
                'pic': False,
                }),
            json.dumps({
                'question': 'Paris is closer to:',
                'number':49,
                'round':2,
                'topic': 'Geography',
                'Wwer': 'Bordeaux',
                'Rwer': 'Calais',
                'pic': False,
                }),
            json.dumps({
                'question': 'Sri Lanka is an island off the coast of:',
                'number':50,
                'round':2,
                'topic': 'Geography',
                'Wwer': 'Cambodia',
                'Rwer': 'India',
                'pic': False,
                }),
            json.dumps({
                'question': 'Liberia shares a border with:',
                'number':51,
                'round':2,
                'topic': 'Geography',
                'Wwer': 'Morocco',
                'Rwer': 'Guinea',
                'pic': False,
                }),
            json.dumps({
                'question': 'Oman shares a border with',
                'number':52,
                'round':2,
                'topic': 'Geography',
                'Wwer': 'Kuwait',
                'Rwer': 'Saudi Arabia',
                'pic': False,
                }),
            json.dumps({
                'question': 'Copenhagen is closer to:',
                'number':53,
                'round':2,
                'topic': 'Geography',
                'Wwer': 'Oslo',
                'Rwer': 'Gothenburg',
                'pic': False,
                }),
            json.dumps({
                'question': 'The Shetland Islands are part of:',
                'number':54,
                'round':2,
                'topic': 'Geography',
                'Wwer': 'Iceland',
                'Rwer': 'Scotland',
                'pic': False,
                }),
            json.dumps({
                'question': 'Tokyo is closer to:',
                'number':55,
                'round':2,
                'topic': 'Geography',
                'Wwer': 'Kyoto',
                'Rwer': 'Hamamatsu',
                'pic': False,
                }),
            json.dumps({
                'question': 'Which dog weighs more, on average?',
                'number':56,
                'round':2,
                'topic': 'Weight',
                'Wwer': 'Labrador',
                'Rwer': 'Great dane',
                'pic': False,
                }),
            json.dumps({
                'question': 'What is the average weight of a \"pink salmon\"?',
                'number':57,
                'round':2,
                'topic': 'Weight',
                'Wwer': '17kg',
                'Rwer': '1.7kg',
                'pic': True,
                }),
            json.dumps({
                'question': 'A cricket bat weighs?',
                'number':58,
                'round':2,
                'topic': 'Weight',
                'Wwer': '14kg',
                'Rwer': '1.4kg',
                'pic': True,
                }),
            json.dumps({
                'question': 'The average weight of a camel is:',
                'number':59,
                'round':2,
                'topic': 'Weight',
                'Wwer': '48kg',
                'Rwer': '480kg',
                'pic': True,
                }),
            json.dumps({
                'question': 'What does a typical, office fire extinguisher weigh?',
                'number':60,
                'round':2,
                'topic': 'Weight',
                'Wwer': '115kg',
                'Rwer': '1.15kg',
                'pic': False,
                }),
            json.dumps({
                'question': 'What is the average weight of an oak tree?',
                'number':61,
                'round':2,
                'topic': 'Weight',
                'Wwer': '900kg',
                'Rwer': '9000kg',
                'pic': False,
                }),
            json.dumps({
                'question': 'What does a typical car tyre weigh?',
                'number':62,
                'round':2,
                'topic': 'Weight',
                'Wwer': '0.7kg',
                'Rwer': '7kg',
                'pic': False,
                }),
            json.dumps({
                'question': 'Which weighs more, on average?',
                'number':63,
                'round':2,
                'topic': 'Weight',
                'Wwer': 'A hen\'s egg',
                'Rwer': 'An ostrich egg',
                'pic': False,
                }),
            json.dumps({
                'question': 'Which weighs more, on average?',
                'number':64,
                'round':2,
                'topic': 'Weight',
                'Wwer': 'An olive',
                'Rwer': 'A fig',
                'pic': False,
                }),
            json.dumps({
                'question': 'How much does an average loaf of bread weigh?',
                'number':65,
                'round':2,
                'topic': 'Weight',
                'Wwer': '40g',
                'Rwer': '400g',
                'pic': False,
                }),
            json.dumps({
                'question': 'How much does a barrel of whisky weigh?',
                'number':66,
                'round':2,
                'topic': 'Weight',
                'Wwer': '2000kg',
                'Rwer': '200kg',
                'pic': False,
                }),
            json.dumps({
                'question': 'How much does an average grizzly bear weigh?',
                'number':67,
                'round':2,
                'topic': 'Weight',
                'Wwer': '3,400kg',
                'Rwer': '340kg',
                'pic': False,
                }),
            json.dumps({
                'question': 'How much does a typical jacket potato weigh?',
                'number':68,
                'round':2,
                'topic': 'Weight',
                'Wwer': '18g',
                'Rwer': '180g',
                'pic': False,
                }),
            json.dumps({
                'question': 'Which weighs more, on average?',
                'number':69,
                'round':2,
                'topic': 'Weight',
                'Wwer': 'An apricot',
                'Rwer': 'An avocado',
                'pic': False,
                }),
            json.dumps({
                'question': 'Which weighs more, on average?',
                'number':70,
                'round':2,
                'topic': 'Weight',
                'Wwer': 'A coconut',
                'Rwer': 'A watermelon',
                'pic': False,
                }),
             json.dumps({
                'question': '\"Chave\" means \"key\" in which language?',
                'number':71,
                'round': 2,
                'topic':'Language',
                'Wwer': 'Spanish',
                'Rwer': 'Portugese',
                'pic': False,
                }),
             json.dumps({
                'question': '\"Umut\" means \"hope\" in which language?',
                'number':72,
                'round': 2,
                'topic':'Language',
                'Wwer': 'German',
                'Rwer': 'Turkish',
                'pic': False,
                }),
             json.dumps({
                'question': u'\"B\xe9ke\" means \"peace\" in which language?'.encode('utf-8'),
                'number':73,
                'round': 2,
                'topic':'Language',
                'Wwer': 'Polish',
                'Rwer': 'Hungarian',
                'pic': False,
                }),
             json.dumps({
                'question': '\"Bloem\" means \"flower\" in which language?',
                'number':74,
                'round': 2,
                'topic':'Language',
                'Wwer': 'Danish',
                'Rwer': 'Dutch',
                'pic': False,
                }),
             json.dumps({
                'question': '\"Sel\" means \"salt\" in which language?',
                'number':75,
                'round': 2,
                'topic':'Language',
                'Wwer': 'German',
                'Rwer': 'French',
                'pic': False,
                }),
             json.dumps({
                'question': '\"Schuh\" means \"shoe\" in which language?',
                'number':76,
                'round': 2,
                'topic':'Language',
                'Wwer': 'Dutch',
                'Rwer': 'German',
                'pic': False,
                }),
             json.dumps({
                'question': '\"Strom\" means \"tree\" in which language?',
                'number':77,
                'round': 2,
                'topic':'Language',
                'Wwer': 'Ukranian',
                'Rwer': 'Slovak',
                'pic': False,
                }),
             json.dumps({
                'question': '\"Hai\" means \"shark\" in which language?',
                'number':78,
                'round': 2,
                'topic':'Language',
                'Wwer': 'Telugu',
                'Rwer': 'Finnish',
                'pic': False,
                }),
             json.dumps({
                'question': '\"Dronning\" means \"queen\" in which language?',
                'number':79,
                'round': 2,
                'topic':'Language',
                'Wwer': 'Serbian',
                'Rwer': 'Norwegian',
                'pic': False,
                }),
             json.dumps({
                'question': '\"Pudel\" means \"bottle\" in which language?',
                'number':80,
                'round': 2,
                'topic':'Language',
                'Wwer': 'Bulgarian',
                'Rwer': 'Estonian',
                'pic': False,
                }),
             json.dumps({
                'question': '\"Tay\" means \"hand\" in which language?',
                'number':81,
                'round': 2,
                'topic':'Language',
                'Wwer': 'Thai',
                'Rwer': 'Vietnamese',
                'pic': False,
                }),
             json.dumps({
                'question': '\"Vinaka\" means \"thank you\" in which language?',
                'number':82,
                'round': 2,
                'topic':'Language',
                'Wwer': 'Swedish',
                'Rwer': 'Fijian',
                'pic': False,
                }),
             json.dumps({
                'question': 'The above means \"to eat\" in which language?',
                'number':83,
                'round': 2,
                'topic':'Language',
                'Wwer': 'Swedish',
                'Rwer': 'Finnish',
                'pic': True,
                }),
             json.dumps({
                'question': 'The above means \"star\" in which language?',
                'number':84,
                'round': 2,
                'topic':'Language',
                'Wwer': 'Macedonian',
                'Rwer': 'Greek',
                'pic': True,
                }),
             json.dumps({
                'question': 'The above is \"festival\" written in which language?',
                'number':85,
                'round': 2,
                'topic':'Language',
                'Wwer': 'Japanese',
                'Rwer': 'Korean',
                'pic': True,
                }),
            json.dumps({
                'question': 'The above is an image of a painting by which artist?',
                'number':86,
                'round':2,
                'topic': 'Art',
                'Wwer': 'Franz Kline',
                'Rwer': 'Jackson Pollack',
                'pic': True,
                }),
            json.dumps({
                'question': 'The above is an image of a painting by which artist?',
                'number':87,
                'round':2,
                'topic': 'Art',
                'Wwer': 'Marcel Duchamp',
                'Rwer': 'Salvador Dali',
                'pic': True,
                }),
            json.dumps({
                'question': 'The above is an image associated with which artist?',
                'number':88,
                'round':2,
                'topic': 'Art',
                'Wwer': 'Roy Lichtenstein',
                'Rwer': 'Andy Warhol',
                'pic': True,
                }),
            json.dumps({
                'question': '\"Flaming June\" is a painting by:',
                'number':89,
                'round':2,
                'topic': 'Art',
                'Wwer': 'Jan van Eyck',
                'Rwer': 'Sir Frederic Leighton',
                'pic': False,
                }),
            json.dumps({
                'question': '\"The Creation of Adam\" is a painting by:',
                'number':90,
                'round':2,
                'topic': 'Art',
                'Wwer': 'Leonardo da Vinci',
                'Rwer': 'Michelangelo',
                'pic': False,
                }),
            json.dumps({
                'question': 'Henri Matisse was a French artist of the:',
                'number':91,
                'round':2,
                'topic': 'Art',
                'Wwer': '15th Century',
                'Rwer': '20th Century',
                'pic': False,
                }),
            json.dumps({
                'question': '\"The Scream\" is a painting by:',
                'number':92,
                'round':2,
                'topic': 'Art',
                'Wwer': 'Ernst Ludwig Kirchner',
                'Rwer': 'Edvard Munch',
                'pic': False,
                }),
            json.dumps({
                'question': '\"Girl with a Pearl Earring\" is a painting by:',
                'number':93,
                'round':2,
                'topic': 'Art',
                'Wwer': 'Peter Paul Rubens',
                'Rwer': 'Johannes Vermeer',
                'pic': False,
                }),
            json.dumps({
                'question': '\"The Mona Lisa\" is a painting by:',
                'number':94,
                'round':2,
                'topic': 'Art',
                'Wwer': 'Vincent van Gogh',
                'Rwer': 'Leonardo da Vinci',
                'pic': False,
                }),
            json.dumps({
                'question': 'Rene Magritte was famous for:',
                'number':95,
                'round':2,
                'topic': 'Art',
                'Wwer': 'Impressionism',
                'Rwer': 'Surrealism',
                'pic': False,
                }),
            json.dumps({
                'question': 'Frida Kahlo was a famous painter from:',
                'number':96,
                'round':2,
                'topic': 'Art',
                'Wwer': 'South Africa',
                'Rwer': 'Mexico',
                'pic': False,
                }),
            json.dumps({
                'question': 'Georgia O\'Keefe was a famous painter of the:',
                'number':97,
                'round':2,
                'topic': 'Art',
                'Wwer': '16th Century',
                'Rwer': '20th Century',
                'pic': False,
                }),
            json.dumps({
                'question': 'Edward Hopper painted \"Nighthawks\" in:',
                'number':98,
                'round':2,
                'topic': 'Art',
                'Wwer': '1742',
                'Rwer': '1942',
                'pic': False,
                }),
            json.dumps({
                'question': '\"The Birth of Venus\" is a painting by:',
                'number':99,
                'round':2,
                'topic': 'Art',
                'Wwer': 'Leonardo da Vinci',
                'Rwer': 'Sandro Boticelli',
                'pic': False,
                }),
            json.dumps({
                'question': 'James Abbott Mcneil Whistler painted \"Whistler\'s Mother\" in:',
                'number':100,
                'round':2,
                'topic': 'Art',
                'Wwer': '1571',
                'Rwer': '1871',
                'pic': False,
                }),
            json.dumps({
                'question': 'This is a dummy question',
                'number':101,
                'round':2,
                'topic': 'dummy',
                'Wwer': 'dummy',
                'Rwer': 'dummy',
                'pic': False,
                })
        ]
        number_transmissions = len([i for i in self.infos() if i.contents not in ["Bad Luck", "Good Luck"]])
        if number_transmissions < len(questions):
            question = questions[number_transmissions]
        else:
            question = questions[-1]
        return question
