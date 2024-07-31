use proconio::input;

fn main() {
    input! {
        n: usize,
        q: usize,
        target_teeth_idx_arr: [usize; q],
    }

    let mut teeth_arr = vec![true; n];
    for i in target_teeth_idx_arr {
        teeth_arr[i - 1] = !teeth_arr[i - 1];
    }

    let res = teeth_arr.iter().filter(|e| **e == true).count();
    println!("{}", res);
}
