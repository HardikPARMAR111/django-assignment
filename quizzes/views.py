from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, Answer, UserSubmission, UserAnswer

def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, "quizzes/quiz_list.html", {"quizzes": quizzes})

def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    return render(request, "quizzes/quiz_detail.html", {"quiz": quiz})

def submit_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        submission = UserSubmission.objects.create(quiz=quiz, user_name=user_name)
        score = 0
        for question in quiz.questions.all():
            selected_id = request.POST.get(str(question.id))
            if selected_id:
                answer = Answer.objects.get(id=int(selected_id))
                is_correct = answer.is_correct
                UserAnswer.objects.create(
                    submission=submission, question=question, answer=answer, is_correct=is_correct
                )
                if is_correct:
                    score += 1
        submission.score = score
        submission.save()
        return redirect("quiz_result", submission_id=submission.id)

def quiz_result(request, submission_id):
    submission = get_object_or_404(UserSubmission, id=submission_id)
    return render(request, "quizzes/quiz_result.html", {"submission": submission})
