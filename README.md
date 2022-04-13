#  Get_movies 
Output movies by their rating with optional filters.
## Optional arguments

	-h, --help            												show help message and exit
	-N  		<int>	for file:	reducer.py							number of top-rated movies 
	-genres	    <str>	for file:	mapper.py							filter by genre, can be multiple.
	-year_from  <int>	for file:	mapper.py							year from which the films were released
	-year_to    <int>   for file:   mapper.py 							year before which the films were released 
	-regexp     <str>  	for file: 	mapper.py							filter (regular expression) on the movie title. 

## Running a single app

To run the app local:


> sh get\_movies_local.sh

To run the app this hadoop:

> sh get\_movies_local.sh

## Application configuration

To configure the application run any text editor and open the executable file of the application that you plan to compete with.Then add parameters like when u calling a console application

For example:

Open file
 
> vi get\_movies_local.sh

Edit:

> cat movies.csv | python3 mapper.py -genres "IMAX" | sort | python3 reducer.py -N 3

And close saving changes:

> :wq