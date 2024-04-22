import random

class Riddle:
    def __init__(self):
        the_riddle_number = random.randint(1,11)
        match the_riddle_number:
            case 1:
                self.damage = 40
                self.time_to_solve = 10
                self.riddle = "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?"
                self.posible_answers = ["Echo","Whisper","Music","Sound"]
                self.answer = 1 
            case 2:
                self.damage = 30
                self.time_to_solve = 7
                self.riddle = "What belongs to you, but other people use it more than you?"
                self.posible_answers = ["Your name","Your house","Your car","Your phone"]
                self.answer = 1 
            case 3:
                self.damage = 50
                self.time_to_solve = 12
                self.riddle = "I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by almost every person. What am I?"
                self.posible_answers = ["Gold","Diamond","Coal","charcoal"]
                self.answer = 4 
            case 4:
                self.damage = 50
                self.time_to_solve = 12
                self.riddle = "I am deeper then every building that you can build, i can be as hight as the clouds. You cant move me but you can damage me"
                self.posible_answers = ["Tree","The sea","Light","Mounten"]
                self.answer = 4  
            case 5:
                self.damage = 70
                self.time_to_solve = 14
                self.riddle = "What has a head and a tail, but no body?"
                self.posible_answers = ["Coin","Snake","Hammer","Frog"]
                self.answer = 1  
            case 6:
                self.damage = 45
                self.time_to_solve = 9
                self.riddle = "I am not alive, but I can grow. I don't have lungs, but I need air. What am I?"
                self.posible_answers = ["Fire","Water","Plant","Cloud"]
                self.answer = 1
            case 7:
                self.damage = 55
                self.time_to_solve = 11
                self.riddle = "I can be cracked, made, told, and played. What am I?"
                self.posible_answers = ["Egg","Joke","Code","Piano"]
                self.answer = 2
            case 8:
                self.damage = 60
                self.time_to_solve = 10
                self.riddle = "If you could save only one who would it be?"
                self.posible_answers = ["Mother","Sister","Brother","father"]
                self.answer = 0
            case 9:
                self.damage = 65
                self.time_to_solve = 13
                self.riddle = "The more you take, the more you leave behind. What am I?"
                self.posible_answers = ["Footsteps","Breath","Memory","Age"]
                self.answer = 1
            case 10:
                self.damage = 40
                self.time_to_solve = 10
                self.riddle = "I will die with you, i was born with you. You can hurt me only if you hurt your self but you can never touch me. Who am i?"
                self.posible_answers = ["my shadow","my self","my reflection","my name"]
                self.answer = 3 
            case 11:
                self.damage = 30
                self.time_to_solve = 7
                self.riddle = "You can kill me by calling me by name, who am i?"
                self.posible_answers = ["air","silence","echo","death"]
                self.answer = 2 
            case _:
                self.damage = 0
                self.time_to_solve = 15
                self.riddle = "No riddle available."
                self.posible_answers = []
                self.answer = None
    
    def display_riddle(self):
        print(self.riddle)
        for i in range(len(self.posible_answers)):
            print(str(i + 1) + "." + self.posible_answers[i])
        print(f"you have {self.time_to_solve} seconds to answer, What is your answer:")
    
    def get_riddle_text(self):
        the_riddle = self.riddle + "\n"
        for i in range(len(self.posible_answers)):
            the_riddle += str(i + 1) + "." + self.posible_answers[i] + "\n"
        return 

    def get_riddel(self):
        return self.riddle

    def get_possible_answers(self):
        return self.posible_answers

    def get_answer(self):
        return self.answer
    
    def get_damage(self):
        return self.damage
    
    def get_time_to_solve(self):
        return self.time_to_solve
    
