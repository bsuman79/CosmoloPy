import cosmolopy.growth_ode  as Dode


zseek= 0.5 #float(sys.argv[1])  # redshift
Om= 0.25  #float(sys.argv[2])   #Omega_m
Ol=1-Om
wt= -1  #float(sys.argv[3])   #dark energy EOS

scalefac, D0, D1=Dode.Da_ode(Om,Ol, wt)
Ds, lDs= Dode.interp_D(zseek,scalefac,D0, D1)
print "redshift D(z) dlog D/d log a (z)"
print zseek, Ds, lDs

Dode.plot_growth(scalefac, D0, D1)
