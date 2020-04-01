import strutils, tables, algorithm

const alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

proc nthRank*(st: string, we: seq[int], n: int): string =
    var
        o = newOrderedTable[int, string]()
        d: seq[int]

        name_buffer = ""
        rank_buffer, length_buffer, weight_buffer = 0

    for i, c in st:
        if c.toLowerAscii() in alphabet:
            length_buffer += 1
            rank_buffer += find(alphabet, c.toLowerAscii()) + 1
            name_buffer = name_buffer & $c
            if i == st.len-1:
                o[rank_buffer*we[weight_buffer]] = name_buffer
                d.add(rank_buffer*we[weight_buffer])
        else:
            o[rank_buffer*we[weight_buffer]] = name_buffer
            d.add(rank_buffer*we[weight_buffer])
            name_buffer = ""
            rank_buffer = 0
            length_buffer = 0
            weight_buffer += 1
    o.sort(system.cmp, order = SortOrder.Descending)
    d.sort(order = SortOrder.Descending)
    return o[d[n-1]]

echo nthRank("Elijah,Chloe,Elizabeth,Matthew,Natalie,Jayden", @[1, 3, 5, 5, 3, 6], 2)