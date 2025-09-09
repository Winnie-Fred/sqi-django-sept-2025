from django.shortcuts import render

# Create your views here.

services_pricing = {
    "Logo design": 50_000,
    "UI/UX": 400_000,
    "Web Development": 600_000,
    "Cybersecurity": 1_000_000
}

def services(request):
    return render(request, "portfolio/services.html", {"services": services_pricing.keys()})


def testimonials(request):
    customer_testimonials = {
        "Alice Johnson": "This product exceeded my expectations! The support team was also fantastic.",
        "Michael Smith": "Very reliable and easy to use. I recommend it to all my colleagues.",
        "Sophia Martinez": "The customer service is top-notch, and the software works flawlessly.",
        "David Lee": "Affordable and efficient. It has streamlined our daily operations significantly.",
        "Emily Brown": "I was skeptical at first, but now I can't imagine working without it."
    }
    return render(request, "portfolio/testimonials.html", context={'testimonials': customer_testimonials})


def pricing(request):
    context = {'pricing': services_pricing}
    return render(request, "portfolio/pricing.html", context)


def blog(request):
    return render(request, "portfolio/blog.html")

def case_studies(request):
    return render(request, "portfolio/case-studies.html")
