/* Question 1:
We want to understand more about the movies that families are watching. 
The following categories are considered family movies: Animation, Children, Classics, Comedy, Family and Music.
Create a query that lists each movie, the film category it is classified in, and the number of times it has been rented out. 
*/

/* I've altered the name of the columns to match the solution shown on the UDACITY classroom using Code below*/
/* Please use the below commands before running the code*/


/*ALTER TABLE film 
RENAME COLUMN title TO film_title;*/
/*ALTER TABLE category 
RENAME COLUMN name TO category_name;*/

WITH family_movies AS (SELECT f.film_title,
       c.category_name,
       COUNT(r.rental_id) AS Rental_Count
  FROM category AS c
       JOIN film_category AS fc
        ON c.category_id = fc.category_id
        AND c.category_name IN ('Animation', 'Children', 'Classics', 'Comedy', 'Family', 'Music')

       JOIN film AS f
        ON f.film_id = fc.film_id

       JOIN inventory AS i
        ON f.film_id = i.film_id

       JOIN rental AS r
        ON i.inventory_id = r.inventory_id
 GROUP BY 1, 2
 ORDER BY 2, 1)
 
 /*The above table lists lists each movie, the film category it is classified in, and the number of times it has been rented out and To view it please use the code below*/
 
 /* SELECT *
	FROM family_movies*/
	
/*TO KNOW THE TOTAL NUMBER OF MOVIES UNDER EACH CATEGORY OF FAMILY MOVIE, I'VE USED THE BELOW CODE*/


SELECT family_movies.category_name, count(family_movies.category_name),SUM(family_movies.rental_count) as total_rental_count
FROM family_movies
GROUP BY 1
   
   


	