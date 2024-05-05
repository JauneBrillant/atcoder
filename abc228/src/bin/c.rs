use proconio::input;

fn main() {
    input! {
        n: usize,
        k: usize,
    }

    let mut p = vec![];
    for i in 0..n {
        input! {
            arr: [usize; 3],
        }
        let total = arr.iter().sum::<usize>();
        p.push((i, total));
    }

    let mut sorted_p = p.clone();
    sorted_p.sort_by(|(_, v1), (_, v2)| v2.cmp(v1));

    for i in 0..n {
        if p[i].1 + 300 >= sorted_p[k - 1].1 {
            println!("Yes");
        } else {
            println!("No");
        }
    }
}
