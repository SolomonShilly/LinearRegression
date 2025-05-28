class FileHandler:
    def __init__(self):
        self.filePath = input('Enter path to file: ')
        self.data = None

    def open_file(self):
        try:
            with open(self.filePath, 'r') as file:
                self.data = file.read()
            print(f'{self.filePath} opened successfully')
            return self.data
        except FileNotFoundError:
            print(f'{self.filePath} was not found')
            return None
        except Exception as e:
            print(f'{e}: Error loading file')
