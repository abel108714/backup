DELIMITER ;;
DROP PROCEDURE IF EXISTS getMonGroupSqSum;
CREATE PROCEDURE getMonGroupSqSum(IN groupname BLOB(255),IN year VARCHAR(255),IN month VARCHAR(255),OUT result VARCHAR(255))BEGIN

	DECLARE a INT;
	DECLARE End INT;
	DECLARE sum INT default 0;
	DECLARE customercode VARCHAR(255);
	DECLARE s INT(255) default 0;
	DECLARE stm VARCHAR(255);
	SET a = 1;
	select count(customer_code) into End from cu where group_name=groupname;
	select End;
	SET @row_number = 0;
	select 'Calculating...' as '';
	simple_loop: LOOP

		SELECT 
		    customer_code into customercode
		FROM
			(SELECT 
				*
			FROM
				cu where group_name=groupname
			ORDER BY customer_code ASC limit 1,a
			) AS tbl
		ORDER BY customer_code DESC
		LIMIT 1; 
		
		select customercode;

	IF day(now())=1 THEN #今日為本月1日，清除本月銷售量欄位
		#select '今日為本月1日，清除本月銷售量欄位';
		UPDATE CU SET sales_this_month = NULL where customer_code=customercode;
		select ( @row_number := @row_number + 1 ) AS num;
	ELSEIF day(now())>1 THEN #今日非本月1日，則開始計算
		select sales_this_month into stm FROM cu where customer_code=customercode;
		#select stm;
		IF stm is NULL THEN #本月銷售量為空，則本月計算全部加總
			SELECT sum(sales_quantity) into s FROM sq where year(sale_date)=(select year(now())) and month(sale_date)=(select month(now())) and customer_code=customercode;
			#select 'case1';
			#select s;
			UPDATE CU SET sales_this_month = s where customer_code=customercode;
			#select ( @row_number := @row_number + 1 ) AS num;
		ELSE #本月銷售量不為空，則計算本月銷售量加今日加總，(比對不等於儲存日期避免重覆加總)
			#select 'case2';
			SELECT sum(sales_quantity) into s FROM sq where year(sale_date)=(select year(now())) and month(sale_date)=(select month(now())) and day(sale_date)=(select day(now())) and customer_code=customercode;
			SELECT sales_this_month into stm FROM cu where customer_code=customercode;

			set stm=stm+s;
			#select stm;
			UPDATE CU SET sales_this_month = stm where customer_code=customercode;
			#select ( @row_number := @row_number + 1 ) AS num;
		END IF;
	ELSE
		select 'ELSE';
	END IF;
 
	IF a=End THEN
		LEAVE simple_loop;
	END IF;
	SET a=a+1;
	END LOOP simple_loop;
	select 'Done!';

END
;;
DELIMITER ;