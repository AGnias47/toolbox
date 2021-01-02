public class Human extends Mammal implements IMove {

    private Human(Builder builder) {
        this.name = builder.name;
        this.weight = builder.weight;
        this.sex = builder.sex;
    }

    public void walk() {
        System.out.println("I am a walking human.");
    }

    public void run() {
        System.out.println("I am a running human!");
    }

    public static class Builder {
        private final String name;

        private int weight;
        private Sex sex;

        public Builder(String name) {
            this.name = name;
        }

        public Builder weight(int weight) {
            this.weight = weight;
            return this;
        }

        public Builder sex(Sex sex) {
            this.sex = sex;
            return this;
        }

        public Human build() {
            return new Human(this);
        }

    }
}
