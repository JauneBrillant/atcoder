use proconio::input;
use std::collections::HashMap;

fn main() {
    input! {
        s: String,
    }

    let mut hashmap: HashMap<char, usize> = HashMap::new();
    for c in s.chars() {
        *hashmap.entry(c).or_insert(0) += 1;
    }

    let mut sorted_keys: Vec<char> = hashmap.keys().copied().collect();
    sorted_keys.sort();

    let mut max_val = 0;
    let mut max_key = '\0';
    for key in sorted_keys {
        let val = hashmap.get(&key).unwrap();
        if max_val < *val {
            max_val = *val;
            max_key = key;
        }
    }

    println!("{}", max_key);
}
