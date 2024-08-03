use proconio::input;

fn main() {
    input! {
        a: usize,
        b: usize,
        c: usize,
        d: usize,
    }

    for i in a..=b {
        if (c..=d).all(|j| !is_prime(i + j)) {
            println!("Takahashi");
            return;
        }
    }

    println!("Aoki");
}

fn is_prime(x: usize) -> bool {
    if x == 2 {
        return true;
    }

    for i in 2..x {
        if x % i == 0 {
            return false;
        }
    }

    true
}
