DELIMITER ;;
DROP PROCEDURE IF EXISTS insertAmsData;
CREATE PROCEDURE insertAmsData(OUT result VARCHAR(255))BEGIN

   

   DECLARE a INT;
   DECLARE End INT;
   truncate table ams;   
	
   #select id;
   #call getYearSaleAvg(id,@YearSaleAvg);
   #select @YearSaleAvg;
   #INSERT AMS (id,avg_mon_sales_for_a_year) VALUES(id,@YearSaleAvg);

   SET a = (select distinct product_id from inv order by product_id asc limit 1);
   #set a= 11506001;
   SET End = (select distinct product_id from inv order by product_id desc limit 1);
   simple_loop: LOOP

      IF (select distinct product_id from inv where product_id=a limit 1) THEN
          select a;
          call getYearSaleAvg(a,@YearSaleAvg);
          select @YearSaleAvg;
          INSERT AMS (id,avg_mon_sales_for_a_year) VALUES(a,@YearSaleAvg);
      END IF;

      #IF(a IS NOT NULL) and (select product_id from inv where id=a) THEN
      #    select a;
      #END IF;
      IF a=End THEN
         LEAVE simple_loop;
      END IF;
      SET a=a+1;
   END LOOP simple_loop;

END
;;
DELIMITER ;