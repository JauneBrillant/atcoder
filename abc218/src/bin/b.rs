use proconio::input;

fn main() {
    input! {
        p: [u8; 26],
    }

    let mut res = String::new();
    for i in 0..26 {
        let c = (96 + p[i]) as char;
        res.push(c);
    }

    println!("{}", res);
}
