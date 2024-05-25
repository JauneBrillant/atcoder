use proconio::input;

fn main() {
    input! {
        n: usize,
        x: [usize; n],
    }

    for i in 0..n {
        if is_prime(x[i]) {
            println!("Yes");
        } else {
            println!("No");
        }
    }
}

fn is_prime(x: usize) -> bool {
    for i in 2.. {
        if i * i > x {
            break;
        }

        if x % i == 0 {
            return false;
        }
    }

    true
}
