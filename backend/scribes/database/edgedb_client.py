"""Python client for the EDGEDB database.
"""

from typing import Any, Dict
import edgedb

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
        self.client = edgedb.create_client(host=db_host, port=db_port, database=db_name)

    @staticmethod
    def build_insert_query(table_name: str, data_model: Dict[str, str]):
        """Given an operation, a table name, a data model and a dataset, build the corresponding
        query to manipulate the data.

        Args:
            table_name (str): The name of the table to manipulate the data from.
            data_model (Dict[str, str]): The data model to manipulate the data with.
        """
        query = f"INSERT {table_name} " + "{\n "
        # Create query by iterating over datatype
        for field_name, field_type in data_model.items():
            query += f"{field_name} := <{field_type}>${field_name},\n"
        # Close query
        query += "}"
        return query

    def insert_table(self, table_name: str, data_model: Dict[str, str], data: Dict[str, Any]):
        """Insert the data into the table table_name.

        Args:
            table_name (str): The name of the table to insert the data in.
            data_model (str): The data model for the table.
            data (Dict[str, Any]): The data  to insert.
        """
        # Demo query to insert manuscript
        """INSERT Text {
                name:= <str>$toto
        }
        """
        # Build query
        self.build_insert_query(table_name=table_name, data_model=data_model)
        # 


    def get_table(self, table_name: str) -> Dict[str, Any]:
        """Get all the data in the table table_name."""

    def get_by_id(self, id_: str, table_name: str) -> Any:
        """Get the data with ID id in the table table_name.

        Args:
            id_(str): The id to retrieve the data for.
            table_name(str): The name of the table the data is located in .

        Returns:
            Any: The corresponding data.
        """
