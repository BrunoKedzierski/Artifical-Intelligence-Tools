import javax.swing.*;
import java.util.*;

public class KnnClassifier {

    List<List<String>> testSet;
    List<List<String>> trainingSet;
    int k;

    public KnnClassifier(List<List<String>> testSet, List<List<String>> trainingSet, int k) {
        this.testSet = testSet;
        this.trainingSet = trainingSet;
        this.k = k;

    }



    public double testClassifier() throws Exception {
        int no_of_correct = 0;


        for ( List<String> line_test: testSet) {
            Map<Double, String> neighbors = new TreeMap<>();
            for ( List<String> line_training: trainingSet){
                double distance = calcDistance(line_test.subList(0,line_test.size()-1), line_training.subList(0,line_training.size()-1));
                neighbors.put(distance, line_training.get(line_training.size() -1 ));
            }
            





            String prediciton =  decideKNeigbors( Arrays.copyOf(neighbors.values().toArray(), neighbors.values().toArray().length, String[].class), false);
           // System.out.println("Prediction: " + prediciton + " " + "Actual: " + line_test.get(line_test.size() -1));
            if (prediciton.equals(line_test.get(line_test.size() -1))) {
              //  System.out.println("Correct!");
                no_of_correct += 1;
            }
        }

        return  no_of_correct/(double)testSet.size();
    }

    public String predict(List<String> v) throws Exception {
        Map<Double, String> neighbors = new TreeMap<>();
        for ( List<String> line_training: trainingSet){
            double distance = calcDistance(v, line_training.subList(0,line_training.size()-1));
            neighbors.put(distance, line_training.get(line_training.size() -1 ));
        }
        String[] ar = Arrays.copyOf(neighbors.values().toArray(), neighbors.values().toArray().length, String[].class);

        String prediciton =  decideKNeigbors( ar,true);
        return prediciton;

    }

    public static double calcDistance(List<String> v1, List<String> v2) throws Exception {

        if(v1.size() != v2.size())
            throw new Exception("Input vectors are not the same size!");

        double distance = 0;

        for (int i = 0; i < v1.size(); i++) {



            distance += Math.pow(Double.parseDouble( v2.get(i)) - Double.parseDouble(v1.get(i)),2);
        }

        return distance;


    }

    public String decideKNeigbors(String[] arr, Boolean print){


        Map<String, Integer> cnt = new HashMap<>();

        for (int i = 0; i < this.getK() ; i++) {
            cnt.merge(arr[i], 1 , (a,b) ->Integer.sum(a, b));

        }

        int maxcnt =0;
        String nearest = null;
        for (Map.Entry<String, Integer> entry: cnt.entrySet()) {
            if (entry.getValue() > maxcnt)
                nearest = entry.getKey();

        }
        if(print)
            System.out.println("Closest neighbors: " + cnt.keySet().toString());


        return  nearest;


    }

    public List<List<String>> getTestSet() {
        return testSet;
    }

    public void setTestSet(List<List<String>> testSet) {
        this.testSet = testSet;
    }

    public List<List<String>> getTrainingSet() {
        return trainingSet;
    }

    public void setTrainingSet(List<List<String>> trainingSet) {
        this.trainingSet = trainingSet;
    }

    public int getK() {
        return k;
    }

    public void setK(int k) {
        this.k = k;
    }
}
