import java.io.*;
import java.util.ArrayList; 

public class postprocess{
	public static void main(String[] args) throws IOException{
		
		int indent = 0;
		boolean flag = false;
		BufferedReader reader = new BufferedReader(new InputStreamReader(  
                new FileInputStream(args[0])));  
		
		String str =reader.readLine(); 
		ArrayList<String> lineArray = new ArrayList<String>();
		for(;;){
			if(str!=null)
			{
             lineArray.add(str);
             str =reader.readLine(); 
			
	}else{
		break;
	}
		}
		
		String lastline=null;
		
		
		for(int i = 0; i<lineArray.size()-1; i++){
			String line = lineArray.get(i);
			if(!line.equals(lastline)){
				if(line.contains("if")||line.contains("for")||line.contains("while")){
					indent++;
				}else if(line.contains("#end")){
					flag =true;
					indent--;
					
					
				}
			}
			
			for(int j= 0; j<indent; j++){
				System.out.print("\t");
			}
			
			if(!flag){
			System.out.println(lineArray.get(i+1));
			}else{
				System.out.println(lineArray.get(i));
				flag =false;
			}
			
		}
	}
}
