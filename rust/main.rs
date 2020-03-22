mod basic_functionality;

fn main()
{
    basic_functionality::print_string(String::from("Hello World!"));
    let a = basic_functionality::cube(5);
    println!("{}", a);
    let b = basic_functionality::get_float_quotient(7, 5);
    println!("{}", b);
    let c = 14;
    let d: i32 = 17;
    let e = basic_functionality::is_prime(c);
    let f = basic_functionality::is_prime(d);
    println!("{}, {}", e, f);   
}
