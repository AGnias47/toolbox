mod basic_functionality;

fn main()
{
	basic_functionality::print_string(String::from("Hello World!"));
	let a = basic_functionality::cube(5);
	println!("{}", a);
}
