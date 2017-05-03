      program functions
      real Aa,Bb,Cc
      real AV, AVSQ1, AVSQ2
      real AVRAGE
      data Aa,Bb,Cc/5.0,2.0,3.0/
      AV = AVRAGE(Aa,Bb,Cc)
      AVSQ1 = AVRAGE(Aa,Bb,Cc) **2
      AVSQ2 = AVRAGE(Aa**20,Bb**10,Cc**30)
      print *,'Statistical Analysis'
      print *,'The average of the numbers is:',AV
      print *,'The average squared of the numbers: ',AVSQ1
      print *,'The average of the squares is: ', AVSQ2
      end
     real function AVRAGE(Xx,Yy,Zz)
     real Xx,Yy,Zz,SUM
     SUM = Xx + Yy + Zz
     AVRAGE = SUM /3.0
      return
     end
