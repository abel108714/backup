DELIMITER ;;
DROP PROCEDURE IF EXISTS getMonSqSum;
CREATE PROCEDURE getMonSqSum(IN product_id VARCHAR(255),IN year VARCHAR(255),IN month VARCHAR(255),OUT result VARCHAR(255))BEGIN

   select sum(sales_quantity) into @result from sq where id=product_id and year(sale_date)=year and month(sale_date)=month;
   #select @result;

END
;;
DELIMITER ;