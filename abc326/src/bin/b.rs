use proconio::input;

fn main() {
    input! {
        n: i32,
    }

    for i in n..i32::MAX {
        if is_326_like_number(i) {
            println!("{}", i);
            return;
        }
    }
}

fn is_326_like_number(mut num: i32) -> bool {
    let one = num % 10;
    num /= 10;
    let ten = num % 10;
    num /= 10;
    let handred = num;

    handred * ten == one
}
