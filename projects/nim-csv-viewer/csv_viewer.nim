# Import nigui and init
import nigui, parsecsv, os
app.init()

proc getCmdFile: string =
  try: return paramStr(1)
  except IndexError: echo "You need to specify what file to open."; quit 0

# Create window
var window = newWindow("CSV Viewer")
window.width = 600.scaleToDpi
window.height = 400.scaleToDpi

# Create containers
var container = newLayoutContainer(Layout_Horizontal)

# add container to window
window.add(container)

# create a sequence of TextAreas
var contents: seq[TextArea]

# create parset
var parser: CsvParser
parser.open(getCmdFile())

# read headers, create TextAreas and add the header names
parser.readHeaderRow()
for header in parser.headers: contents.add(newTextArea(header & '\n'))

# add TextAreas to container
for area in contents: container.add(area)

block:
  # add data to TextAreas
  var row = 1
  while parser.readRow():
    for n, i in parser.row: contents[n].addLine( $row & ") " & i)
    row += 1

parser.close()

# show window
window.show()

# run app
app.run()