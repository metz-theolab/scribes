"""Represents a manuscript.
"""

from pydantic import BaseModel, Field


class Manuscript(BaseModel):
    """Represents a manuscript.
    """
    id_: str = Field(..., "The ID of the manuscript.")
    text_id: str = Field(..., "The ID of the text represented by the manuscript.")
    year: int = Field(None, "Datation of the manuscript.")
    width: int = Field(None, "Width of the manuscript.")
    height: int = Field(None, "Height of the manuscript.")
    comment: str = Field(..., "A generic comment field for this manuscript.")


class Text(BaseModel):
    """Represents a Text.
    """
    id_: str = Field(..., "The ID of the text.")
    name: str = Field(..., "The name of the text.")


class Chapter(BaseModel):
    """Represents a chapter of a Text.
    """
    id_: str = Field(..., "The ID of the chapter.")
    nbr: str = Field(..., "The number of the chapter.")


class Verse(BaseModel):
    """Represents a verse of a Chapter.
    """
    id_: str = Field(..., "The ID of the verse.")
    nbr: str = Field(..., "The number of the verse in a chapter.")
    chapter_id: str = Field(..., "The ID of the chapter the verse is from.")


class Collation(BaseModel):
    """Represents a Verse collation.
    """
    id_: str = Field(..., "The ID of the collation.")
    verse_id: str = Field(..., "The ID of the verse of the collation.")


class Reading(BaseModel):
    """Represents an instance of a reading within a collation.
    """
    id_: str = Field(..., "The ID of the word.")
    word: str = Field(..., "The content of the word.")


class Morphology(BaseModel):
    """The morphology of a word.
    """
    id_: str = Field(..., "The ID of the morphology.")
    word_id: str = Field(..., "The ID of the word.")
    lemma: str = Field(..., "The lemma of the word.")


class Meaning(BaseModel):
    """The definition of a word.
    """
    id_: str = Field(..., "The ID of the meaning.")
    lemma_id: str = Field(..., "The ID of the lemma.")
    meaning: str = Field(..., "The meaning of the word")


class Images(BaseModel):
    """An image representing a manuscript.
    """
    id_: str = Field(..., "An image representing a manuscript.")
    manuscript_id: str = Field(..., "The ID of the represented manuscript.")
    verse_start: int = Field(..., "The ID of the starting verse.")
    verse_end: int = Field(..., "The ID of the ending verse.")


class MarginalNote(BaseModel):
    """The marginal note."""
    id_: str = Field(..., "The ID of the marginal note.")
    manuscript_id: str = Field(..., "The ID of the manuscript with the marginal note.")
    content: str = Field(..., "The content of the marginal note.")
    verse: str = Field(..., "The ID of the verse next to the marginal note.")
