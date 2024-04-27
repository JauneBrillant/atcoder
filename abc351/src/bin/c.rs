use proconio::input;

fn main() {
    input! {
        n: usize,
        a: [i64; n],
    }

    let mut arr: Vec<i64> = vec![];
    for num in a {
        arr.push(num);
        while arr.len() >= 2 && arr[arr.len() - 1] == arr[arr.len() - 2] {
            arr.pop();
            let last = arr.pop().unwrap();
            arr.push(last + 1);
        }
    }
    println!("{}", arr.len());
}
