from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt


from .serializers import UserSerializer

csrf_exempt
@api_view(['POST'])
def signup(request):
    print('entro')
    print(request.data)  # Para verificar la estructura de los datos recibidos
    serializer = UserSerializer(data=request.data)
    print(serializer.is_valid())  # Para verificar si la serialización es válida
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data})
    return Response(serializer.errors, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response("missing user", status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    return Response({'token': token.key, 'user': serializer.data})

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed!")
  
#
#class UserLogin(APIView):
#    def post(self, request, format=None):
#        serializer = UserSerializer(data=request.data)
#        if serializer.is_valid():
#            username = serializer.validated_data['username']
#            password = serializer.validated_data['password']
#            user = authenticate(username=username, password=password)
#            if user:
#                token, created = Token.objects.get_or_create(user=user)
#                return Response({'token': token.key}, status=status.HTTP_200_OK)
#            else:
#                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Class based view to Get User Details using Token Authentication


#class UserDetailAPI(APIView):
#  authentication_classes = (TokenAuthentication,)
#  permission_classes = (AllowAny,)
#  def get(self,request,*args,**kwargs):
#    user = User.objects.get(id=request.user.id)
#    serializer = UserSerializer(user)
#    return Response(serializer.data)

#Class based view to register user
#class RegisterUserAPIView(generics.CreateAPIView):
#  permission_classes = (AllowAny,)
#  serializer_class = RegisterSerializer
  
# Create your views here.
