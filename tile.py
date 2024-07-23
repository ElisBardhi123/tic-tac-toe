
class Tile:

    def __init__(self, content) -> None:
        self.content = content
    
    def __str__(self) -> str:
        if self.content == 'X' or self.content == 'O': 
            return str(self.content)
        else:
            return str(f'[{self.content}]')
    
    def setContent(self, content):
        self.content = content 