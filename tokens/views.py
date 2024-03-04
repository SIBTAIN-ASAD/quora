'''
This file is used to handle api views request in tokens app
Using simplejwt for authentication
'''

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from .models import UserRatingComment
from .commons import encrypt, decrypt

class JWTLoginView(APIView):
    '''
    View to authenticate user and return JWT tokens
    '''
    def post(self, request):
        '''
        Post request with username and password
        '''
        username = request.data.get('username')
        password = request.data.get('password')

        print(username, password)

        # Authenticate user
        user = authenticate(username=username, password=password)
        if user:
            # If user is authenticated, generate JWT tokens
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            # Return tokens in response
            return Response({
                'access_token': access_token,
                'refresh_token': refresh_token,
            }, status=status.HTTP_200_OK)
        else:
            # If authentication failed, return error message
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class HomeView(APIView):
    '''
    View to test authentication
    '''
    permission_classes = [IsAuthenticated]

    def get(self, request):
        '''
        Get request to test authentication
        '''

        if request.user.is_anonymous:
            return Response({'error': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

        if request.user.profilePicture:
            profilePicture = request.user.profilePicture.url
        else:
            profilePicture = 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png'

        content = {'message': 'Welcome to the JWT Authentication page using React Js and Django!',
                   'name': str(request.user.first_name) + ' ' + str(request.user.last_name),
                    'email': str(request.user.email),
                    'username': str(request.user.username),
                    'profilePicture': str(profilePicture)
        }
                    

        return Response(content)

class LogoutView(APIView):
    '''
    View to logout user and blacklist refresh token
    '''
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        '''
        Post request to logout user and blacklist refresh token
        '''
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# ------------------------------------------------------------------
# Practicing encryption and decryption
# ------------------------------------------------------------------
class UserRatingCommentView(APIView):
    '''
    View to handle user rating and comments
    it will use encryption and decryption in various ways
    '''
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        '''
        Post request to save user rating and comments
        '''
        user = request.user
        rating = request.data.get('rating')
        comment = request.data.get('comment')
        review = request.data.get('review')
        catalog = request.data.get('catalog')
        comment_type = request.data.get('comment_type')

        # Save user rating and comments
        userRatingComment = UserRatingComment.objects.create(user=user, 
                            rating=encrypt(rating), # Manual encryption
                            comment=comment,
                            review=review, 
                            catalog=catalog, 
                            comment_type=comment_type)
        userRatingComment.save()

        return Response(status=status.HTTP_201_CREATED)
    
    def get(self, request):
        '''
        Get request to get user rating and comments
        '''
        user = request.user
        userRatingComment = UserRatingComment.objects.filter(user=user)

        # Decrypt user rating
        for userRating in userRatingComment:
            userRating.rating = decrypt(userRating.rating) # Manual decryption

        # Return user rating and comments
        return Response({
            'userRatingComment': userRatingComment.values()
        }, status=status.HTTP_200_OK)

    def delete(self, request):
        '''
        Delete request to delete user rating and comments
        '''
        id = request.data.get('id')  # Retrieve id from the request body

        # Delete user rating and comments
        userRatingComment = UserRatingComment.objects.filter(id=id).delete()

        return Response(status=status.HTTP_200_OK)

    def put(self, request):
        '''
        Put request to update user rating and comments
        '''
        user = request.user
        rating = request.data.get('rating')
        comment = request.data.get('comment')
        review = request.data.get('review')
        catalog = request.data.get('catalog')
        comment_type = request.data.get('comment_type')

        # Update user rating and comments
        userRatingComment = UserRatingComment.objects.filter(user=user).update(
                            rating=encrypt(rating), # Manual encryption
                            comment=comment,
                            review=review, 
                            catalog=catalog, 
                            comment_type=comment_type)

        return Response(status=status.HTTP_200_OK)
# ------------------------------------------------------------------
# ------------------------------------------------------------------
