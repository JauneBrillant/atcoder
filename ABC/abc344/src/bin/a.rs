use proconio::input;

fn main() {
    input! {
        s: String,
    }

    let mut index_one = None;
    let mut index_two = None;
    for (i, c) in s.chars().enumerate() {
        if c == '|' {
            if index_one.is_none() {
                index_one = Some(i);
            } else {
                index_two = Some(i);
            }
        }
    }

    let res: String = s.chars().enumerate().filter_map(|(i, c)| {
        if i < index_one.unwrap() || i > index_two.unwrap() {
            Some(c)
        } else {
            None
        }
    }).collect();

    println!("{}", res);
}
