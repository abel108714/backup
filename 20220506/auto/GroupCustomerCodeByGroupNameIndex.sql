DELIMITER ;;
DROP PROCEDURE IF EXISTS getGroupCustomerCodeByGroupNameIndex;
CREATE PROCEDURE getGroupCustomerCodeByGroupNameIndex(IN groupname BLOB(255),IN rownumber INT(255),OUT result VARCHAR(255))BEGIN
	DECLARE a INT;
	DECLARE customercode VARCHAR(255);
	SELECT 
	    customer_code into customercode
	FROM
		(SELECT 
			*
		FROM
			cu where group_name=groupname
		ORDER BY customer_code ASC limit 1,rownumber
		) AS tbl
	ORDER BY customer_code DESC
	LIMIT 1; 
	select customercode;
END
;;
DELIMITER ;