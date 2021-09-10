DELIMITER ;;
DROP PROCEDURE IF EXISTS getYearSqAvg;
CREATE PROCEDURE getYearSqAvg(IN id VARCHAR(255))
BEGIN

	call getYearSqSum(id,@YearSqSum);
	select @YearSqSum/12;

END;
;;
DELIMITER ;


