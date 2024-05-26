use proconio::input;
use std::collections::BTreeMap;

fn main() {
    input! {
        q: usize,
    }

    let mut total_b = 0;
    let mut tr_map = BTreeMap::new();

    for _ in 0..q {
        input! {
            event: usize,
        }

        match event {
            1 => {
                input! {
                    mut x: i64,
                }
                x -= total_b;
                *tr_map.entry(x).or_insert(0) += 1
            }
            2 => {
                input! {
                    x: i64,
                }
                total_b += x;
            }
            3 => {
                if let Some((&k, &v)) = tr_map.iter().next() {
                    println!("{}", k + total_b);
                    if v == 1 {
                        tr_map.remove(&k);
                    } else {
                        *tr_map.entry(k).or_insert(0) -= 1;
                    }
                }
            }
            _ => (),
        }
    }
}
