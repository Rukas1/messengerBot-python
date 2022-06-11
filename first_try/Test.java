
public class Test
{
    public static void main(String[] args) throws Exception
    {
        System.out.println(clean(""));
    }

    public static String clean(String msg)
    {
        String out = msg.replace("&#39;", "'");
        return out;
    }
}