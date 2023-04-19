# Web Development with Django

<a href="https://www.packtpub.com/product/web-development-with-django-second-edition/9781803230603?utm_source=github&utm_medium=repository&utm_campaign="><img src="https://content.packt.com/B18654/cover_image_small.jpg" alt="" height="256px" align="right"></a>

This is the code repository for [Web Development with Django](https://www.packtpub.com/product/web-development-with-django-second-edition/9781803230603?utm_source=github&utm_medium=repository&utm_campaign=), published by Packt.

**A definitive guide to building modern Python web applications using Django 4**

## What is this book about?
Do you want to develop reliable and secure applications that stand out from the crowd without spending hours on boilerplate code? You’ve made the right choice trusting the Django framework, and this book will tell you why. Often referred to as a “batteries included” web development framework, Django comes with all the core features needed to build a standalone application. Web Development with Django will take you through all the essential concepts and help you explore its power to build real-world applications using Python.

This book covers the following exciting features:
* Create a new application and add models to describe your data
* Use views and templates to control behavior and appearance
* Implement access control through authentication and permissions
* Develop practical web forms to add features such as file uploads
* Build a RESTful API and JavaScript code that communicates with it
* Connect to a database such as PostgreSQL

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1803230606) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into folders. For example, Chapter02.

The code will look like the following:
```
from django.http import HttpResponse
from django.views import View

class IndexView(View):
    
    def get(self, request):
        return HttpResponse("Hey there!")
```

**Following is what you need for this book:**
This book is for programmers looking to enhance their web development skills using the Django framework. To fully understand the concepts explained in this book, basic knowledge of Python programming as well as familiarity with JavaScript, HTML, and CSS is assumed.

With the following software and hardware list you can run all code files present in the book (Chapter 1-16).
### Software and Hardware List
| Chapter | Software required | OS required |
| -------- | ------------------------------------ | ----------------------------------- |
| 1-16 | Python 3.8 | Windows, macOS, or Linux |
| 1-16 | Django 4.0 | Windows, macOS, or Linux |
| 1-16 | React 16 | Windows, macOS, or Linux |

We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://packt.link/5pZtF).

### Related products
* Becoming an Enterprise Django Developer [[Packt]](https://www.packtpub.com/product/becoming-an-enterprise-django-developer/9781801073639?utm_source=github&utm_medium=repository&utm_campaign=9781801073639) [[Amazon]](https://www.amazon.com/dp/1801073635)

*  Django 4 for the Impatient [[Packt]](https://www.packtpub.com/product/django-4-for-the-impatient/9781803245836?utm_source=github&utm_medium=repository&utm_campaign=9781803245836) [[Amazon]](https://www.amazon.com/dp/1803245832)


## Get to Know the Author
**Ben Shaw** is a software engineer based in Auckland, New Zealand. He has worked as a developer for
over 16 years and has been building websites with Django since 2007. In that time, his experience has
helped many diff erent types of companies, ranging in size from start-ups to large enterprises. He is
also interested in machine learning, data science, automating deployments, and DevOps. When not
programming, Ben enjoys outdoor sports and spending time with his partner and son.

**Saurabh Badhwar** is an infrastructure engineer who works on building tools and frameworks that
enhance developer productivity. A major part of his work involves using Python to develop services
that scale to thousands of concurrent users. He is currently employed at LinkedIn and works on
infrastructure performance tools and services.

**Chris Guest** is based in Melbourne and started programming in Python 24 years ago when it was an
obscure academic language. He has since used his Python knowledge in the publishing, hospitality,
medical, academic, and fi nancial sectors. Th roughout his career, he has worked with many Python
web development frameworks, including Zope, TurboGears, web2py, and Flask, although he still
prefers Django.

**Bharath Chandra K S** is a passionate soft ware developer with over 14 years of experience in the
industry, currently residing in Sydney, Australia. He specializes in Python stack development, including
frameworks such as Flask and Django, and has extensive experience with both monolithic and microservice
architectures. Bharath has developed various public-facing applications and data processing
backend systems. When not creating soft ware, he enjoys cooking delicious food.


## Other books by the authors
[Web Development with Django](https://www.packtpub.com/product/web-development-with-django/9781839212505?utm_source=github&utm_medium=repository&utm_campaign=9781839212505)

[Hands-On Enterprise Application Development with Python](https://www.packtpub.com/product/hands-on-enterprise-application-development-with-python/9781789532364?utm_source=github&utm_medium=repository&utm_campaign=9781789532364)
