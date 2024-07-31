use proconio::input;

fn main() {
    input! {
        n: i64,
        k: usize,
    }

    let mut num = n;
    for _ in 0..k {
        let base10 = from_8_to_10(num);
        let base9 = from_10_to_9(base10);
        let str_base9 = base9.to_string();
        let after_str = str_base9.replace('8', "5");
        num = after_str.parse::<i64>().unwrap();
    }

    println!("{}", num);
}

fn from_8_to_10(mut num: i64) -> i64 {
    let mut res = 0;
    let len = num.to_string().len();
    for i in 0..len {
        let digit = num % 10;
        res += 8_i64.pow(i as u32) * digit;
        num /= 10;
    }

    res
}

fn from_10_to_9(mut num: i64) -> i64 {
    let mut res = vec![];
    while num > 0 {
        res.push((num % 9).to_string());
        num /= 9;
    }

    res.into_iter()
        .rev()
        .collect::<String>()
        .parse::<i64>()
        .unwrap()
}
