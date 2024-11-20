class Tekken8Mains:
  def __init__( self, name, rank, playtime, wins, losses):
    self.rank = rank
    self.playtime = playtime
    self.name = name
    self.wins = wins
    self.losses = losses
  def winloss(self):
     return self.wins / self.losses
  
Zafina = Tekken8Mains('Zafina', 'Mighty Ruler', 14, 250, 70)
Asuka = Tekken8Mains('Asuka', 'Garyu', 6, 124, 53)
Azucena = Tekken8Mains('Azucena', 'Warrior', 4, 54, 19)

print(f"Win/loss ratio: {Azucena.winloss()}")