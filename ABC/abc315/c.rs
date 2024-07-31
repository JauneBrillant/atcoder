use proconio::input;
use std::collections::HashMap;

fn main() {
    input! {
        n: usize,
        fs: [(usize, usize); n],
    }

    let mut map = HashMap::new();
    for (f, s) in fs.iter() {
        map.entry(f).or_insert(vec![]).push(s);
    }

    let same = map.values()
        .map(|arr| {
            if arr.len() < 2 {
                0
            } else {
                let mut arr = arr.clone();
                arr.sort_by(|a, b| b.cmp(&a));
                arr[0] + (arr[1] / 2)
            }
        })
        .max()
        .unwrap();

    let mut maxs = map.iter()
        .map(|(_, arr)| arr.iter().max().unwrap())
        .collect::<Vec<_>>();
    maxs.sort_by(|a, b| b.cmp(&a));

    let mut diff = 0;
    if maxs.len() < 2 {

    } else {
        diff = **maxs[0] + **maxs[1];
    }

    println!("{}", same.max(diff));
}
