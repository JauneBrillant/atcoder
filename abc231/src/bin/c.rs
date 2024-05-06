// use proconio::input;

// fn main() {
//     input! {
//         n: usize,
//         q: usize,
//         mut a: [usize; n],
//         x: [usize; q],
//     }

//     a.sort_by(|a, b| b.cmp(a));

//     let mut ordered_p = vec![];
//     for (i, h) in x.iter().enumerate() {
//         ordered_p.push((i, h))
//     }
//     ordered_p.sort_by(|&(_, h1), &(_, h2)| h2.cmp(h1));

//     // println!("a = {:?}", a);
//     // println!("ordered_p = {:?}", ordered_p);

//     let mut ans = vec![];
//     let mut i = 0;
//     let mut total = 0;
//     for (pos, &q) in ordered_p {
//         while i < n && a[i] >= q {
//             i += 1;
//             total += 1;
//             if i == n {
//                 break;
//             }
//         }
//         ans.push((pos, total));
//     }

//     ans.sort();
//     for (_, v) in ans {
//         println!("{}", v);
//     }
// }

use proconio::input;

fn main() {
    input! {
        n: usize,
        q: usize,
        a: [usize; n],
        x: [usize; q],
    }

    let mut sorted_a = a;
    sorted_a.sort();
    for h in x {
        let pos = sorted_a.binary_search(&h).unwrap_or_else(|e| e);
        println!("{}", n - pos);
    }
}
