public class DogFactory {
    public Dog createDog(String dogType, String dogName) {
        if (dogType.equalsIgnoreCase("Black Mouth Cur") || dogType.equalsIgnoreCase("BMC")) {
            return new BlackMouthCur.Builder(dogName).build();
        }
        else if (dogType.equalsIgnoreCase("Husky")) {
            return new Husky.Builder(dogName).build();
        }
        else {
            return null;
        }
    }
}
