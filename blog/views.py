from django.utils import timezone
from .models import Post
from django.shortcuts import render
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import SendingForm

def post_list(request):
	posts = Post.objects.filter(published_date=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html',  {'posts': posts})
	
def main(request):
	return render(request, 'blog/main.html', {})

def send(request):
    if (request.method == 'POST'):
        form = SendingForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            send_mail(
                '{} {}'.format(name, email),
				'test meassage',
                'diana.omarova2013@gmail.com',
                ['kairatawer@gmail.com', '150106019@stu.sdu.edu.kz'],
                fail_silently=False,
            )
            return render(request, 'blog/result.html', {
                     'name': form.cleaned_data['name'],
			         'email': form.cleaned_data['email'],
				})
    else:
        form = SendingForm()
    return render(request, 'blog/send.html', {'form':form});
