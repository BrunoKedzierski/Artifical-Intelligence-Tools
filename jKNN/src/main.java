import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;
import java.util.stream.Collectors;

public class main {


    public static void main(String[] args) throws Exception {
        List<List<String>> training_raw = new ArrayList<>();
        List<List<String>> test_raw = new ArrayList<>();


        try(BufferedReader training_reader = new BufferedReader(new FileReader("iris_training.csv"))){

            String line;
            while ((line = training_reader.readLine()) != null) {
                String[] values = line.split(",");
                training_raw.add(Arrays.asList(values));
            }

        } catch (IOException e) {
            e.printStackTrace();
        }


        try(BufferedReader test_reader = new BufferedReader(new FileReader("iris_test.csv"))){

            String line;
            while ((line = test_reader.readLine()) != null) {
                String[] values = line.split(",");
                test_raw.add(Arrays.asList(values));
            }

        } catch (IOException e) {
            e.printStackTrace();
        }




        KnnClassifier classifier = new KnnClassifier(test_raw,training_raw,3);

        System.out.println("Model accuracy: " + classifier.testClassifier());

        Scanner scan = new Scanner(System.in);
        boolean flag = true;
        while (flag) {
            System.out.println("Do you want to classify a vector?");
            String ans = scan.nextLine();
            if(ans.equals("n"))
                break;
            else if(ans.equals("y")) {
                System.out.println("Enter four coordinates, separated by comma");
                String vec = scan.nextLine();
                System.out.println("Prediction: " + classifier.predict(Arrays.asList(vec.split(","))));
            }
            else
                System.out.println("try again");
        }



    }
}
