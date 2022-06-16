"""CLI to fill up the database.
"""


class DatabaseFiller:
    """Class to fill up the database.
    """

    def __init__(self,
                 db_host: str,
                 db_port: int,
                 db_name: str,
                 data_folder: str) -> None:
        """Create an object of class database filler given the information of the database.
        """
        self.db_host = db_host
        self.db_port = db_port
        self.db_name = db_name
        self.data_folder = data_folder

    def from_json(self):
        """Load the data from json.
        """

    def from_tei(self):
        """Load the data from XML TEI.
        """
