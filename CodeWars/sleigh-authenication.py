class Sleigh(object):
    def authenticate(self, name, password):
        self.name = name
        self.password = password
        self.owner = 'Santa Claus'
        self.word = 'Ho Ho Ho!'
        self.open = True if self.name == self.owner and self.word == self.password else False
        return self.open
