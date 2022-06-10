DELIMITER ;;
DROP PROCEDURE IF EXISTS checkGroup;
CREATE PROCEDURE checkGroup(IN customercode VARCHAR(255), IN groupname BLOB(255), OUT result VARCHAR(255))BEGIN

	SELECT IFNULL( (select (CASE WHEN customer_code IS NULL THEN 0 ELSE 1 END) from cu where customer_code=customercode and group_name=groupname) ,'0');

END
;;
DELIMITER ;