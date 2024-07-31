use proconio::input;

fn main() {
    input! {
        n: usize,
        k: usize,
        a: usize,
    }

    let mut curr = a - 1;
    for _ in 0..k {
        curr += 1;
        if curr == n + 1 {
            curr = 1;
        }
    }

    println!("{}", curr);
}
