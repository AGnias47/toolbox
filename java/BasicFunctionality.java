/*
 *   A. Gnias
 *
 *   Linux 4.18.0-18-generic #19-Ubuntu
 *   openjdk version "11.0.3"
 *   Vim 8.0 [tabstop=3]
 */


class BasicFunctionality {
	public static void HelloWorld() {
		System.out.println("Hello World!");
	}

	public static void MATH() {
		int five = 5;
		int seven = 7;
		//prints 12
		System.out.println(five + seven);
	}

	public static void stringToint() {
		char a = 'a';
		int b = a; //to 97
		System.out.println(b);

		String andy = "Andy";
		String n = andy.substring(1,2);
		char en = n.charAt(0);
		int an = en;
		System.out.println(n + en + an);

	}

	public static void main(String args[])
	{
		HelloWorld();
		MATH();
		stringToint();
	}
}
