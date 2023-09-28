for f in */ ; 
	do 
	
	cd ${f} ; 
	 phonopy -p -s mesh.conf
	
	cd ../ ; 
done
