-- Lists all bands with Glam rock as their style,
-- ranked by their longevity
-- Column names must be: band_name & lifespan

SELECT band_name, 
       (YEAR('2022-01-01') - CAST(SUBSTRING_INDEX(formed, '-', 1) AS UNSIGNED)) AS lifespan
FROM bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;

