/*
 *   A. Gnias
 *   openjdk version "11.0.3"
 */

public class BlackMouthCur extends Dog {

    private BlackMouthCur(Builder builder) {
        this.name = builder.name;
        this.weight = builder.weight;
        this.sex = builder.sex;
    }

    public void howl() {
        System.out.println("owoo");
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
            return new BlackMouthCur(this);
        }

    }
}
