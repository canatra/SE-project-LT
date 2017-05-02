import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class preprocess{
public static void main(String[] args) throws IOException{
    BufferedReader reader = new BufferedReader(new InputStreamReader(new FileInputStream(args[0])));
		
		String str =reader.readLine(); 
		ArrayList<String> lineArray = new ArrayList<String>();
		
		for(;;){
			if(str==null) break;
			
			String tokens[]=str.split(" ");
			if(str.isEmpty()||tokens[0].equals("c")){
			// do nothing for blankline or comment line 	
			}
			else {
			String temp=str.toLowerCase();
			lineArray.add(temp);
			}
			
			str = reader.readLine();
		}
		
		
		for(String i:lineArray){
			System.out.println(i);
		}
	/*	String temp= "ABCD E F ";
		String temp2 =temp.toLowerCase();
		System.out.println(temp2);   */
		
		reader.close();
	}
}
