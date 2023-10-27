class EntityComponent:
    def __init__(self):
        self.components = {}

    def add_component(self, component):
        self.components[type(component)] = component