import sequtils, random
randomize()

for x in 1..5:
    echo toSeq(rand(1..5)..rand(6..11))