use std::collections::HashMap;

use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        x: Chars,
        n: usize,
        mut s: [Chars; n],
    }

    let mut char_map = HashMap::new();
    for (i, &c) in x.iter().enumerate() {
        char_map.insert(c, i);
    }

    s.sort_by_key(|name| {
        name.iter()
            .map(|&c| char_map[&c])
            .collect::<Vec<_>>()
    });

    for name in s {
        println!("{}", name.iter().collect::<String>());
    }
}
