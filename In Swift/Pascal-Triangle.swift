import Foundation

func fact(_ n: Int) -> Int {
    return (1...max(n,1)).reduce(1, *)
}

func ncr(_ n: Int, _ r: Int) -> Int {
    return fact(n) / (fact(r) * fact(n - r))
}

print("Enter number of rows: ", terminator: "")
if let input = readLine(), let n = Int(input) {
    for i in 0..<n {
        print(String(repeating: " ", count: n - i), terminator: "")
        for j in 0...i {
            print("\(ncr(i, j)) ", terminator: "")
        }
        print()
    }
}
