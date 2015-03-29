/**
 * Created by craigbryan on 29/03/15.
 */
public class TweetData {
    private long sid;
    private long uid;
    private Mood mood;
    private String tweetString;

    public TweetData(long aSID, long aUID, Mood aMood, String aTweet) {
        sid = aSID;
        uid = aUID;
        mood = aMood;
        tweetString = aTweet;
    }

    public long getSid() {
        return sid;
    }

    public long getUid() {
        return uid;
    }

    public Mood getMood() {
        return mood;
    }

    public String getTweetString() {
        return tweetString;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("sid: " + sid + "\n");
        sb.append("uid: " + uid + "\n");
        sb.append("mood: " + mood + "\n");
        sb.append("tweet: " + tweetString + "\n");
        return sb.toString();
    }
}
