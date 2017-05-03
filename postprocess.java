import java.io.*;
import java.util.ArrayList; 

public class postprocess{
	public static void main(String[] args) throws IOException{
		
		boolean defFlag = false;
		int defIndex = 0;
		int indent = 0;
		boolean flag = false;
		boolean linePrinted = false;
		BufferedReader reader = new BufferedReader(new InputStreamReader(  
                new FileInputStream(args[0])));  
		
		String str =reader.readLine(); 
		ArrayList<String> lineArray = new ArrayList<String>();
		for(;;){
			if(str!=null)
			{
		
			 if(!str.isEmpty()&&!str.contains("def")&&!defFlag){
                 lineArray.add(str);

			 }else if(str.contains("def")){
				 defFlag = true;
				 lineArray.add(defIndex, str);
				 defIndex++;
				 
			 }else if(!str.contains("def") && defFlag){
				 lineArray.add(defIndex, str);

				 defIndex++;
				 if(str.contains("#end function")){

					 defFlag =false;
					 defIndex = 0;
				 }
			 }
			 
			 str =reader.readLine(); 
	}else{
		break;
	}
		}
		
		String lastline=null;
		System.out.println();
		
		for(int i = 0; i<lineArray.size(); i++){
			String line = lineArray.get(i);

				if((line.contains("if")||line.contains("for")||line.contains("while")||line.contains("def"))&&!line.contains("#end")){
					System.out.println(lineArray.get(i));

					indent= indent+1;
					
					continue;
				}else if(line.contains("#end")){
					System.out.println(lineArray.get(i));
					flag =true;
					if(indent >0)
					indent--;
				}
				
				for(int j= 0; j<indent; j++){
					System.out.print("\t");
				}
				
				if(!flag && !linePrinted){
					System.out.println(lineArray.get(i));
					}else{
					    linePrinted =false;
						flag =false;
				}
		}
			
		
	}
}

