class Ball(object):
    def __init__(self, super=None):
        self.ball_type = "super" if super else "regular"
