// import ANTLR's runtime libraries
import java.io.*;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;

public class Test {  
  public static void main(String[] args) throws Exception {
    File testFile = new File(args[0]);
    InputStream fileStream = new FileInputStream(testFile);
    // create a CharStream that reads from standard input
    ANTLRInputStream input = new ANTLRInputStream(fileStream);
    
    // create a lexer that feeds off of input file
    fortran77Lexer lexer = new fortran77Lexer(input);
    
    // create a buffer of tokens pulled from the lexer
    CommonTokenStream tokens = new CommonTokenStream(lexer);
    
    // create a parser that feeds off the tokens buffer
    fortran77Parser parser = new fortran77Parser(tokens);
    ParseTree tree = parser.program(); // begin parsing at translationunit rule
    
    // Create a generic parse tree walker that can trigger callbacks
    ParseTreeWalker walker = new ParseTreeWalker();
    f_to_py translator = new f_to_py(tokens);
    // Walk the tree created during the parse, trigger callbacks
    walker.walk(test, tree);
    System.out.println(); // print a \n after translation
  }
}
