import java.net.HttpURLConnection;
import java.net.URL;
import java.io.BufferedReader;
import java.io.InputStreamReader;


public class BasicRequestToApi
{
    public static void main(String[] args) throws Exception
    {   
        URL url = new URL("https://api.waifu.pics/sfw/waifu");
        HttpURLConnection con = (HttpURLConnection) url.openConnection();
        con.setRequestMethod("GET");
        int status = con.getResponseCode();
        System.out.println(status);
        
        InputStreamReader port = new InputStreamReader(con.getInputStream());
        BufferedReader in = new BufferedReader(port);
        
        String inputLine;
        StringBuilder content = new StringBuilder();
        while ((inputLine = in.readLine()) != null) {
            content.append(inputLine);
        }

        System.out.println(content);
        in.close();
    }
}


/**
import java.net.*;
import java.io.*;

public class BasicRequestToApi 
{
    public static void main(String[] args) throws Exception
    {   
        HttpURLConnection con = (HttpURLConnection) new URL("https://api.waifu.pics/sfw/waifu").openConnection();
        con.setRequestMethod("GET");
        System.out.println(con.getResponseCode());
        System.out.println(new BufferedReader(new InputStreamReader(con.getInputStream())).readLine());
    }
}
*/