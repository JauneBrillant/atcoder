use proconio::input;
use itertools::Itertools;

fn main() {
    input! {
        n: String,
    }

    let permutations = n.chars().permutations(n.len());

    let mut ans = 0;
    for perm in permutations {
        let str = perm.iter().collect::<String>();
        for i in 1..n.len() {
            let (l, r) = str.split_at(i);
            let l: usize = l.parse().unwrap();
            let r: usize = r.parse().unwrap();
            ans = ans.max(l * r);
        }
    }

    println!("{}", ans);
}
