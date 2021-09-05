DELIMITER ;;
DROP PROCEDURE IF EXISTS getYearSsqAvg;
CREATE PROCEDURE getYearSsqAvg(id VARCHAR(255))
BEGIN

	call getYearSsqSum(id,@ContactType);
	select @ContactType/12;

END;
;;
DELIMITER ;


