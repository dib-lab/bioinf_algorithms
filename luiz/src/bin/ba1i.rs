use std::cmp;
use std::collections::HashMap;
use std::env;
use std::error::Error;
use std::fs;
use std::str;

use bioinformatics_algorithms::neighbors;

pub fn frequent_words_with_mismatches(text: &[u8], k: usize, d: usize) -> Vec<String> {
    let mut frequent = HashMap::new();
    let mut max = 0;

    text.windows(k)
        .map(|x| {
            for pattern in neighbors(str::from_utf8(x).unwrap(), d) {
                let kmer = frequent.entry(pattern).or_insert(0);
                *kmer += 1;
                max = cmp::max(max, *kmer);
            }
        })
        .count();

    frequent
        .iter()
        .filter_map(|(kmer, &count)| {
            if count == max {
                Some(kmer.clone())
            } else {
                None
            }
        })
        .collect()
}

fn main() -> Result<(), Box<dyn Error>> {
    let input: String = env::args()
        .nth(1)
        .unwrap_or("data/rosalind_ba1i.txt".into());
    let data = fs::read_to_string(input)?;
    let mut lines = data.lines();

    let text = lines.next().unwrap();
    let mut ints = lines
        .next()
        .unwrap()
        .split(' ')
        .map(|x| x.parse().unwrap())
        .take(2);
    let k = ints.next().unwrap();
    let d = ints.next().unwrap();

    for word in frequent_words_with_mismatches(text.as_bytes(), k, d) {
        print!("{} ", word);
    }
    println!();

    Ok(())
}
