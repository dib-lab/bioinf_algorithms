use std::cmp;
use std::collections::HashMap;
use std::env;
use std::error::Error;
use std::fs;

pub fn frequent_words(text: &[u8], k: usize) -> Vec<String> {
    let mut frequent = HashMap::new();
    let mut max = 0;

    text.windows(k)
        .map(|x| {
            let kmer = frequent.entry(x).or_insert(0);
            *kmer += 1;
            max = cmp::max(max, *kmer);
        })
        .count();

    frequent
        .iter()
        .filter_map(|(&kmer, &count)| {
            if count == max {
                Some(String::from_utf8(kmer.to_vec()).unwrap())
            } else {
                None
            }
        })
        .collect()
}

fn main() -> Result<(), Box<dyn Error>> {
    let input: String = env::args()
        .nth(1)
        .unwrap_or("data/rosalind_ba1b.txt".into());
    let data = fs::read_to_string(input)?;
    let mut lines = data.lines();

    let text = lines.next().unwrap();
    let k = lines.next().unwrap().parse()?;

    for word in frequent_words(text.as_bytes(), k) {
        print!("{} ", word);
    }
    println!();

    Ok(())
}
