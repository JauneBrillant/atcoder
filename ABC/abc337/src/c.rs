use proconio::input;
use std::collections::HashMap;

fn main() {
    input! {
        n: usize,
        a: [i32; n],
    }

    let mut res: Vec<i32> = vec![0; n];
    let mut hashmap = HashMap::new();
    for (i, &v) in a.iter().enumerate() {
        hashmap.insert(v, (i + 1) as i32);
        if v == -1 {
            res[0] = (i + 1) as i32;
        }
    }

    for i in 1..n {
        res[i] = *hashmap.get(&res[i - 1]).unwrap();
    }

    for num in res {
        print!("{} ", num);
    }
}
