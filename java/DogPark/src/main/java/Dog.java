public abstract class Dog extends Mammal implements IMove {
	public void walk() {
		System.out.println("Trit Trot");
	}
	public void run() {
		System.out.println("RUN!");
	}

	public abstract void howl();
}