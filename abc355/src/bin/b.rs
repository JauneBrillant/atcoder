use proconio::input;

fn main() {
    input! {
        n: usize,
        m: usize,
        a: [usize; n],
        b: [usize; m],
    }

    let mut ab = vec![];
    for i in 0..n {
        ab.push((a[i], 'a'));
    }

    for i in 0..m {
        ab.push((b[i], 'b'));
    }

    ab.sort();
    for i in 0..n + m - 1 {
        if ab[i].1 == 'a' && ab[i].1 == ab[i + 1].1 {
            println!("Yes");
            return;
        }
    }

    println!("No");
}
