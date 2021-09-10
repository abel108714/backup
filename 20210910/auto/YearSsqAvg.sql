DELIMITER ;;
DROP PROCEDURE IF EXISTS getYearSsqAvg;
CREATE PROCEDURE getYearSsqAvg(id VARCHAR(255))
BEGIN

	call getYearSsqSum(id,@YearSsqSum);
	select @YearSsqSum/12;

END;
;;
DELIMITER ;


