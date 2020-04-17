
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;


/**
 * Sentiment Analysis Training Data
 */
public class SentimentAnalysisTrainingData {

    public static void main(String[] args) {
        try {
            String filename;
            String file;
            String text;
            String filePath = "SentimentAnalysisDataset.csv";
            List<String> lines = Files.readAllLines(Paths.get(filePath),StandardCharsets.ISO_8859_1);
            for(String s : lines){
                String[] oneLine = s.split(",");
                if(Integer.parseInt(oneLine[1])==1){
                    filename = "pos";
                }else{
                    filename = "neg";
                }
                file = oneLine[0]+".txt";
                text = oneLine[3];
                Files.write(Paths.get("review_polarity\\txt_sentoken\\"+filename+"\\"+file), text.getBytes());
            }

        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }

}