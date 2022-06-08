from ma.models import Line
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.shortcuts import redirect


def linedata(request):
	linedata=Line.objects.all()
	lineid=Line._meta.get_field('line_id').column
	return render_to_response('linedata.html',local())