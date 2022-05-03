from manage_panel.models import Line
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.shortcuts import redirect

def line(request):
	line = Line.objects.all()
	line_id = Line._meta.get_field('line_id').column
	name = Line._meta.get_field('name').column
	permission_name = Line._meta.get_field('permission_name').column
	datetime = Line._meta.get_field('datetime').column
	retrun render_to_response('Line.html',locals())

#CREATE Table line(
#	line_id varchar(255) character set utf8 NOT NULL, #line id
#	name varchar(50) character set utf8, #名字
#	permission_name varchar(50) character set utf8, #權限名稱
#	datetime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, #資料儲存時間
#	PRIMARY KEY (line_id) #設定主鍵
#)ENGINE = InnoDB;
	
