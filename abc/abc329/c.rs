use proconio::input;
use std::collections::HashMap;

fn main() {
    input! {
        _n: usize,
        s: String,
    }

    // ch_len -> ランレングス圧縮
    let mut ch_len: Vec<(char, usize)> = vec![];
    for c in s.chars() {
        if let Some(last_element) = ch_len.last_mut() {
            if last_element.0 == c {
                last_element.1 += 1;
            } else {
                ch_len.push((c, 1));
            }
        } else {
            ch_len.push((c, 1));
        }
    }

    let mut hashmap = HashMap::new();
    for (ch, len) in ch_len {
        if let Some(value) = hashmap.get_mut(&ch) {
            if *value < len {
                *value = len;
            }
        } else {
            hashmap.insert(ch, len);
        }
    }

    let res: usize = hashmap.values().map(|v| v).sum();
    println!("{}", res);
}
