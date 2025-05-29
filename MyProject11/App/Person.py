# Person.py

class Person:
    def __init__(self, name, id1, count):
        self.name = name
        self.id1 = id1
        self.count = count

    def __str__(self):
        return f"Name: {self.name}, ID: {self.id1}, Matches Played: {self.count}"

class GoalKeeper(Person):
    def __init__(self, name, id1, count, stopping_shots):
        super().__init__(name, id1, count) 
        self.stopping_shots = stopping_shots
        self.stop_rate = self.stopping_shots / self.count if self.count > 0 else 0

    def __str__(self):
        return f"{super().__str__()}, Stopping Shots: {self.stopping_shots}, Stop Rate: {self.stop_rate:.2f}"

class FieldPlayer(Person):
    def __init__(self, name, id1, count, goal_count):
        super().__init__(name, id1, count)  
        self.goal_count = goal_count

    def __str__(self):
        return f"{super().__str__()}, Goals Scored: {self.goal_count}"
