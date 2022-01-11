from django.shortcuts import render
from .models import Payment

# Create your views here.


def payment(request):
	context ={
		'payments' : Payment.objects.all()
	}
	return render(request, 'payment/payment.html', context)