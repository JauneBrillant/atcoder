use proconio::input;

fn main() {
    input! {
        n: usize,
    }

    let mut res = 0;
    for i in 1..=n {
        let str_num = i.to_string();
        if str_num.len() % 2 == 1 {
            res += 1;
        }
    }

    println!("{}", res);
}
