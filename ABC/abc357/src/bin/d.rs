use proconio::input;

fn main() {
    input! {
        n: String,
    }

    let size = n.parse().unwrap();
    let mut ans = String::from("");
    for i in 0..size {
        println!("i回目 : {}", i);
        ans += &n;
        println!("ans = {}", ans);
        let mut num_ans = ans.parse::<usize>().unwrap();
        println!("nuj_ans = {}", num_ans);
        num_ans %= size;
        ans = num_ans.to_string();
        println!("ans = {}", ans);
    }

    println!("{}", ans);
}
