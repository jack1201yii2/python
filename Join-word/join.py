from docxcompose.composer import Composer
from docx import Document 

doc1 = Document("16841902 Diseño de imagen corporativa GNX.docx")
composer = Composer(doc1)
doc2 = Document("16841903 Zonificación y desarrollo del espacio turistico.docx")
composer.append(doc2)

composer.save("full.docx")
