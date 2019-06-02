/*
 *   A. Gnias
 *
 *   Linux 4.18.0-18-generic #19-Ubuntu
 *   openjdk version "11.0.3"
 *   Vim 8.0 [tabstop=3]
 */

public class Dog implements Animal {

	public String _name;
	public int _weight;
	public Color _color;

	public Dog(String name)
	{
		_name = name;
		_weight = _name.charAt(0);
		_color = Color.Copper;
	}

	public void eat() {
		System.out.println("nom nom nom");
	}

	public void sleep() {
		System.out.println("zzzzz");
	}

	public String name() {
		return _name;
	}

	public int weight() {
		return _weight;
	}

	public Color color() {
		return _color;
	}

	public static void main(String args[])
	{
		Dog doggy = new Dog("Annika");
		System.out.println("Name: " + doggy.name());
		System.out.println("Weight: " + doggy.weight());
		System.out.println("Color: " + doggy.color());
	}
}
