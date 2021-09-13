DELIMITER ;;
DROP PROCEDURE IF EXISTS insertAmsData;
CREATE PROCEDURE insertAmsData(OUT result VARCHAR(255))BEGIN

   DECLARE a INT;
   DECLARE End INT;


   #select id;
   #call getYearSaleAvg(id,@YearSaleAvg);
   #select @YearSaleAvg;
   #INSERT AMS (id,avg_mon_sales_for_a_year) VALUES(id,@YearSaleAvg);

   SET a = (select distinct product_id from inv order by product_id asc limit 1);
   SET End = (select distinct product_id from inv order by product_id desc limit 1);
   simple_loop: LOOP

      #IF(@ss IS NULL) THEN
      #    SET @ss =0;
      #END IF;
      select a;
      IF(@ss IS NULL) THEN
          SET @ss =0;
      END IF;

      IF a=End THEN
         LEAVE simple_loop;
      END IF;
      SET a=a+1;
   END LOOP simple_loop;

END
;;
DELIMITER ;