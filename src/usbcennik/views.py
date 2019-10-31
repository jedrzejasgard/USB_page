from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf


def home_page(request):
	return render(request,'base.html')

def edycja_cen(request):
	return render(request,'edytuj_ceny.html')

class GeneratePDF(View):
	def get(self, request, *args , **kwargs):
		template = get_template('cennikUSB.html')
	
		context = {
			'index': '19340' ,
			'cena' : '12,40' ,
			'data' : '12-30-2012'
		}

		html = template.render(context)
		pdf = render_to_pdf('cennikUSB.html', context)
		if pdf:
			response = HttpResponse(pdf, content_type='application/pdf')
			filename = "Cennik_USB.pdf"
			content = 'inline; filename="%s"' %(filename)			
			download = request.GET.get('download')
			if download:
				content = 'attachment; filename="%s"' %(filename)
			response['Content-Disposition'] = content
			return response
		return HttpResponse('Coś poszło nie tak i PDF się nie wygenerował')