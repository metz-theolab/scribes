"""Represents a manuscript.
"""

from enum import Enum

from pydantic import BaseModel, Field

# Je suis vraiment pas sûr de ce code pour le champ Enum :-)
class LanguageEnum (str, Enum):
    hebrew = 'Hebrew'
    greek = 'Greek'
    aramaic = 'Aramaic'
    syriac = 'Syriac'
    samaritan = 'Samaritan'
    samaritan_aramaic = 'Samaritan Aramaic'
    latin = 'Latin'


class Manuscript(BaseModel):
    """Represents a manuscript.
    """
    id_: str = Field(..., "The ID of the manuscript.")
    name: str = Field(..., "The ID of the text represented by the manuscript. Ex. 'MS A' or '4Q418'")
 
    #Identification of the ms
    library: str = Field (None, "The library of preservation.")
    shelfmark: str = Field(None, "The shelfmark of the manuscript in the Library where it is preserved.")
    
    #Description of the ms   
    origin: str = Field (None, "place of discovery")    
    material: str = Field (None, "Scroll Leather, Parchment, Paper, Papyrus, etc.") #On devrait pouvoir mettre un enum ici
    language: LanguageEnum = Field (None, "Hebrew, Greek, Aramaic, Syriac, Samaritan, Samaritan Aramaic, Latin.")
    year: int = Field(None, "Datation of the manuscript.")
    script_type: str = Field (None, "Describe the type of script: formal, semi-formal, cursive, semi-cursive, oriental, etc..")
    ink: str = Field (None, "ink description")
    comment: str = Field(..., "A generic comment field for this manuscript.")

    quire_composition: str = Field (None, "Description of the quire composition (ex. number of bifolios, number of quires and quires composition, etc.).")
    vocalization: Enum = Field ("True, False, Sporadic")
    justified_lines: boolean = Field (None, "If lines are justified or not")
    ruling: boolean = Field (None, "If the manuscript is ruled")
    illumination: boolean = Field (None, "If the ms contain illuminations")
    colophon: str = Field (None, "Report here the colophon in original language and translation")

    #Size description
    width: int = Field(None, "Width of the manuscript.")
    height: int = Field(None, "Height of the manuscript.")
    upper_margin: int = Field(None, "Upper margin in mm")
    lower_margin: int = Field(None, "Lower margin in mm")
    inner_margin: int = Field(None, "Inner margin in mm")
    outer_margin: int = Field(None, "Outer margin in mm")
    text_height: int = Field (None, "text_height in mm")
    text_width: int = Field(None, "text width in mm")
    line_nbr: int = Field (None, "Number of line per page or column")
    interline: float = Field (None, "Distance between two lines")
    interline_10: float = Field (None, "Distance bewteen ten lines")


class Text(BaseModel):
    """Represents a Text.
    """
    id_: str = Field(..., "The ID of the text.")
    name: str = Field(..., "The name of the text. Ex. 'Ben Sira' ou 'Hodayot'")
    manuscript_id: str = Field(..., "List of the manuscripts associated to the text.") #But here we need a list of value, not just one value...

class Folio(BaseModel): #Or Fol_frg
    """Represent a folio OR a fragment OR for reconstructed scoll the column of the scroll."""
    id_: str = Field(..., "The ID of the folio.")
    nbr: int = Field(..., "The number of the folio")
    manuscript_id: str = Field(..., "The id of the text the folio is from")

class Column(BaseModel):
    """Represent the column on a folio, a fragment. If it is no column then nbr = 0"""
    id_: str = Field(..., "The ID of the column.")
    nbr: int = Field(..., "The number of the line")
    folio_id: str = Field(..., "the ID of the folio the line is from.")

class Line(BaseModel):
    id_: str = Field(..., "The ID of the line.")
    nbr: int = Field(..., "The number of the line")
    column_id: str = Field(..., "The ID of the folio the line is from.")
    word_start_id: str = Field(..., "The ID of the word that starts the line")
    word_stop_id: str = Field(..., "The ID of the word that ends the line")


class Chapter(BaseModel):
    """Represents a chapter of a Text.
    """
    id_: str = Field(..., "The ID of the chapter.")
    nbr: int = Field(..., "The number of the chapter.")
    text_id: str = Field(..., "the id of the text the chapter is from")


class Verse(BaseModel):
    """Represents a verse of a Chapter.
    """
    id_: str = Field(..., "The ID of the verse.")
    nbr: int = Field(..., "The number of the verse in a chapter.")
    chapter_id: str = Field(..., "The ID of the chapter the verse is from.")

class SyntaxicUnit(BaseModel):
    """Represents a syntaxic unity"""
    id_: str = Field(..., "The ID of the sentence")
    word_id: str = Field(..., "The id of the words of the sentence")
    #Pour collation et reading je ne sais pas trop comment tu vois les choses

class Reading(BaseModel):
    """Represents an instance of a reading within a collation.
    """
    id_: str = Field(..., "The ID of the word.")
    word: str = Field(..., "The content of the word.")
    #preceding_word: str = Field(..., "Pointe vers l'id_ du mot word précédent")
    manuscript_id: str = Field(..., "the manuscript where the word is from")
    folio_id: str = Field(..., "the folio where the word is from")
    column_id: str = Field(..., "the column where the word is from")
    line_id: str = Field(..., "the line where the word is from")
    chapter_id: str = Field(..., "The ID of the chapter of the collation.")
    verse_id: str = Field(..., "The ID of the verse of the collation.")

class MarginalNote(BaseModel):
    """The marginal note."""
    id_: str = Field(..., "The ID of the marginal note.")
    manuscript_id: str = Field(..., "The ID of the manuscript with the marginal note.")
    content: str = Field(..., "The content of the marginal note.")
    verse: str = Field(..., "The ID of the verse next to the marginal note.")



class Morphology(BaseModel):
    """The morphology of a word.
    """
    id_: str = Field(..., "The ID of the morphology.")
    word_id: str = Field(..., "The ID of the word.")
    lemma: str = Field(..., "The lemma of the word.")
    morph_analysis: str = Field(..., "The morphanalysis of the word.")
    #En fait on pourrait mettre juste un str ou subdiviser en plein de champs (verb, noun, binyanim, person, gender, number, suffixe, etc.)#
    #ça dépend un peu d'où et comment on reprend les données de dicta

 

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
    folio_id: str = Field(..., "The ID of the folio or the fragment of the manuscript")
    verse_start_ch: int = Field(..., "The ID of the starting verse.")
    verse_start_vs: int = Field(..., "The ID of the starting verse.")
    verse_end_ch: int = Field(..., "The ID of the ending verse.")
    verse_end_vs: int = Field(..., "The ID of the ending verse.")
    """
    JS : Je pense qu'on devrait vraiment faire qq part une classe d'objet x:y ou x et y sont des int représentant
    respectivement chapitre et verset et que l'on puisse trier, etc. voire même qui interprète correctement des encodages du type "2:2-4;3,4-5"
    """

class NotesOnReading(BaseModel):
    """The notes on reading in markdown
    """
    id_: str = Field(..., "The ID of the note on reading")
    word_id: str = Field(..., "The ID of the word or group of words the note on reading is related to")
    note: str = Field(..., "The note on the reading")

class NotesOnTranslation(BaseModel):
    """The notes on translation in markdown
    """
    id_: str = Field(..., "The ID of the note on translation")
    word_id: str = Field(..., "The ID of the word or group of words the note on translation is related to")
    note: str = Field(..., "The note on the translation")


