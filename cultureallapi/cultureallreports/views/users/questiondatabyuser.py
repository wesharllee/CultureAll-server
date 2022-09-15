"""Module for generating question data by user report"""
from django.shortcuts import render
from django.db import connection
from django.views import View

from cultureallreports.views.helpers import dict_fetch_all

class UserQuestionData(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            #Write a query to get 
            db_cursor.execute("""
            SELECT
            qt.question_type_id,
            qt.type,
            q.
            u.first_name ||" " || u.last_name as full_name,

            """)