use std::collections::{HashMap, HashSet};
use std::env;
use std::error::Error;
use std::fs;

pub fn find_clumps(text: &[u8], ksize: usize, length: usize, times: usize) -> HashSet<String> {
    let mut keepers = HashSet::new();

    let mut kmer_counts = HashMap::new();

    text.windows(ksize)
        .take(length)
        .map(|x| {
            let kmer = kmer_counts.entry(x).or_insert(0);
            *kmer += 1;

            if *kmer >= times {
                keepers.insert(String::from_utf8(x.to_vec()).unwrap());
            };
        })
        .count();

    for i in 1..=text.len() - length {
        let prev_kmer = &text[i - 1..i + ksize - 1];
        let kmer = kmer_counts.entry(prev_kmer).or_insert(0);
        *kmer -= 1;

        let last_kmer = &text[i + length - ksize..i + length];
        let kmer = kmer_counts.entry(last_kmer).or_insert(0);
        *kmer += 1;

        if *kmer >= times {
            keepers.insert(String::from_utf8(last_kmer.to_vec()).unwrap());
        };
    }

    keepers
}

fn main() -> Result<(), Box<dyn Error>> {
    let input: String = env::args()
        .nth(1)
        .unwrap_or("data/rosalind_ba1e.txt".into());
    let data = fs::read_to_string(input)?;
    let mut lines = data.lines();

    let text = lines.next().unwrap();
    let params: Vec<usize> = lines
        .next()
        .unwrap()
        .split_whitespace()
        .take(3)
        .map(|w| w.parse::<usize>().unwrap())
        .collect();

    let k = params[0];
    let l = params[1];
    let t = params[2];

    for word in find_clumps(text.as_bytes(), k, l, t) {
        print!("{} ", word);
    }
    println!();

    Ok(())
}
