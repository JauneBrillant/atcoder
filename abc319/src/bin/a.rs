use proconio::input;
use std::collections::HashMap;

fn main() {
    input! {
        s: String,
    }

    let mut hashmap: HashMap<String, usize> = HashMap::new();
    hashmap.insert(String::from("tourist"), 3858);
    hashmap.insert(String::from("ksun48"), 3679);
    hashmap.insert(String::from("Benq"), 3658);
    hashmap.insert(String::from("Um_nik"), 3648);
    hashmap.insert(String::from("apiad"), 3638);
    hashmap.insert(String::from("Stonefeang"), 3630);
    hashmap.insert(String::from("ecnerwala"), 3613);
    hashmap.insert(String::from("mnbvmar"), 3555);
    hashmap.insert(String::from("newbiedmy"), 3516);
    hashmap.insert(String::from("semiexp"), 3481);

    if let Some(rate) = hashmap.get(&s) {
        println!("{}", rate);
    } else {
        // pass
    }
}
