from manage_panel.models import Line
from django.shortcuts import render_to_response
from django.shortcuts import render
#from django.shortcuts import redirect

import sys




def line(request):
	modulename = 'manage_panel.models'
	if modulename not in sys.modules:
		print("You have not imported the {} module".format(modulename))
	data = Line.objects.all()
	line_id = Line._meta.get_field('line_id').column
	name = Line._meta.get_field('name').column
	permission_name = Line._meta.get_field('permission_name').column
	datetime = Line._meta.get_field('datetime').column
	#print("line_id: "+line_id)
	#line_id=request.GET['line_id']
	# name = Line._meta.get_field('name').column
	# permission_name = Line._meta.get_field('permission_name').column
	# datetime = Line._meta.get_field('datetime').column
	return render_to_response('Line.html',locals())
	#return render('Line.html',locals())
	#context = {line_id}
	#return render('none',request,"Line.html",context)

#CREATE Table line(
#	line_id varchar(255) character set utf8 NOT NULL, #line id
#	name varchar(50) character set utf8, #�W�r
#	permission_name varchar(50) character set utf8, #�v���W��
#	datetime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, #����x�s�ɶ�
#	PRIMARY KEY (line_id) #�]�w�D��
#)ENGINE = InnoDB;

# def do_insert(request):
# 	line_id=request.POST['line_id']
# 	Line.objects.create(line_id=line_id)
# 	return render(request,'go_line.html')

	
