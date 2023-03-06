from src.repository.repository import Repository
from src.services.service import Service
from src.ui.gui import GameUI
from src.ui.ui import Console

if __name__ == '__main__':
    repository = Repository()
    service = Service(repository)

    # console = Console(service)
    # console.start_game()

    console = GameUI(service)
    console.start_game()
