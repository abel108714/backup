DELIMITER ;;
DROP PROCEDURE IF EXISTS getYearSaleAvg;
CREATE PROCEDURE getYearSaleAvg(IN id VARCHAR(255))
BEGIN

	call getYearSqSum(id,@YearSqSum);
	call getYearSsqSum(id,@YearSsqSum);
	#select @YearSqSum;
	#select @YearSsqSum;
	select (@YearSqSum+@YearSsqSum)/12;

END;
;;
DELIMITER ;


