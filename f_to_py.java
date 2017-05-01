import org.antlr.v4.runtime.misc.Interval;
import org.antlr.v4.runtime.BufferedTokenStream;
import org.antlr.v4.runtime.Token;

public class f_to_py extends fortran77BaseListener{
    BufferedTokenStream tokens;

    public f_to_py(BufferedTokenStream tokens){

	this.tokens = tokens;
    }


	@Override
	public void enterAssignmentStatement(fortran77Parser.AssignmentStatementContext ctx) {
		// TODO Auto-generated method stub
		super.enterAssignmentStatement(ctx);
        String temp = ctx.getText();
        String temp2;
	   
	    temp2 = temp.replace(".false.", "False").replace(".true.","True");
	    System.out.print(temp2);
        
	}    
    
    	@Override public void enterPrintStatement(fortran77Parser.PrintStatementContext ctx) {

	    
	    System.out.print("print ");
	    String delims ="print";
	    String tobeparsed = ctx.getText();
	   String temp= tobeparsed.replace("*,","");
	    String [] tokens = temp.split(delims);
	    
	    
	    for (int i = 1; i < tokens.length; ++i)
		{
		   
		    	System.out.print(tokens[i]);
		    	
		
		}
	    //test for SEOS?
	   
	
	}

    //use this function and parse the read statement;
	@Override public void enterReadStatement(fortran77Parser.ReadStatementContext ctx) {
	    String delims ="[read,,]+";
	    String tobeparsed = ctx.getText();
	    String [] tokens = tobeparsed.split(delims);
	    
	    
	    for (int i = 1; i < tokens.length; ++i)
		{
		    
		    if (tokens[i].equals("*") )
		    	continue;
		    else{
		    	System.out.print(tokens[i]);
		    	System.out.println(" = input(\" \")");
		    	    }
		}
	}
    
	@Override public void enterSeos(fortran77Parser.SeosContext ctx) {
	        System.out.println(" ");   
	}

@Override public void enterVarRef(fortran77Parser.VarRefContext ctx){
    // System.out.println("in enterVarRef function");
    //System.out.print(ctx.getText());

}


    //don't use these functions
   @Override public void enterFormatIdentifier(fortran77Parser.FormatIdentifierContext ctx) {

       
       //System.out.println(ctx.getText());
    }

    @Override public void enterIoList(fortran77Parser.IoListContext ctx) {// System.out.println(ctx.getText());
    }

	@Override
	public void enterParamassign(fortran77Parser.ParamassignContext ctx) {
		// TODO Auto-generated method stub
		System.out.print(ctx.getText());
			System.out.print(ctx.getParent());
			//super.enterParamassign(ctx);
	}


    
	@Override public void enterDoVarArgs(fortran77Parser.DoVarArgsContext ctx) {

	    String temp = ctx.getText();
	    String temp2 = temp.replace("<missing '='>", " ");
	 
	    temp2 = temp2.replace("do","");
			       
	    if (temp2.contains("while")){
		System.out.print(temp2);
	    }
	    else{
		
		String delims = "=";
		String [] tokens = temp2.split(delims);
		
		System.out.print("for ");
		
		for (int i = 0; i < tokens.length; ++i)
		    {
			if ( i < 1){
			    System.out.print(tokens[i]);
			    System.out.print(" in xrange(");
			}else{
			    System.out.print(tokens[i]);
			}
					    
		}

	    System.out.print(")");
	    }
      
	    System.out.print(": #loop");
	    
	}
    
    	@Override public void exitDoStatement(fortran77Parser.DoStatementContext ctx) {
	    System.out.print("#end loop");
	}

    
    
}//end of class
