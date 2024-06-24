use proconio::input;

fn main() {
    input! {
        n: usize,
        m: usize,
        a: [usize; m],
    }

    let mut arr = vec![0; n + 1];
    let mut max_idx = 0;
    for ai in a.into_iter() {
        arr[ai] += 1;
        if arr[max_idx] < arr[ai] {
            max_idx = ai;
        }
        if arr[max_idx] == arr[ai] {
            max_idx = max_idx.min(ai);
        }
        println!("{}", max_idx);
    }
}
