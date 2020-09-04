#Polymorphism

#Duck typing

class Spyder:
    def execute(self):
        print('Compiling')
        print('Running')

class Sublime_Text:
    def execute(self):
        print('Spell check')
        print('Conventional check')
        print('Compiling ')
        print('Running')

class DuckTyping:
    def code_with(self,ide):
        ide.execute()



duck = DuckTyping()
duck.code_with(Spyder()) # duck with Spyder
duck.code_with(Sublime_Text()) # duck with Sublime Text

