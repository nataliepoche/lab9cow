class FileCow():
    def __init__(self, name, filename):
        self.name = name # initializes name

        try:
            file = open(filename) # checks for file
            self.image = file.read() # opens file to read

        except Exception: # if can't find file
            raise RuntimeError("MOO!!") # what is returned


    def set_image(self, image):
        raise RuntimeError("Cannot reset FileCow image")

    def get_image(self):
        return self.image