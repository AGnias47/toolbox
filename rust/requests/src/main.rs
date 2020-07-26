#[macro_use]
extern crate clap;
use clap::App;
use error_chain::error_chain;
use std::io::Read;

error_chain! {
    foreign_links {
        Io(std::io::Error);
        HttpRequest(reqwest::Error);
    }
}

fn main() -> Result<()> {
    let yaml = load_yaml!("cli.yml");
    let matches = App::from_yaml(yaml).get_matches();
    let url = matches.value_of("url").unwrap_or("http://httpbin.org/get");

    // ?: Unpack Result if okay, else return error
    let mut response = reqwest::blocking::get(url)?;
    let mut body = String::new();
    response.read_to_string(&mut body)?;

    println!("Status: {}", response.status());
    println!("Body: {}", body);

    Ok(())
}
