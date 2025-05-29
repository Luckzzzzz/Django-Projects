# models.py
from django.db import models

class Player(models.Model):
    PLAYER_TYPES = (
        ('Goalkeeper', 'Goalkeeper'),
        ('FieldPlayer', 'FieldPlayer'),
    )

    name = models.CharField(max_length=50)
    id1 = models.IntegerField()
    count = models.IntegerField()
    player_type = models.CharField(max_length=20, choices=PLAYER_TYPES)
    total_stopping_shots = models.IntegerField(null=True, blank=True)
    goal_count = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.id1} ({self.name}) - {self.player_type}"

