use proconio::input;

fn main() {
    input! {
        n: usize,
        a: [i64; n],
    }

    let mut res: Vec<i64> = vec![];
    for num in a {
        res.push(num);

        loop {
            if res.len() <= 1 {
                break;
            }

            if res[res.len() - 1] != res[res.len() - 2] {
                break;
            }

            let last = res.pop();
            let _second_last = res.pop();
            res.push(last.unwrap() + 1);
        }
    }
    println!("{}", res.len());
}
