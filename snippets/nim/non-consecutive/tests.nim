import unittest, random, sequtils
import solution

randomize()

proc random_check*(arr: seq[int]): seq[int] =
    var prev_num = arr[0]
    for n in arr[1..<arr.len]:
        if n != prev_num + 1: return @[n]
        prev_num = n
    return @[]

suite "First Non-consecutive Number":
    test "Six":
        check first_non_consecutive(@[1,2,3,4,6,7,8]) == @[6]
    test "None":
        let expected: seq[int] = @[]
        check first_non_consecutive(@[1,2,3,4,5,6,7,8]) == expected
    test "Six":
        check first_non_consecutive(@[4,6,7,8,9,11]) == @[6]
    test "Eleven":
        check first_non_consecutive(@[4,5,6,7,8,9,11]) == @[11]
    test "None":
        let expected: seq[int] = @[]
        check first_non_consecutive(@[31,32]) == expected
    test "Zero":
        check first_non_consecutive(@[-3,-2,0,1]) == @[0]
    test "Negative one":
        check first_non_consecutive(@[-5,-4,-3,-1]) == @[-1]
    
    # Random tests
    test "Random":
        for x in 1..40:
            var arr = toSeq(rand(1..5)..rand(6..11))
            if rand(0..1) == 1: arr.delete(rand(0..<arr.len))
            check first_non_consecutive(arr) == random_check(arr)