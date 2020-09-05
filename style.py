
def change_font():
    """Une méthode qui retourme le fichier HTML et CSS adéquat pour les fonts dans jupyter.
    """

    html = """
    <style>
    
    .rendered_html {
         font-size: 22px; 
         font-family: Garamond;
         line-height: 140%;
         text-align: justify;
         text-justify: inter-word;
    }

    div.text_cell_render h1 { /* Main titles bigger, centered */
        text-align:center;
    # }
    
    </style>"""

    return html