use proconio::input;
use std::{cmp::Reverse, collections::BinaryHeap};

fn main() {
    input! {
        q: usize,
    }

    let mut total_b = 0;
    let mut heap = BinaryHeap::new();

    for _ in 0..q {
        input! {
            event: usize,
        }

        match event {
            1 => {
                input! {
                    mut x: i64,
                }
                heap.push(Reverse(x - total_b))
            }
            2 => {
                input! {
                    x: i64,
                }
                total_b += x;
            }
            3 => {
                if let Some(Reverse(e)) = heap.pop() {
                    println!("{:?}", e + total_b);
                }
            }
            _ => (),
        }
    }
}
