proc first_non_consecutive*(arr: seq[int]): seq[int] =
    var prev_num = arr[0]
    for n in arr[1..<arr.len]:
        if n != prev_num + 1: return @[n]
        prev_num = n
    return @[]