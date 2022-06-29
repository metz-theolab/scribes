type Text {
    required property name -> str;
}

type Manuscript {
    property comment -> str;
    required link text_id -> Text; 
}

