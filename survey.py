# -*- ecoding:utf-8 -*-
'''一个要测试的类'''


class AnonymousSurvey():
    '''收集匿名调查问卷的答案'''

    def __init__(self, question):
        """存储一个问题,并为存储答案做准备"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示调查问卷"""
        print self.question

    def store_response(self, new_response):
        """添加一个问题答案"""
        self.responses.append(new_response)

    def show_results(self):
        """显示收集到的所有答案"""
        print("Survey results:")
        for res in self.responses:
            print('-' + res)