from subprocess import call
call(["pandoc", "-t", "odt", "InputReport.md", "-o", "OutputReport.docx"])
