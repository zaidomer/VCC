from random import choice
import random

agents = []
maps = []
guns = []
ranks = []
descriptive = []
verbs = []

class TitleGen():

    def __init__(self):
        self.agents = []
        self.maps = []
        self.guns = []
        self.ranks = []
        self.descriptive = []
        self.verbs = []

    def readText(self):
        with open("titleGeneratorTerms.txt",'r') as terms:
            count = 0
            for line in terms:
                if line[:-1] == '*':
                    count+=1
                elif count == 0:
                    self.agents.append(line[:-1])
                elif count == 1:
                    self.maps.append(line[:-1])
                elif count == 2:
                    self.guns.append(line[:-1])
                elif count == 3:
                    self.ranks.append(line[:-1])
                elif count == 4:
                    self.descriptive.append(line[:-1])
                else:
                    self.verbs.append(line[:-1])

    def fullRNG(self):
        self.readText()
        firstWord = choice([True, False])
        lastWord = choice([True, False])
        last = ''
        first = self.descriptive[random.randint(0, len(self.descriptive)-1)].capitalize()
        if firstWord:
            firstWord3 = random.randint(0, 3)
            if firstWord3 == 0:
                first = self.agents[random.randint(0, len(self.agents)-1)].capitalize()
            elif firstWord3 == 1:
                first = self.maps[random.randint(0, len(self.maps)-1)].capitalize()
            elif firstWord3 == 2:
                first = self.guns[random.randint(0, len(self.guns)-1)].capitalize()
            else:
                first = self.ranks[random.randint(0, len(self.ranks)-1)].capitalize()
        elif lastWord:
            lastWord3 = random.randint(0, 3)
            if lastWord3 == 0:
                last = 'w/' + self.agents[random.randint(0, len(self.agents)-1)].capitalize()
            elif lastWord3 == 1:
                last = 'in ' + self.maps[random.randint(0, len(self.maps)-1)].capitalize()
            elif lastWord3 == 2:
                last = 'w/' + self.guns[random.randint(0, len(self.guns)-1)].capitalize()
            else:
                last = 'in ' + self.ranks[random.randint(0, len(self.ranks)-1)].capitalize()

        verb = self.verbs[random.randint(0, len(self.verbs)-1)].capitalize()

        if (len(first.split())>=2) or (len(verb.split())>=2):
            last = ''

        return(f'{first} {verb} {last}')

    def twoWords(self,title):
        self.readText()
        des = ''
        des1 = ''
        ver = ''
        getFirst = False
        getdescriptive = False
        getVerb = False

        if not getFirst:
            for agent in self.agents:
                if agent.lower() in title.lower():
                    des = agent.capitalize()
                    des2 = 'w/' + agent.capitalize()
                    name = agent.capitalize()
                    getFirst = True
                    break

        if not getFirst:
            for rank in self.ranks:
                if rank.lower() in title.lower():
                    des = rank.capitalize()
                    des2 = 'in' + rank.capitalize()
                    name = rank.capitalize()
                    getFirst = True
                    break

        if not getFirst:
            for map in self.maps:
                if map.lower() in title.lower():
                    des = map.capitalize()
                    des2 = 'in' + map.capitalize()
                    getFirst = True
                    break

        if not getFirst:
            for gun in self.guns:
                if gun.lower() in title.lower():
                    des = gun.capitalize()
                    des2 = 'w/' + gun.capitalize()
                    name = gun.capitalize()
                    getFirst = True
                    break

        for desc in self.descriptive:
            if desc.lower() in title.lower():
                des1 = desc.capitalize()
                getdescriptive = True
                break

        for verb in self.verbs:
            if verb.lower() in title.lower():
                ver = verb.capitalize()
                getVerb = True
                break

        if [getFirst,getVerb,getdescriptive].count(True) > 1:
            if getFirst and getVerb:
                if choice([True, False]):
                    return(f'{des} {ver}')
                else:
                    return(f'{ver} {des2}')
            elif getdescriptive and getFirst:
                return(f'{des1} {name}')
            elif getVerb and getdescriptive:
                return(f'{des1} {verb}')
        else:
            return('_')

    def oneWord(self,title):
        self.readText()
        word = ''
        word2 = ''
        getFirst = False
        getdescriptive = False
        getVerb = False

        if not getFirst:
            for agent in self.agents:
                if agent.lower() in title.lower():
                    word = agent.capitalize()
                    word2 = 'w/' + agent.capitalize()
                    name1 = word
                    getFirst = True
                    break

        if not getFirst:
            for rank in self.ranks:
                if rank.lower() in title.lower():
                    word = rank.capitalize()
                    word2 = 'in' + rank.capitalize()
                    name1 = word
                    getFirst = True
                    break

        if not getFirst:
            for map in self.maps:
                if map.lower() in title.lower():
                    word = map.capitalize()
                    word2 = 'in' + map.capitalize()
                    getFirst = True
                    break

        if not getFirst:
            for gun in self.guns:
                if gun.lower() in title.lower():
                    word = gun.capitalize()
                    word2 = 'w/' + gun.capitalize()
                    name1 = word
                    getFirst = True
                    break

        if not getFirst:
            for desc in self.descriptive:
                if desc.lower() in title.lower():
                    word = desc.capitalize()
                    getdescriptive = True
                    break

        if not getdescriptive:
            for verb in self.verbs:
                if verb.lower() in title.lower():
                    word = verb.capitalize()
                    getVerb = True
                    break

        ver = self.verbs[random.randint(0, len(self.agents)-1)].capitalize()
        des1 = self.descriptive[random.randint(0, len(self.descriptive)-1)].capitalize()

        desc = random.randint(0, 3)
        if desc == 0:
            des = self.agents[random.randint(0, len(self.agents)-1)].capitalize()
            des2 = 'w/' + des
            name = des
        elif desc == 1:
            des = self.ranks[random.randint(0, len(self.ranks)-1)].capitalize()
            des2 = 'in ' + des
            name = des
        elif desc == 2:
            des = self.maps[random.randint(0, len(self.maps)-1)].capitalize()
            des2 = 'in ' + des
        else:
            des = self.guns[random.randint(0, len(self.guns)-1)].capitalize()
            des2 = 'w/' + des
            name = des


        if getFirst:
            rng = random.randint(0, 2)
            if rng == 0:
                return(f'{word} {ver}')
            elif rng == 1:
                return(f'{ver} {word2}')
            else:
                return(f'{des1} {name1}')
        elif getdescriptive:
            rng = random.randint(0, 1)
            if rng == 0:
                return(f'{word} {name}')
            elif rng == 1:
                return(f'{word} {ver}')
        elif getVerb:
            rng = random.randint(0, 2)
            if rng == 0:
                return(f'{des} {word}')
            elif rng == 1:
                return(f'{word} {des2}')
            else:
                return(f'{des1} {word}')
        else:
            return('_')

