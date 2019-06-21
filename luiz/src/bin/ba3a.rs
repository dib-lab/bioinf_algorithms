use std::collections::HashSet;
use std::env;
use std::error::Error;
use std::fs;

// This function is also defined in lib.rs
pub fn composition(k: usize, text: &[u8]) -> HashSet<String> {
    text.windows(k)
        .map(|kmer| String::from_utf8_lossy(kmer).into_owned())
        .collect()
}

fn main() -> Result<(), Box<dyn Error>> {
    let input: String = env::args()
        .nth(1)
        .unwrap_or("data/rosalind_ba3a.txt".into());
    let data = fs::read_to_string(input)?;
    let mut lines = data.lines();

    let k = lines.next().unwrap().parse()?;

    let text: String = lines.next().unwrap().into();

    for kmer in composition(k, text.as_str().as_bytes()) {
        println!("{}", kmer);
    }

    Ok(())
}
