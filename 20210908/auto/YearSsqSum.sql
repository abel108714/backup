DELIMITER ;;
DROP PROCEDURE IF EXISTS getYearSsqSum;
CREATE PROCEDURE getYearSsqSum(IN product_id VARCHAR(255),OUT result VARCHAR(255))
   BEGIN

      DECLARE a INT;
      DECLARE End INT;
      DECLARE sum INT default 0;
#今年
      SET a = 1;
      SET End = month(now())-1;
      simple_loop: LOOP
         select getColumnNameWithIndex('ssq','ssq_index',a) into @ColName;
         SET @select_ssq_colname = CONCAT('SELECT sum(',@ColName,') into @ss FROM ssq where product_id = ',product_id,' and year=year(now())');
         PREPARE ins FROM @select_ssq_colname;
         EXECUTE ins;
         #select @ss;
         IF(@ss IS NULL) THEN
            SET @ss =0;
         END IF;
         select @ss;
         SET sum = sum + @ss;
         select sum;
         IF a=End THEN
            LEAVE simple_loop;
         END IF;
         SET a=a+1;
      END LOOP simple_loop;

#去年
      SET a = End+1;
      #select End;
      simple_loop: LOOP
         select getColumnNameWithIndex('ssq','ssq_index',a) into @ColName;
         SET @select_ssq_colname = CONCAT('SELECT sum(',@ColName,') into @ss FROM ssq where product_id = ',product_id,' and year=year(now())-1');
         PREPARE ins FROM @select_ssq_colname;
         EXECUTE ins;
         #select @ss;
         IF(@ss IS NULL) THEN
            SET @ss =0;
         END IF;
         select @ss;
         SET sum = sum + @ss;
         select sum;
         IF a=12 THEN
            LEAVE simple_loop;
         END IF;
         SET a=a+1;
      END LOOP simple_loop;
      set result=sum;

END
;;
DELIMITER ;