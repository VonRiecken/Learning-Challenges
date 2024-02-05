class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
        self.worth_it = True if self.draft - 1.5 * self.crew > 20 else False
        return self.worth_it
