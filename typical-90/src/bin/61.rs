use proconio::input;
use std::collections::VecDeque;

fn main() {
    input! {
        q: usize,
        tx: [(usize, usize); q],
    }

    let mut deque = VecDeque::new();
    let mut res = vec![];
    for (t, x) in tx.into_iter() {
        match t {
            1 => deque.push_front(x),
            2 => deque.push_back(x),
            3 => {
                if let Some(&v) = deque.iter().nth(x - 1) {
                    res.push(v);
                }
            }
            _ => (),
        }
    }

    for e in res {
        println!("{}", e);
    }
}
