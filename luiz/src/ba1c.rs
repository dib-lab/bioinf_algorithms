use std::env;
use std::error::Error;
use std::fs;

pub fn revc(text: &[u8]) -> String {
    text.iter()
        .rev()
        .map(|x| match *x as char {
            'A' => "T",
            'C' => "G",
            'G' => "C",
            'T' => "A",
            _ => panic!(),
        })
        .collect()
}

fn main() -> Result<(), Box<dyn Error>> {
    assert_eq!(revc(b"AAAACCCGGT"), "ACCGGGTTTT");

    let input: String = env::args().nth(1).expect("Input data file missing");
    let data = fs::read_to_string(input)?;
    let mut lines = data.lines();

    let text = lines.next().unwrap();

    println!("{}", revc(text.as_bytes()));

    Ok(())
}
