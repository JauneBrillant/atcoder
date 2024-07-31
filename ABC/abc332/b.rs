use proconio::input;

fn main() {
    input! {
        mut k: usize,
        g: i32,
        m: i32,
    }

    let mut glass = 0;
    let mut cup = 0;
    while k > 0 {
        match (glass == g, cup == 0) {
            (true, _) => glass = 0,
            (_, true) => cup = m,
            _ => {
                let glass_capacity = g - glass;
                if glass_capacity >= cup {
                    glass += cup;
                    cup = 0;
                } else {
                    glass += glass_capacity;
                    cup -= glass_capacity;
                }
            }
        }
        k -= 1;
    }

    println!("{} {}", glass, cup);
}
