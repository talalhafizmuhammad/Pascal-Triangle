fun fact(n: Int): Int {
    var f = 1
    for (i in 1..n) f *= i
    return f
}

fun ncr(n: Int, r: Int): Int {
    return fact(n) / (fact(r) * fact(n - r))
}

fun main() {
    print("Enter number of rows: ")
    val n = readln().toInt()

    for (i in 0 until n) {
        print(" ".repeat(n - i))
        for (j in 0..i) {
            print("${ncr(i, j)} ")
        }
        println()
    }
}
