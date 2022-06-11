DELIMITER ;;

use invdb
set character_set_client=utf8;
set character_set_connection=big5;
set @this_year=year(now());
set @this_month=month(now());
call getMonGroupSqSum('聯盟',@this_year,@this_month,@result);
call getMonGroupSqSum('實通團購',@this_year,@this_month,@result);
call getMonGroupSqSum('流通連鎖',@this_year,@this_month,@result);
call getMonGroupSqSum('電購',@this_year,@this_month,@result);
call getMonGroupSqSum('網路',@this_year,@this_month,@result);

;;
DELIMITER ;
