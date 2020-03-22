pub fn print_string(s: String)
{
    println!("{}", s);
}

pub fn cube(a: u32) -> u32
{
    return a.pow(3);
}

pub fn get_float_quotient(numerator: i32, denominator: i32) -> f32
{
    let numerator = numerator as f32;
    let denominator = denominator as f32;
    return numerator / denominator;
}

pub fn is_prime(n: i32) -> bool {
    let upper_limit: i32 = (n as f64).sqrt() as i32 + 1;
    for i in 2..upper_limit {
        if n % i == 0 { 
            return false;
        }
    }
    return true;
}


