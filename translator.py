#!/usr/bin/python
import re
import sys

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
linecount = 0;
#libraries = {"datetime-fortran":"datetime",  }

#match the codeline whose key word do not know how to manage
pat_ignore=re.compile(r"\s*USE|use|MODULE|module|IMPLICIT|implicit|program|PROGRAM|!\s*\.*")
 #match the codeline whose declaration without assigning value
pat_declare=re.compile(r"\s*\S*\s*::\s*")
 #match the codeline whose declaration with assigning value
pat_assign_dec=re.compile(r".*::.*=.*")
#match the codeline whose assigning one value
pat_assign_one=re.compile(r'\s*\w+\s*=\s*("(.*)"|\w*.|\w*)\s*\w*\s*') 
 #match the codeline include print statement
pat_print=re.compile(r'print|PRINT|Print\s*(,)\w*')


fo = open("program.py", 'w')

#getting the line and splitting it into tokens

with open("program.f90",'rb') as fi:

        #re.compile()
	while True:
        	line = fi.readline()
		if not line: break #exit while read loop if line not read
		linecount = linecount +1 #track line number for error messages
		# check for gotos, currently not supported
		if ("goto" in line) or ("GOTO" in line):
			print "Goto detected in line " + linecount + ".  Translation terminating.\n"
			fo.write("TRANSLATION HALTED ON LINE " + linecount + ". 'GOTO' is not supported\n")
			sys.exit()
		#check for comments
		if ("!" in line) and (line[0] != "!"): #if there is code and a comment on same line
			line.split("!")
			codeline = line[0]
			comments = line[1]
		else:
			codeline = line
                codeline =codeline.strip(" ")
                tokens = codeline.split(" ")

                #special line types
		if codeline == "\n": #if blank line
			fo.write("\n")
		elif (codeline[0] == "!"): # if whole line is comment
			printtabs(fo, index)
			fo.write("#" + codeline + "\n")
		elif (codeline == "end\n") or (codeline == "END\n"): #if end of program
			fo.write("# script ends")
		#if statements
		elif (tokens[0] == "IF") or (tokens[0] == "if"):
			printtabs(fo, index)
			fo.write("if")
			counter = 1
			while (codeline[counter] != "THEN") and (codeline[counter] != "then") and (codeline[counter] != "EXIT") and (codeline[counter] != "exit"):
				if (codeline[counter] == ".AND."):
					fo.write("and ")
				elif (codeline[counter] == ".OR."):
					fo.write("or ")
				elif (codeline[counter] == ".EQV."):
					fo.write("!xor ")
				elif (codeline[counter] == ".NEQV."):
					fo.write("xor ")
				elif (codeline[counter] == ".NOT."):
					fo.write("!")
				else:
					fo.write(codeline[counter] + " ")
				counter = counter + 1
			if (codeline[counter] == "THEN") or (codeline[counter] == "then"):
				fo.write(":")
			        index = index + 1 #whatever follows must be indented
			elif (codeline[counter] == "EXIT") or (codeline[counter] == "exit"):
				fo.write(": break")
				#the next line will not be indented as the if block ends

		elif (tokens[0] == "EXIT") or (tokens[0] == "exit"):
			printtabs(fo, index)
			fo.write("break")
		elif (tokens[0] == "CONTINUE") or (tokens[0] == "continue"):
			printtabs(fo, index)
			fo.write("continue")
		elif ((tokens[0] == "ELSE") or (tokens[0] == "else")) and ((tokens[1] == "IF") or (tokens[1] == "if")):
			index = index - 1
			printtabs(fo, index)
			fo.write("elif ")
			counter = 2
			while (codeline[counter] != "THEN") and (codeline[counter] != "then") and (codeline[counter] != "EXIT") and (codeline[counter] != "exit"):
				if (codeline[counter] == ".AND."):
					fo.write("and ")
				elif (codeline[counter] == ".OR."):
					fo.write("or ")
				elif (codeline[counter] == ".EQV."):
					fo.write("!xor ")
				elif (codeline[counter] == ".NEQV."):
					fo.write("xor ")
				elif (codeline[counter] == ".NOT."):
					fo.write("!")
				else:
					fo.write(codeline[counter] + " ")
				counter = counter + 1
			if (codeline[counter] == "THEN") or (codeline[counter] == "then"):
				fo.write(":")
				index = index + 1
			elif (codeline[counter] == "EXIT") or (codeline[counter] == "exit"):
				fo.write(": break")
				# the next line will not be indented as the if block ends
		elif (tokens[0] == "ENDIF") or (tokens[0] == "endif"):
			index = index - 1
			printtabs(fo, index)
		#do loops
		elif (tokens[0] == "DO") or (tokens[0] == "do"):
			printtabs(fo, index)
			fo.write("for "+ tokens[2] + " in range(" + tokens[4]+ tokens[5] + "):")
			index = index + 1
		elif (tokens[0] == "ENDDO") or (tokens[0] == "enddo"):
			index = index - 1
			printtabs(fo, index)
		elif (tokens[0] == "END") or (tokens[0] == "end"):
			#some loops use "end if" or "end do" rather than run together
			index = index - 1
			printtabs(fo, index)	
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
                                        
                                        if tokens[1] == 'default\r\n' or tokens[1] == 'DEFAULT\r':
                                                fo.write("else: ")
                                                index += 2
                                        else:
                                            
                                                case = (tokens[1].split('('))[1].split(')')[0]
                                            
                                                index += 2
                                            
                                                fo.write("if "+ selector + " == " + case +" :")
                                        #check for ranges
                                else:
                                        printtabs(fo, index)
                                        index -= 2
                                        fo.write(codeline)

                                        #need to check statement
                                        #if it calls a function
                                        #if it does arithmetic
                                        #if it just sets equal to the variable then done
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
                        printtabs(fo,index)
                        fo.write(str[1].strip())
                        continue
                elif pat_declare.match(codeline):
                        continue
                elif pat_assign_one.match(codeline):
                        printtabs(index) 
                        fo.write(codeline.strip())
                        continue   
                # write print statement 
                elif pat_print.match(codeline):
                        if "*" in codeline:
                                temptoken=codeline.split("print")
                                tempstr="print("+temptoken[1].replace("*","").replace(",","",1).strip()+")"
                                printtabs(fo,index) 
                                fo.write(tempstr.strip())
                        else :
                                temptoken=codeline.split("print")
                                tempstr="print("+temptoken[1].strip()+")"
                                printtabs(fo,index)       
                                fo.write(tempstr.strip())
				
		#EOL comment printing
		if comments in locals(): #if there was a comment set
			fo.write(" #" + comments + "\n")
		else:
			fo.write("\n")
