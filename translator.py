#!/usr/bin/python
import re

#function to print the tabs at the beginning of the lines
def printtabs(fo, i):
	if i < 1:
		return
	else:
		for i in range (0, i-1):
			fo.write("\t")
	return

#variables; fi should probably be set as a command line argument
index = 0;
#libraries = {"datetime-fortran":"datetime",  }
fo = open("program.py", 'w')

#getting the line and splitting it into tokens

with open("program.f90",'rb') as fi:

        #re.compile()
	while True:
        	codeline=fi.readline()
		if not codeline: break
                codeline =codeline.strip(" ")
                tokens = codeline.split(" ")

	        #if statement controls
                
		if codeline == "\n":
			fo.write("\n")

		elif (tokens[0] == "IF") or (tokens[0] == "if"):
			printtabs(fo, index)
			fo.write("if")
			counter = 1
			while (codeline[counter] != "THEN") and (codeline[counter] != "then") and (codeline[counter] != "EXIT") and (codeline[counter] != "exit"):
				fo.write(" " + codeline[counter])
				counter = counter + 1
			if (codeline[counter] == "THEN") or (codeline[counter] == "then"):
				fo.write(":\n")
			elif (codeline[counter] == "EXIT") or (codeline[counter] == "exit"):
				fo.write(": break\n")
			        index = index + 1
		elif (tokens[0] == "EXIT") or (tokens[0] == "exit"):
			fo.write("break\n")
		elif (tokens[0] == "CONTINUE") or (tokens[0] == "continue"):
			fo.write("continue\n")
		elif (tokens[0] == "ELSE") or (tokens[0] == "else"):
			index = index - 1
			printtabs(fo, index)
			fo.write("elif")
			counter = 2
			while (codeline[counter] != "THEN") and (codeline[counter] != "then") and (codeline[counter] != "EXIT") and (codeline[counter] != "exit"):
				fo.write(" " + codeline[counter])
				counter = counter + 1
			        fo.write(":\n")
			        index = index + 1
		elif (tokens[0] == "ENDIF") or (tokens[0] == "endif"):
			index = index - 1
			printtabs(fo, index)
			fo.write(":\n")
		        #do loop controls
		elif (tokens[0] == "DO") or (tokens[0] == "do"):
			printtabs(fo, index)
			fo.write("for "+ tokens[2] + " in range(" + tokens[4]+ tokens[5] + ":")
			index = index + 1
		elif (tokens[0] == "ENDDO") or (tokens[0] == "enddo"):
			index = index - 1
			printtabs(fo, index)
			fo.write("\n")
		elif (tokens[0] == "END") or (tokens[0] == "end"):
			#some loops use "end for" or "end do" rather than run together
			index = index - 1
			printtabs(fo, index)
			fo.write("\n")	
                elif (tokens[0] == "select") or (tokens[0] == "SELECT"):
                        selector = (tokens[2].split('('))[1].split(')')[0]
                        
                        print selector
                        
                        while "end" not in tokens or "END" not in tokens:
                                codeline = fi.readline()
                                codeline =codeline.strip(" ")
                                tokens = codeline.split(" ")

                                if "end" in tokens or "END" in tokens:
                                        break;
		                elif codeline == "\n":
			                fo.write("\n")
                                                                                
                                elif tokens[0] == "case" or tokens[0] == "CASE":
                                        
                                        if tokens[1] == 'default\r\n' or tokens[1] == 'DEFAULT\r\n':
                                                fo.write("else: \n")
                                                index += 2
                                        else:
                                            
                                                case = (tokens[1].split('('))[1].split(')')[0]
                                            
                                                index += 2
                                            
                                                fo.write("if "+ selector + " == " + case +" :\n")
                                        #check for ranges
                                else:
                                        printtabs(fo, index)
                                        index -= 2
                                        fo.write(codeline + "\n")

                                        #need to check statement
                                        #if it calls a function
                                        #if it does arithmetic
                                        #if it just sets equal to the variable then done
                elif pat_ignore.match(codeline): 
   	                elif pat_ignore.match(codeline): 
                                #declare program 
                                if "PROGRAM" in codeline:
                                        recodeline=codeline.replace("PROGRAM","def") 
                                        print("write this line", recodeline)  
                                        
                                        fo.write(recodeline.strip()) 
                                        fo.write('\n')
                                        index=index+2
                                        
                                elif "program" in codeline:
                                        recodeline=codeline.replace("program","def")
                                        print("write this line", recodeline)   
                                        fo.write(recodeline.strip()) 
                                        fo.write('\n')
                                        index=index+2
                                        #ignore other declaration    
                                else:   
                                        print("ignore this line", codeline)
                                        continue
                                # write assignment
                elif pat_assign_dec.match(codeline):
                        str=codeline.split("::")
                        printtabs(index)
                        printtabs(fo,index)
                        fo.write(str[1].strip())
                        fo.write('\n')
                        continue
                elif pat_declare.match(codeline):
                        continue
                elif pat_assign_one.match(codeline):
                        printtabs(index) 
                        fo.write(codeline.strip())
                        fo.write('\n')
                        continue   
                # write print statement 
                elif pat_print.match(codeline):
                        if "*" in codeline:
                                temptoken=codeline.split("print")
                                tempstr="print("+temptoken[1].replace("*","").replace(",","",1).strip()+")"
                                printtabs(index) 
                                printtabs(fo,index) 
                                fo.write(tempstr.strip())
                                fo.write('\n')
                        else :
                                temptoken=codeline.split("print")
                                tempstr="print("+temptoken[1].strip()+")"
                                printtabs(index)       
                                printtabs(fo,index)       
                                fo.write(tempstr.strip())   
                                fo.write('\n')
