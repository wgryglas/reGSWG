----------------
Example Document
----------------
This is an example document to fill testable content.

Titles
------
Titles are underlined (or over and underlined) with a printing non alphanumeric
7-bit ASCII character. Recommended choices are "``= - ` : ' " ~ ^ _ * + # < >``".
The underline/overline must be at least as long as the title text.

A lone top-level (sub)section is lifted up to be the document's (sub)title.

Main document title thus would be a over + under lined first title in the document.
It is recommended to use over + under, while the rest of subtitles use only underline.

Remember - the underline(over as well) have to be at least the length of the title string
itself, it might be longer, but never shorter.


Paragraphs
----------
This is a paragraph.

Paragraphs line up at their left edges, and are normally separated by blank lines.
Multiple lines, not separated with extra empty line would be treated as single paragraph,
despite line breaks in source file.


Lists
-----
A text block which begins with a "*", "+", "-", "•", "‣", or "⁃",
followed by whitespace, is a bullet list item (a.k.a. "unordered"
list item). List item bodies must be left-aligned and indented relative
to the bullet; the text immediately after the bullet determines the indentation.
List:
  - one
  - two
  - three

Numbered list:
  1. First
  2. Second - saodmas adsojaso dasdasd a
     daosdj asd aoksd koas doksakod as
     mdoasdkopasopda opasdk pas
  3. Third

Auto enumerated list:
  #. First
  #. Second
  #. Third
  #. ASDsdadasd
  #. SAdada

Please, not that any list must be separated from previous text by the blank line. If the
list needs to use title (introductory statement) it can place directly in front of list,
without extra blank line. Blank line on the other hand must be placed after paragraph before
list (or list title).




Inline Elements
---------------
Inline elements are decoration(special treatment) for the part of the text inside paragraph.

The common elements are:
  - *emphasis*
  - **strong emphasis**
  - `interpreted text`
  - ``inline literal``
  - reference_
  - `phrase reference`_
  - anonymous__
  - _`inline internal target`
  - |substitution reference|
  - footnote reference [1]_
  - citation reference [CIT2002]_

