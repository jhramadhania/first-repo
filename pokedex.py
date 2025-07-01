class Pokemon:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught

    def speak(self):
        print(self.name + ' ' + self.name)
    
    def display_details(self):
        print('Entry number: ' + str(self.entry))
        print('Name: ' + self.name)
        print('Type: ' + self.types)
        print('Description: ' + self.description)
        if self.is_caught == True:
            print(self.name + ' has already been caught!')

pikachu = Pokemon(33, 'Pikachu', 'Electric', "Pikachu has yellow color", True)

pikachu.speak()

pikachu.display_details()