use proconio::input;

fn main() {
    input! {
        n: usize,
    }

    let mut k = 0;
    while (1 << k) <= n { k+= 1 }

    println!("{}", k - 1);
}
