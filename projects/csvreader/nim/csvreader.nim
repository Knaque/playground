import parsecsv, os, terminal, sequtils

proc getCmdFile: string =
  try: return paramStr(1)
  except IndexError: echo "You need to specify what file to open."; quit 0

var parser: CsvParser
parser.open(getCmdFile())
parser.readHeaderRow()

for (header, color) in zip(parser.headers, [fgRed, fgYellow, fgGreen, fgCyan, fgBlue, fgMagenta].cycle(int(parser.headers.len div 6 + 1))):
  stdout.setForegroundColor(color)
  stdout.write(header)
  for x in header.len()+1..20: stdout.write(' ')
stdout.write('\n')
stdout.setForegroundColor(fgDefault)

while parser.readRow():
  for i in parser.row:
    stdout.write(i)
    for x in i.len()+1..20: stdout.write(' ')
  stdout.write('\n')

parser.close()