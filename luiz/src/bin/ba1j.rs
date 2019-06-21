use std::collections::{HashMap, HashSet};
use std::env;
use std::error::Error;
use std::fs;
use std::str;

use bioinformatics_algorithms::{neighbors, revc};

pub fn frequent_words_with_mismatches_and_rc(text: &[u8], k: usize, d: usize) -> HashSet<String> {
    let mut kmers = HashMap::new();
    let mut frequent = HashSet::new();
    let mut max = 0;

    text.windows(k)
        .map(|x| {
            for pattern in neighbors(str::from_utf8(x).unwrap(), d) {
                let rc_str = revc(&pattern);
                let mut current_freq = 0;
                {
                    let kmer = kmers.entry(pattern.clone()).or_insert(0);
                    *kmer += 1;

                    current_freq += *kmer;
                }

                if let Some(&rc_c) = kmers.get(&rc_str) {
                    current_freq += rc_c
                };

                if current_freq == max {
                    frequent.insert(pattern);
                    frequent.insert(rc_str);
                } else if current_freq > max {
                    max = current_freq;
                    frequent.clear();
                    frequent.insert(pattern);
                    frequent.insert(rc_str);
                }
            }
        })
        .count();

    frequent
}

fn main() -> Result<(), Box<dyn Error>> {
    let input: String = env::args()
        .nth(1)
        .unwrap_or("data/rosalind_ba1j.txt".into());
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

    for word in frequent_words_with_mismatches_and_rc(text.as_bytes(), k, d) {
        print!("{} ", word);
    }
    println!();

    Ok(())
}
