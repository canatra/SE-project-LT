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
				String sections[]=str.split("\'");
				String temp = sections[0].toLowerCase();
				//System.out.println("Section 0: " + sections[0]);
				for (int i = 1; i < sections.length; i++) {
					//System.out.println("Section " + i + ": " + sections[i]); 
					if (i%2 == 1) { //do not change case of statements in quotes
						temp += "\'";
						temp += sections[i];
						temp += "\'";
					}
					else {
						temp += sections[i].toLowerCase();
					}
				}
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
