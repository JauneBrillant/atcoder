use proconio::input;
use std::collections::HashMap;

fn main() {
    input! {
        s: String,
    }

    let mut hashmap = HashMap::new();
    for c in s.chars() {
        *hashmap.entry(c).or_insert(0) += 1;
    }

    let mut target = None;
    for (k, v) in &hashmap {
        if *v == 1 {
            target = Some(*k);
            break;
        }
    }


    let res = s.find(target.unwrap());
    println!("{}", res.unwrap() + 1);
}
