use proconio::input;
use std::collections::HashSet;

fn main() {
    input! {
        x1: i32,
        y1: i32,
        x2: i32,
        y2: i32,
    }

    let mut st1 = HashSet::new();
    st1.insert((x1 + 1, y1 + 2));
    st1.insert((x1 + 2, y1 + 1));
    st1.insert((x1 + 2, y1 - 1));
    st1.insert((x1 + 1, y1 - 2));
    st1.insert((x1 - 1, y1 - 2));
    st1.insert((x1 - 2, y1 - 1));
    st1.insert((x1 - 2, y1 + 1));
    st1.insert((x1 - 1, y1 + 2));

    let mut st2 = HashSet::new();
    st2.insert((x2 + 1, y2 + 2));
    st2.insert((x2 + 2, y2 + 1));
    st2.insert((x2 + 2, y2 - 1));
    st2.insert((x2 + 1, y2 - 2));
    st2.insert((x2 - 1, y2 - 2));
    st2.insert((x2 - 2, y2 - 1));
    st2.insert((x2 - 2, y2 + 1));
    st2.insert((x2 - 1, y2 + 2));

    for (a, b) in st1.iter() {
        for (c, d) in st2.iter() {
            if (a, b) == (c, d) {
                println!("Yes");
                return;
            }
        }
    }
    println!("No");
}
