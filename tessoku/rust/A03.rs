use proconio::input;

fn main() {
    input! {
        n: usize,
        k: usize,
        p: [usize; n],
        q: [usize; n],
    }

    for i in p.iter() {
        for j in q.iter() {
            if i + j == k {
                println!("Yes");
                return;
            }
        }
    }

    println!("No");
}
