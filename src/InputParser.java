import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.LinkedList;
import java.util.List;

/**
 * Created by craigbryan on 29/03/15.
 */
public class InputParser {

    private final String POSITIVE_STRING = "\"positive\"";
    private final String NEGATIVE_STRING = "\"negative\"";
    private final String NEUTRAL_STRING = "\"neutral\"";
    private final String OBJECTIVE_STRING = "\"objective\"";

    public List<TweetData> parse(String filename) throws IOException {
        BufferedReader in =
                new BufferedReader(new FileReader(new File(filename)));

        List<TweetData> tweetList = new LinkedList<TweetData>();
        TweetData currentTweet;
        String dataLine = in.readLine();

        while(dataLine != null) {
            currentTweet = dataArrayToTweetData(dataLine.split("\t"));

            if(currentTweet != null) {
                tweetList.add(currentTweet);
            }

            dataLine = in.readLine();
        }

        in.close();
        return tweetList;
    }

    private TweetData dataArrayToTweetData(String[] data) {
        long sid = Long.parseLong(data[0]);
        long uid = Long.parseLong(data[1]);
        Mood mood = moodFromString(data[2]);

        if(mood == null) {
            System.err.println("Skipping tweet " + sid +
                    " due to unrecognized mood string");
            return null;
        }

        return new TweetData(sid, uid, mood, data[3]);
    }

    private Mood moodFromString(String moodString) {
        if(POSITIVE_STRING.equals(moodString)) {
            return Mood.POSITIVE;
        } else if(NEGATIVE_STRING.equals(moodString)) {
            return Mood.NEGATIVE;
        } else if(NEUTRAL_STRING.equals(moodString)) {
            return Mood.NEUTRAL;
        } else if(OBJECTIVE_STRING.equals(moodString)) {
            return Mood.OBJECTIVE;
        } else {
            return null;
        }
    }
}
