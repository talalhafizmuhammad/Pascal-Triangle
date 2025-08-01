package main

import (
	"fmt"
)

func fact(n int) int {
	f := 1
	for i := 1; i <= n; i++ {
		f *= i
	}
	return f
}

func ncr(n, r int) int {
	return fact(n) / (fact(r) * fact(n - r))
}

func main() {
	var n int
	fmt.Print("Enter number of rows: ")
	fmt.Scan(&n)

	for i := 0; i < n; i++ {
		for j := 0; j < n - i; j++ {
			fmt.Print(" ")
		}
		for j := 0; j <= i; j++ {
			fmt.Printf("%d ", ncr(i, j))
		}
		fmt.Println()
	}
}
