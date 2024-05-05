use proconio::input;

fn main() {
    input! {
        s: usize,
        t: usize,
        x: usize,
    }

    let mut times = vec![false; 24];
    if s < t {
        (s..t).for_each(|h| times[h] = true);
    } else {
        (s..24).for_each(|h| times[h] = true);
        (0..t).for_each(|h| times[h] = true);
    }

    println!("{}", if times[x] { "Yes" } else { "No" });
}
