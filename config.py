
from dotenv import load_dotenv, find_dotenv

class LoadEnv():
    """Instantiate our environment variable file
    """

    def __init__(self) -> None:
        load_dotenv(find_dotenv())  # Loads our environment variable


initialize = LoadEnv()