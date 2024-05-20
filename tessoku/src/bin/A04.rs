use proconio::input;

fn main() {
    input! {
        mut n: usize,
    }
 
    let mut res = vec![];
    while n > 0 {
        if n % 2 == 0 {
            res.push('0');
        } else {
            res.push('1');
        }
        n /= 2;
    }

    while res.len() < 10 {
        res.push('0');
    }

    let s = res.iter().rev().collect::<String>();
    println!("{}", s);
}
