from django.shortcuts import render, redirect
from LoginPages.models import signupdata
from django.contrib.auth import authenticate
from django.core.mail import send_mail

def login(request):
    """
    This function handles the login process for a user. It collects user details, validates the contact number,
    saves the user data to the database, and sends a welcome email.

    Parameters:
    request (HttpRequest): The request object containing the user's input data.

    Returns:
    HttpResponse: The rendered login page if the request method is not POST.
    HttpResponse: The rendered signup page with an error message if the contact number is invalid.
    HttpResponse: The rendered signup page with an error message if the email is already registered.
    HttpResponse: The rendered login page with the user's data stored in the dictionary.
    """
    dictionary = {}
    if request.method == 'POST':
        full_name = request.POST.get('name')
        username = request.POST.get('username')
        email_id = request.POST.get('email')
        contact = request.POST.get('num')
        password = request.POST.get('pass')
        """ validate contact number """
        if not contact.isdigit() or len(contact)!=10:
            return render(request, 'signup.html', {'error': 'Invalid contact number'})
        try:
            data = signupdata(full_name=full_name, username=username, email_id=email_id, contact=contact, password=password)
            data.save()
        except Exception as e:
            return render(request,'signup.html',{'error': 'Email already registered'})
        """ subject = 'Welcome to our Platform'
        message = 'Thank you for signing up.'
        from_email='vibhanshujaiswal28@gmail.com'
        to_email = email_id
        send_mail(subject, message, from_email, [to_email]) """

        dictionary = {'key':data}
    return render(request, 'login.html')

def signup(request):
    """
    This function handles the signup view for a new user. It renders the signup page.

    Parameters:
    request (HttpRequest): The request object containing the user's input data. This function is expected to be called when a user navigates to the signup page.

    Returns:
    HttpResponse: The rendered signup page. This page contains a form for the user to enter their details for registration.
    """
    return render(request, 'signup.html')


def forgetpass(request):
    return render(request, 'forgetpass.html')

def dashboard(request):
    """
    This function handles the dashboard view for a logged-in user. It retrieves the user's username and password from the POST request,
    queries the database to check if the user exists, and renders the dashboard page with the user's data.

    Parameters:
    request (HttpRequest): The request object containing the user's input data. The data is expected to be sent as a POST request with 'username' and 'pass' fields.

    Returns:
    HttpResponse: The rendered dashboard page with the user's data stored in the dictionary.
    HttpResponseRedirect: A redirect to the home page if the user does not exist in the database.
    """

    email = request.POST.get('email')
    pswd = request.POST.get('pass')
    obj = signupdata.objects.filter(email_id=email, password=pswd )
    
    """ if request.method == 'POST':
        uname = request.POST.get('username')
        pswd = request.POST.get('pass')
        user = authenticate(username=uname, password=pswd)
        print(user)
        if user:
            return redirect('dashboard')
        else:
            return redirect('/')
    if obj.password == request.POST.get('pass'):
        return redirect(dashboard) """
    if obj:
        data = {'key':obj}
        a = data['key']
        x = []
        for i in a:
            x.append(i.full_name)
            x.append(i.username)
            x.append(i.email_id)
            x.append(i.contact)
        return render(request, 'dashboard.html',{'key':x})
    else:
        return redirect('/')
    