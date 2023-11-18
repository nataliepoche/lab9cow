class Dragon:
    def __init__(self, name, image):
        self.name = name  # set self.name to be name
        self.image = image  # set self.image to be None

    def get_name(self):
        return self.name # returns name

    def get_image(self):
        return self.image # retrieve attribute self.image

    def set_image(self, image):
        self.image = image # set self.image to be image, how you can update the attribute

    def can_breathe_fire(self):
        print("This dragon can breathe fire.") # prints message
        return True # returns attribute