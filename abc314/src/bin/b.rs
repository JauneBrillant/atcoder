use std::collections::HashMap;

use proconio::input;

fn main() {
    input! {
        n: usize,
        arrs: [[usize]; n],
        x: usize,
    }

    let mut map = HashMap::new();
    for i in 0..n {
        for j in 0..arrs[i].len() {
            if arrs[i][j] == x {
                map.insert(i + 1, arrs[i].len());
            }
        }
    }

    if map.is_empty() {
        println!("0");
        return;
    }

    let mut sorted_entries: Vec<_> = map.into_iter().collect();
    sorted_entries.sort_by(|(_, v1), (_, v2)| v1.cmp(&v2));

    let less_bet_cnt = sorted_entries[0].1;
    let mut res = sorted_entries.iter()
        .filter(|&(_, bet_cnt)| *bet_cnt == less_bet_cnt)
        .map(|&(p, _)| p)
        .collect::<Vec<usize>>();
    res.sort();

    println!("{}", res.len());
    for v in res {
        print!("{} ", v);
    }
}
