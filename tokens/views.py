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

from tokens.models import UserRatingComment
from tokens.commons import encrypt, decrypt
from tokens.serializers import UserRatingCommentSerializer

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
            return Response({'error': 'User not authenticated'},
                            status=status.HTTP_401_UNAUTHORIZED)

        if request.user.profilePicture.url:
            profile_picture = request.user.profilePicture.url
        else:
            profile_picture = 'https://cdn.pixabay.com/photo/2015/10/0\
                5/22/37/blank-profile-picture-973460_1280.png'

        content = {'message': 'Welcome to the JWT Authentication page using React Js and Django!',
                   'name': str(request.user.first_name) + ' ' + str(request.user.last_name),
                    'email': str(request.user.email),
                    'username': str(request.user.username),
                    'profile_picture': profile_picture
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
        except PermissionError:
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
        user_rating_comment = UserRatingComment.objects.create(user=user,
                            rating=encrypt(rating), # Manual encryption
                            comment=comment,
                            review=review,
                            catalog=catalog,
                            comment_type=comment_type)
        user_rating_comment.save()

        return Response(status=status.HTTP_201_CREATED)

    def get(self, request):
        '''
        Get request to get user rating and comments
        '''
        # user = request.user
        # user_rating_comment = UserRatingComment.objects.filter(user=user)

        # # Decrypt user rating
        # for userRating in user_rating_comment:
        #     userRating.rating = decrypt(userRating.rating) # Manual decryption

        # # Return user rating and comments
        # return Response({
        #     'user_rating_comment': user_rating_comment.values()
        # }, status=status.HTTP_200_OK)

        user = request.user
        user_rating_comments = UserRatingComment.objects.filter(user=user)

        # Decrypt user rating
        for user_rating_comment in user_rating_comments:
            user_rating_comment.rating = decrypt(user_rating_comment.rating) # Manual decryption

        # Serialize the queryset
        serializer = UserRatingCommentSerializer(user_rating_comments, many=True)

        # Return serialized data
        return Response({
            'user_rating_comment': serializer.data
        }, status=status.HTTP_200_OK)

    def delete(self, request):
        '''
        Delete request to delete user rating and comments
        '''
        key = request.data.get('id')  # Retrieve id from the request body

        # Delete user rating and comments
        UserRatingComment.objects.filter(id=key).delete()

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
        UserRatingComment.objects.filter(user=user).update(
                            rating=encrypt(rating), # Manual encryption
                            comment=comment,
                            review=review,
                            catalog=catalog,
                            comment_type=comment_type)

        return Response(status=status.HTTP_200_OK)
# ------------------------------------------------------------------
# ------------------------------------------------------------------
    