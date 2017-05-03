      program SUBDEM 
      REAL Aa,Bb,Cc,SUM,SUMSQ
      call INPUT()
      end
   	subroutine INPUT()
   	REAL Xx,Yy,Zz
   	print *,'ENTER THREE NUMBERS => '
 	read *,Xx,Yy,Zz
        call CALC(Xx,Yy,Zz)
        return
 	end
 	subroutine CALC(Aa,Bb,Cc)
   	REAL Aa,Bb,Cc,SUM,SUMSQ
   	SUM = Aa + Bb + Cc
   	SUMSQ = SUM **20
        call OUTPUT(SUM,SUMSQ)
   	return
   	end
   	subroutine OUTPUT(SUM,SUMSQ)
   	REAL SUM, SUMSQ
   	print *,'The sum of the numbers you entered are: ',SUM
   	print *,'And the square of the sum is:',SUMSQ
        return
   	end
