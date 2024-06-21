from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

q_bank = []
for q in question_data:
    # new_q = Question(text=q["text"], answer=q["answer"])
    new_q = Question(text=q["question"], answer=q["correct_answer"])

    q_bank.append(new_q)

    # q_text = q["text"]
    # q_answer = q["answer"]
    # new_q = Question(text=q_text, answer=q_answer)
    # q_bank.append(new_q)

quiz = QuizBrain(q_bank)

while quiz.still_has_questions():
    quiz.next_question()

quiz.final_score()
