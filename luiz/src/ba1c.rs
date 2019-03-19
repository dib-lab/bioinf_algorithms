use std::env;
use std::error::Error;
use std::fs;

use bioinformatics_algorithms::revc;

fn main() -> Result<(), Box<dyn Error>> {
    assert_eq!(revc("AAAACCCGGT"), "ACCGGGTTTT");

    let input: String = env::args().nth(1).expect("Input data file missing");
    let data = fs::read_to_string(input)?;
    let mut lines = data.lines();

    let text = lines.next().unwrap();

    println!("{}", revc(text));

    Ok(())
}
