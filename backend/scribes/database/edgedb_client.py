"""Python client for the EDGEDB database.
"""


from typing import Any, Dict


class EdgeDBClient:
    """Generic class for the manipulation of data stored in the EdgeDB database.
    """

    def __init__(self, db_host: str, db_port: int, db_name: str) -> None:
        """Initialize an object of class EdgeDBClient.

        Args:
            db_host (str): The host of the database.
            db_port (int): The port of the database.
            db_name (str): The name of the database.
        """
        self.client = None

    def insert_table(self, table_name: str, data: Dict[str, Any]):
        """Insert the data into the table table_name.

        Args:
            table_name (str): The name of the table to insert the data in.
            data (Dict[str, Any]): The data to insert.
        """

    def get_table(self, table_name: str) -> Dict[str, Any]:
        """Get the data in the table table_name"""

    def get_by_id(self, id_: str, table_name: str) -> Any:
        """Get the data with ID id in the table table_name.

        Args:
            id_ (str): The id to retrieve the data for.
            table_name (str): The name of the table the data is located in.

        Returns:
            Any: The corresponding data.
        """
