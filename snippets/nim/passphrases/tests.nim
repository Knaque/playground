import strutils, unittest, passphrases

proc dotest(s: string, n: int, exp: string) =
    echo "s ", s
    echo "n ", n
    let actual = playPass(s, n)
    echo "Exp: $1\ngot: $2".format(exp, actual)
    echo actual == exp
    check(actual == exp)
    echo "-"

suite "playPass":
  test "fixed tests":
    dotest("I LOVE YOU!!!", 1, "!!!vPz fWpM J")
    dotest("I LOVE YOU!!!", 0, "!!!uOy eVoL I")
    dotest("AAABBCCY", 1, "zDdCcBbB")