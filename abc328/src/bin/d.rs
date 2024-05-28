use proconio::input;

fn main() {
    input! {
        s: String,
    }

    let res = s
        .chars()
        .fold(vec![], |mut stack, c| {
            stack.push(c);
            let len = stack.len() - 1;
            if stack.len() >= 3
                && stack[len] == 'C'
                && stack[len - 1] == 'B'
                && stack[len - 2] == 'A'
            {
                stack.pop();
                stack.pop();
                stack.pop();
            }
            stack
        })
        .iter()
        .collect::<String>();

    println!("{}", res);
}
