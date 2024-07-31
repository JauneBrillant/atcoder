use proconio::input;
use std::collections::HashMap;

fn main() {
    input! {
        n: usize,
        t: usize,
        ab: [(usize, usize); t],
    }

    let mut score_cnts = HashMap::new();
    score_cnts.insert(0, n);

    let mut points = vec![0; n + 1];
    for &(a, b) in ab.iter() {
        if score_cnts.contains_key(&points[a]) {
            score_cnts
                .entry(points[a])
                .and_modify(|e| *e -= 1)
                .or_insert(0);

            if let Some(&v) = score_cnts.get(&points[a]) {
                if v == 0 {
                    score_cnts.remove(&points[a]);
                }
            }
        }

        points[a] += b;
        *score_cnts.entry(points[a]).or_insert(0) += 1;

        println!("{}", score_cnts.len());
    }
}
