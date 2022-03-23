class MainMemory:
    def __init__(self):
        self.clean()
        self.loaded_memory = []

    def load(self, value):
        self.loaded_memory.append(value)

    def get(self, index):
      if  0 > index >= len(self.loaded_memory) or (not isinstance(index, int)):
        return 0

      content = self.loaded_memory[index]

      return int(content) 

    def clean(self):
        self.loaded_memory = []

