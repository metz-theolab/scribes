"""Specific client for the SCRIBES project.
"""

from this import s
from typing import List
from scribes.database.edgedb_client import EdgeDBClient


class ScribesClient(EdgeDBClient):
    """Client for the EdgeDB database of the SCRIBE project.
    """

    # DATA GETTERS
    def get_full_text(self, manuscript_id: str) -> str:
        """Return the full text of a given manuscript.

        Args:
            manuscript_id (str): The ID of the manuscript to get in the database.

        Returns:
            str: The full text associated with the manuscript.
        """

    def get_verse(self, verse_nbr: int, chapter_nbr: int, manuscript_id: str) -> str:
        """Return the content of a verse for a given chapter and a given manuscript.

        Args:
            verse_nbr (int): The number of the verse.
            chapter_nbr (int): The number of the chapter.
            manuscript_id (str): The ID of the manuscript.

        Returns:
            str: The corresponding verse.
        """

    def get_marginal_note(self):  # FIXME: marginal notes ??
        """Retrieve the marginal note.
        """
        pass

    def get_image(self, verse_start: str, verse_end: str):
        """Retrieve the image corresponding to the start of a verse and the end of a verse.

        Args:
            verse_start (str): The first verse represented by the image.
            verse_end (str): The last verse represented by the image.
        """

    # DATA INSERTERS
    def add_manuscript(self, manuscript_id: str, text_id: str):
        """Add a manuscript with id manuscript_id, corresponding to text
        text_id.

        Args:
            manuscript_id (str): The ID of the manuscript to insert.
            text_id (str): The ID of the text represented by the manuscript.
        """

    def add_collation(self, verse_id: str, readings: List[str]):
        """Add a collation to the database corresponding to a verse.
        """

    def append_to_collation(self, collation_id: str, reading: str):
        """Add a new reading to a collation.

        Args:
            collation_id (str): The ID of the collation to insert some data for.
            reading (str): The reading of the verse to append to the collation.
        """
