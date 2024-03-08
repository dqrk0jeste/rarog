/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE DEFINER=`urosm`@`localhost` PROCEDURE `createMovie`(
    IN name VARCHAR(255),
    IN releaseYear INT,
    IN genre VARCHAR(255),
    IN director VARCHAR(255),
    IN `cast` TEXT,
    IN `length` INT,
    IN description TEXT,
    IN screenwriters VARCHAR(255)
)
BEGIN
	DECLARE mediaId VARCHAR(32);
    DECLARE movieId VARCHAR(32);
    DECLARE movieCategory VARCHAR(32);
    
	SET mediaId = REPLACE(UUID(), '-', '');
	SET movieId = REPLACE(UUID(), '-', '');
	SET movieCategory = "d203540115204ab784a530cb0e450dcf";
	
    INSERT INTO example_media (mediaId, name, releaseYear, genre, categoryId_id)
    VALUES (mediaId, name, releaseYear, genre, movieCategory);
	
	INSERT INTO example_movie(movieId, director, `cast`, `length`, description, screenwriters, mediaId_id)
    VALUES (movieId, director, `cast`, `length`, description, screenwriters, mediaId);
    
    SELECT mediaId, movieId;
END;



/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;