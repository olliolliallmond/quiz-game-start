# TODO: ask the question
# TODO: check answer
# TODO: check of done

# Attributes:
# question_number = 0
# questions_list

# Methods:
# next_question()
# still_has_questions()
# check_answer()


class QuizBrain:
    def __init__(self, list):
        self.q_num = 0
        self.score = 0
        self.q_list = list

    def check_answer(self, q_ans, user_ans):
        # covert user_input to upper
        # target first letter of answers
        # print(q_ans[0] == user_ans[0])
        if q_ans[0] == user_ans[0]:
            print("You got is right!")
            self.score +=1
        else:
            print("You've learned something new!")
        print(f"The correct answer is: {q_ans}")
        print(f"Your score is: {self.score}/{self.q_num}\n")
        # return q_ans[0] == user_ans[0]

    def still_has_questions(self):
        # list_len = len(self.q_list)
        # if self.q_num == list_len:
        #     return False
        # return True
        return self.q_num < len(self.q_list)
    def next_question(self):
        curr_q = self.q_list[self.q_num]
        self.q_num += 1
        resp = input(f"Q.{self.q_num}: {curr_q.text} (True/False): ").upper()
        self.check_answer(q_ans=curr_q.answer, user_ans=resp)

    def final_score(self):
        print(f"Congratulations! You've completed the quiz.\nYour final score is {self.score}/{self.q_num}!")