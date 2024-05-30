use itertools::Itertools;
use proconio::input;
use std::collections::HashMap;
use std::collections::HashSet;

fn main() {
    input! {
        s1: String,
        s2: String,
        s3: String,
    }

    let unique_chars: HashSet<char> = s1.chars().chain(s2.chars()).chain(s3.chars()).collect();
    if unique_chars.len() > 10 {
        println!("No solution");
        return;
    }

    let digits = (0..10).collect::<Vec<u8>>();
    let permutations = digits.iter().permutations(unique_chars.len());

    for perm in permutations {
        let mut mapping = HashMap::new();
        for (i, &c) in unique_chars.iter().enumerate() {
            mapping.insert(c, perm[i]);
        }
    }

    println!("No solution");
}
