for f in */ ; 
	do 
	
	cd ${f} ; 
	 find . -name *.py -exec sed -i "s/init_no = 0 /init_no = 3 /g" {} +
	
	cd ../ ; 
done
