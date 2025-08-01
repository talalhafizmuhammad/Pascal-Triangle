use std::io;

fn fact(n: u32) -> u32 {
    (1..=n).product()
}

fn ncr(n: u32, r: u32) -> u32 {
    fact(n) / (fact(r) * fact(n - r))
}

fn main() {
    println!("Enter number of rows: ");
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let n: u32 = input.trim().parse().unwrap();

    for i in 0..n {
        print!("{}", " ".repeat((n - i) as usize));
        for j in 0..=i {
            print!("{} ", ncr(i, j));
        }
        println!();
    }
}
