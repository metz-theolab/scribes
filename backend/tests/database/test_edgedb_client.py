"""Unit tests from the edge db client class.
Tests only methods that 
"""

import unittest
from scribes.database.edgedb_client import EdgeDBClient
from utils.edgedb_test_container import EdgeDBContainer


class TestEdgeDBClient(unittest.TestCase):
    """Unit testing for the EdgeClient.
    """

    def test_build_query(self):
        """Tests that building a query works as expected.
        """
        test_table_name = "TestTable"
        test_data_model = {"name": "str", "firstname": "str"}

        expected_query = """INSERT TestTable {\n name := <str>$name,\nfirstname := <str>$firstname,\n}"""
        received_query = EdgeDBClient.build_insert_query(table_name=test_table_name,
                                        data_model=test_data_model)
        self.assertEqual(expected_query, received_query)



if __name__ == "__main__":
    unittest.main()

        