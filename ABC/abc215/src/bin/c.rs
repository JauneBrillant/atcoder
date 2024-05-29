use proconio::input;
use itertools::Itertools;

fn main() {
    input! {
        s: String,
        k: usize,
    }

    let mut permutations = s.chars().sorted().permutations(s.len()).unique();

    if let Some(kth_permutation) = permutations.nth(k - 1) {
        let res: String = kth_permutation.into_iter().collect();
        println!("{}", res);
    }
}
