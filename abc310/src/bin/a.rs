use proconio::input;

fn main() {
    input! {
        n: usize,
        p: i32,
        q: i32,
        d: [i32; n],
    }

    let min = d.iter().min().unwrap();
    let res = if p < q + min { p } else { q + min };
    println!("{}", res);
}
