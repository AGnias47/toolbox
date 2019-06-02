/*
 *   A. Gnias
 *
 *   Linux 4.18.0-18-generic #19-Ubuntu
 *   openjdk version "11.0.3"
 *   Vim 8.0 [tabstop=3]
 */

enum Color {
	Black,
	White,
	Copper
}

interface Animal {
	public void eat();
	public void sleep();
	public String name();
	public int weight();
	public Color color();
}

