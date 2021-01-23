public class Husky extends Dog {

    private Husky(Builder builder) {
        this.name = builder.name;
        this.weight = builder.weight;
        this.sex = builder.sex;
    }

    public void howl() {
        System.out.println("OWOOOOOOOO!");
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

        public Dog build() {
            return new Husky(this);
        }

    }
}
