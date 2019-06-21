use std::collections::HashSet;
use std::env;
use std::error::Error;
use std::fs;
use std::str;

use bioinformatics_algorithms::{hamming, neighbors};

pub fn motif_enumeration(text: Vec<String>, k: usize, d: usize) -> HashSet<String> {
    let mut patterns = HashSet::new();

    let first = &text[0];
    first
        .as_str()
        .as_bytes()
        .windows(k)
        .map(|pattern| {
            for pattern_p in neighbors(str::from_utf8(pattern).unwrap(), d) {
                patterns.insert(pattern_p);
            }
        })
        .count();

    for dna in &text[1..] {
        let mut current = HashSet::<String>::new();
        dna.as_str()
            .as_bytes()
            .windows(k)
            .map(|x| {
                for pattern_p in &patterns {
                    let pattern = str::from_utf8(x).unwrap();
                    if hamming(pattern, pattern_p) <= d {
                        current.insert(pattern_p.clone());
                    }
                }
            })
            .count();

        patterns = current.into_iter().collect();
    }

    patterns
}

fn main() -> Result<(), Box<dyn Error>> {
    let input: String = env::args()
        .nth(1)
        .unwrap_or("data/rosalind_ba2a.txt".into());
    let data = fs::read_to_string(input)?;
    let mut lines = data.lines();

    let mut ints = lines
        .next()
        .unwrap()
        .split(' ')
        .map(|x| x.parse().unwrap())
        .take(2);
    let k = ints.next().unwrap();
    let d = ints.next().unwrap();

    let text: Vec<String> = lines.map(|x| x.into()).collect();

    for word in motif_enumeration(text, k, d) {
        print!("{} ", word);
    }
    println!();

    Ok(())
}
