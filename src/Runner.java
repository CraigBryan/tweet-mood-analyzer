import java.io.IOException;
import java.util.List;

/**
 * Created by craigbryan on 29/03/15.
 */
public class Runner {

    public static void main(String[] args) {
        InputParser parser = new InputParser();
        List<TweetData> tweetList = null;

        try {
            tweetList = parser.parse("res/semeval_twitter_data.txt");
        } catch (IOException e) {
            e.printStackTrace();
            System.exit(-1);
        }

    }
}
