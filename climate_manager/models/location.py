class Location:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.history = []
    
    def add_history(self, history):
        self.history.append(history)
