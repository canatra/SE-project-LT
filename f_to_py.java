import org.antlr.v4.runtime.misc.Interval;
import org.antlr.v4.runtime.BufferedTokenStream;
import org.antlr.v4.runtime.Token;

public class f_to_py extends fortran77BaseListener{
    BufferedTokenStream tokens;

    public f_to_py(BufferedTokenStream tokens){

	this.tokens = tokens;
    }

    @Override
    public void enterProgram(fortran77Parser.ProgramContext ctx)
    {
	//open the python file, write program comments in the python file, translate libraries?
	System.out.println("entering program");
    }
    
    @Override
    public void exitProgram(fortran77Parser.ProgramContext ctx){

    }


    @Override public void enterFunctionSubprogram(fortran77Parser.FunctionSubprogramContext ctx) { }

    @Override public void exitFunctionSubprogram(fortran77Parser.FunctionSubprogramContext ctx) { }

    @Override public void enterSubroutineSubprogram(fortran77Parser.SubroutineSubprogramContext ctx) { }

    @Override public void exitSubroutineSubprogram(fortran77Parser.SubroutineSubprogramContext ctx) { }

    	@Override public void enterFunctionStatement(fortran77Parser.FunctionStatementContext ctx) { }

    
    	@Override public void exitFunctionStatement(fortran77Parser.FunctionStatementContext ctx) { }

    	@Override public void enterSubroutineStatement(fortran77Parser.SubroutineStatementContext ctx) { }

    	@Override public void exitSubroutineStatement(fortran77Parser.SubroutineStatementContext ctx) { }

    
    
}
