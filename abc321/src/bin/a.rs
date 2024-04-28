use proconio::input;
// use proconio::marker::Chars;

// fn main() {
//     input! {
//         n: Chars,
//     }

//     if n.windows(2).any(|w| w[0] <= w[1]) {
//         println!("No");
//     } else {
//         println!("Yes");
//     }
// }

fn main() {
    input! {
        mut n: i32,
    }

    let mut prev_digit = n % 10;
    n /= 10;
    while n > 0 {
        let curr_digit = n % 10;

        // println!("curr_digit = {} : prev_digit = {}", curr_digit, prev_digit);

        if curr_digit <= prev_digit {
            println!("No");
            return;
        }
        n /= 10;
        prev_digit = curr_digit;
    }
    println!("Yes");
}
