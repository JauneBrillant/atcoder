use proconio::input;
use std::collections::HashMap;

fn main() {
    input! {
        s: String,
    }

    let mut freq_ch: HashMap<char, usize> = HashMap::new();
    for c in s.chars() {
        *freq_ch.entry(c).or_insert(0) += 1;
    }

    // (key, value) = (文字の出現回数, 文字の出現回数の個数)
    let mut freq_cnt = HashMap::new();
    for value in freq_ch.values() {
        *freq_cnt.entry(value).or_insert(0) += 1;
    }

    let flag = freq_cnt.values().all(|&cnt| cnt == 0 || cnt == 2);

    println!("{}", if flag { "Yes" } else { "No" });
}
