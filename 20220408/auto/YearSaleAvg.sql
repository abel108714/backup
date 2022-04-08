DELIMITER ;;
DROP PROCEDURE IF EXISTS getYearSaleAvg;
CREATE PROCEDURE getYearSaleAvg(IN id VARCHAR(255),OUT result VARCHAR(255))
BEGIN
	select id;	
	call getYearSqSum(id,@YearSqSum);
	select @YearSqSum;
	call getYearSsqSum(id,@YearSsqSum);
	select @YearSsqSum;
	set result=(select (@YearSqSum+@YearSsqSum)/12);
END;
;;
DELIMITER ;


