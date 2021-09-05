from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from rest_framework import status
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from .serializers import CreateUserSerializer

User = get_user_model()


# Through this view user can get JWT for being authorized
class LoginUserView(APIView):

    def post(self, request, *args, **kwargs):
        user = authenticate(email=request.data['email'], password=request.data['password'])
        if user is not None:
            token = RefreshToken.for_user(user=user)
            res = {
                'email': user.email,
                'refresh': str(token),
                'access_token': str(token.access_token)
            }
            return Response(data=res, status=status.HTTP_200_OK)
        else:
            return Response(data={'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)


# This view create a normal user with email and password neither a student or teacher just a registered user.
# To register student and teacher please look up in those apps.
class CreateUserView(CreateAPIView):
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()

    def finalize_response(self, request, response, *args, **kwargs):
        response.data['password'] = ''
        return super(CreateUserView, self).finalize_response(request, response, *args, **kwargs)


class PasswordResetBeginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data['email']
        if User.objects.filter(email=email).exists():
            # send a token and password reset endpoint in mail.
            # Currently I am using console email as settings.py
            # if required we can customize the password-reset templates.
            user = User.objects.get(email=email)
            context = {
                "email": email,
                "domain": "localhost:8000",
                "site_name": "Localhost",
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "user": user,
                "token": default_token_generator.make_token(user),
                "protocol": "http",
            }

            render_email = render_to_string('passwordReset.txt', context)
            send_mail("Password Reset", render_email, 'admin@example.com', [user.email], fail_silently=False)
            return Response(data={'message': 'An email has been send to your registered email address.'})
        else:
            return Response(data={'error': 'No registered account found with this email'})
