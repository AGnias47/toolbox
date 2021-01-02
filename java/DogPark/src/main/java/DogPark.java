public class DogPark {
    public static void main(String[] args) {
        Dog Annika = new BlackMouthCur.Builder("Annika").build();
        System.out.println(Annika.name);
        Dog Lupa = new Husky.Builder("Lupa").sex(Sex.Female).build();
        System.out.println(Lupa.name + ", "+ Lupa.sex);
        DogFactory dogFactory = new DogFactory();
        Dog Sky = dogFactory.createDog("Husky", "Sky");
        System.out.println(Sky.name);
        Human Quinn = new Human.Builder("Quinn").sex(Sex.Intersex).build();
        System.out.println(Quinn.name + ", " + Quinn.sex);
        Lupa.walk();
        Annika.run();
        Quinn.run();
        Sky.howl();
    }
}
