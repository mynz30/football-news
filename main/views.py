from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm': '2406436335',     # ganti dengan NPM kamu
        'name': 'Faishal Khoiriansyah Wicaksono',  # ganti dengan nama kamu
        'class': 'PBP D'         # ganti dengan kelas kamu
    }

    return render(request, "main.html", context)
