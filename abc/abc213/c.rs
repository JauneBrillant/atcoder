use proconio::input;
use std::collections::{BTreeSet, HashMap};

fn main() {
    input! {
        _h: usize,
        _w: usize,
        n: usize,
        ab: [(usize, usize); n],
    }

    let rows: BTreeSet<_> = ab.iter().map(|&(a, _)| a).collect();
    let cols: BTreeSet<_> = ab.iter().map(|&(_, b)| b).collect();

    let rows_map: HashMap<_, _> = rows.iter().enumerate().map(|(i, &r)| (r, i + 1)).collect();
    let cols_map: HashMap<_, _> = cols.iter().enumerate().map(|(i, &c)| (c, i + 1)).collect();

    for (a, b) in &ab {
        println!("{} {}", rows_map[a], cols_map[b]);
    }
}
