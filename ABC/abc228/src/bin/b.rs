use proconio::input;

fn main() {
    input! {
        n: usize,
        x: usize,
        a: [usize; n],
    }

    let mut memo = vec![false; n];
    let mut tar = x - 1;
    while memo[tar] == false {
        memo[tar] = true;
        tar = a[tar] - 1;
    }

    let res = memo.iter().filter(|&&e| e == true).count();
    println!("{}", res);
}
