import random

class Hero:
    def init(self, number, team, name):
        self.team = team
        self.number = number
        self.name = name
    def level_up(self):
        print(f"Hero {self.name} поднял уровегь!")

class squad:
    def init(self, number, team):
        self.team = team
        self.number = number
    def follow_hero(self, hero):
        print(f"squad{self.number} следует за героем")

hero1 = Hero(1, "команда А", "Герой1")
hero2 = Hero(2, "команда В", "Герой2")

squad_команда_А = []
squad_команда_В = []

for i in range(100):
    team = random.choice(["команда А", "команда В"])
    squad_obj = squad(i + 1, team)
    if team == "команда А":
        squad_команда_А.append(squad_obj)
    else:
        squad_команда_В.append(squad_obj)

print("Количество солдат в команде А:", len(squad_команда_А))
print("Количество солдат в команде В:", len(squad_команда_В))

if len(squad_команда_А) > len(squad_команда_В):
    hero1.level_up()
else:
    hero2.level_up()

hero1.squad_to_follow = squad_команда_А[0]
hero1.squad_to_follow.follow_hero(hero1) 

