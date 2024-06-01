use itertools::Itertools;
use proconio::input;

fn main() {
    input! {
        n: usize,
        p: usize,
        q: usize,
        a: [usize; n],
    }

    let mut ans = 0;
    for perm in a.iter().combinations(5) {
        let res = perm.iter().fold(1, |acc, &num| acc * num % p);
        if res % p == q {
            ans += 1;
        }
    }

    println!("{}", ans);
}
