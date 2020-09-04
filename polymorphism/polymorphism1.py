class UP:
    def name(self):
        print("Uttar Pradesh")
    
    def population(self):
        print(2342525)

class MP:
    def name(self):
        print('Madhya Pradeshh')
    
    def population(self):
        print(342534)

up = UP()

mp = MP()

for state in (up, mp):
    state.name()
    state.population()
