use proconio::input;

fn main() {
    input! {
        n: usize,
        p: [i32; n],
    }

    if n == 1 {
        println!("0");
        return;
    }

    let goal = p.iter().skip(1).max().unwrap() + 1;
    let res = goal - p[0];
    println!("{}", if p[0] < goal { res } else { 0 });
}
