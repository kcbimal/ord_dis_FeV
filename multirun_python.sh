for f in */ ; 
	do 
	
	cd ${f} ; 
	 python *.py -e screen
	
	cd ../ ; 
done
