use error_chain::error_chain;
use std::io::Read;

error_chain! {
    foreign_links {
        Io(std::io::Error);
        HttpRequest(reqwest::Error);
    }
}

fn main() -> Result<()> {
    // ?: Unpack Result if okay, else return error
    let mut response = reqwest::blocking::get("http://httpbin.org/get")?;
    let mut body = String::new();
    response.read_to_string(&mut body)?;

    println!("Status: {}", response.status());
    println!("Body: {}", body);

    Ok(())
}
