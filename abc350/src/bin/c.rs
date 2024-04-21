use proconio::input;

fn main() {
    input! {
        n: usize,
        arr: [usize; n],
    }

    let mut arr = arr;
    let mut swap_history: Vec<(usize, usize)> = vec![];
    for i in 0..n {
        while arr[i] != i + 1 {
            let idx = arr[i] - 1;
            arr.swap(i, idx);
            swap_history.push((i + 1, idx + 1));
        }
    }

    println!("{}", swap_history.len());
    for tup in swap_history {
        println!("{} {}", tup.0, tup.1);
    }
}
