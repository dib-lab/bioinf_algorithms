use std::collections::HashMap;
use std::env;
use std::error::Error;
use std::fs;

use bioinformatics_algorithms::{composition, overlap};

pub fn de_bruijn(k: usize, text: &str) -> HashMap<String, Vec<String>> {
    let kmers: Vec<&str> = composition(k - 1, text).collect();

    let mut dbg = HashMap::default();

    for (kmer, neighbor) in overlap(&kmers) {
        let neighbors = dbg.entry(kmer).or_insert(Vec::with_capacity(4));
        neighbors.push(neighbor);
    }

    dbg
}

fn main() -> Result<(), Box<dyn Error>> {
    let input: String = env::args()
        .nth(1)
        .unwrap_or("data/rosalind_ba3d.txt".into());
    let data = fs::read_to_string(input)?;

    let mut lines = data.lines();
    let k = lines.next().unwrap().parse()?;
    let text: String = lines.next().unwrap().into();

    for (node, neighbors) in de_bruijn(k, &text) {
        if neighbors.len() == 1 {
            println!("{} -> {}", node, neighbors[0]);
        } else {
            print!("{} -> {}", node, neighbors[0]);

            for neighbor in &neighbors[1..] {
                print!(",{}", neighbor);
            }
            println!();
        }
    }

    Ok(())
}
