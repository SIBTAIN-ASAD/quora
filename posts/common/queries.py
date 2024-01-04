'''
This file contains all the queries that are used in the posts app.
'''
from posts.models import Question, Answer, Vote, Topic

class HomePageQueries:
    '''
    This class contains all the queries that are used in the home page.
    '''
        # return the likes and dislikes of the question
    @staticmethod
    def get_votes(question):
        '''
        This method returns the number of likes and dislikes of the question.
        '''
        likes = Vote.objects.filter(question=question, vote_type="L").count()
        dislikes = Vote.objects.filter(question=question, vote_type="D").count()
        return likes, dislikes

    @staticmethod
    def get_user_questions(user):
        '''
        This method returns all the questions of the topics the user is following.
        Along with the likes and dislikes of the question.
        Order the questions by number of likes.
        '''
        topics = user.followed_topics.all()
        questions = Question.objects.filter(topic__in=topics)
        questions_list = []
        for question in questions:
            likes, dislikes = HomePageQueries.get_votes(question)
            questions_list.append((question, likes, dislikes))

        questions_list.sort(key=lambda x: x[1], reverse=True)

        return questions_list
