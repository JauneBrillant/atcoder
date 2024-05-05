// use proconio::input;

// fn main() {
//     input! {
//         n: usize,
//         mut m: usize,
//         p: usize,
//     }

//     let mut res = 0;
//     while m <= n {
//         res += 1;
//         m += p;
//     }

//     println!("{}", res);
// }
//

use proconio::input;
fn main() {
    input! {
        n: usize,
        m: usize,
        p: usize,
    }

    if n < m {
        println!("0");
        return;
    }

    let mut res = 1;
    res += (n - m) / p;
    println!("{}", res);
}
