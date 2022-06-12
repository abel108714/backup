DELIMITER ;;
DROP PROCEDURE IF EXISTS getYearSqSum;
CREATE PROCEDURE getYearSqSum(IN product_id VARCHAR(255),OUT result VARCHAR(255))
   BEGIN

      DECLARE a INT;
      DECLARE End INT;
      DECLARE sum INT default 0;

#今年
      SET a = 1;
      SET End = month(now())-1;
      simple_loop: LOOP
         #select a;
         call getMonSqSum(product_id,year(now()),a,@MonSqSum);
         SET @result =IFNULL(@result, 0);
         SET sum = sum+@result;
         #select sum;
         IF a=End THEN
            LEAVE simple_loop;
         END IF;
      SET a=a+1;
      END LOOP simple_loop;

#去年
      SET a = End+1;
      simple_loop: LOOP
         #select a;      
         call getMonSqSum(product_id,year(now())-1,a,@MonSqSum);
         SET @result =IFNULL(@result, 0);
         SET sum = sum+@result;
         #select sum;
         IF a=12 THEN
            LEAVE simple_loop;
         END IF;
         SET a=a+1;
      END LOOP simple_loop;
      set result=sum;
   
END
;;
DELIMITER ;