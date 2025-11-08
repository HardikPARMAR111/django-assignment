from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, Answer, UserSubmission, UserAnswer

#fetching all the quizzes from database
def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, "quizzes/quiz_list.html", {"quizzes": quizzes})

#fetching particular quiz from database with id
def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    return render(request, "quizzes/quiz_detail.html", {"quiz": quiz})

#logic for submitting the quiz and user_submission in database
def submit_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        submission = UserSubmission.objects.create(quiz=quiz, user_name=user_name)
        score = 0
        for question in quiz.questions.all():
            selected_id = request.POST.get(f"question_{question.id}")
            if selected_id:
                answer = Answer.objects.get(id=int(selected_id))
                is_correct = answer.is_correct
                UserAnswer.objects.create(
                    submission=submission, 
                    question=question, 
                    answer=answer, 
                    is_correct=is_correct
                )
                if is_correct:
                    score += 1
        submission.score = score
        submission.save()
        return redirect("quiz_result", submission_id=submission.id)

#for qui result page data fetching
def quiz_result(request, submission_id):
    submission = get_object_or_404(UserSubmission, id=submission_id)
    user_answers = UserAnswer.objects.filter(submission=submission).select_related('question', 'answer')
    return render(request, "quizzes/quiz_result.html", {
        "submission": submission,
        "user_answers": user_answers
    })

#for dashboard page data fetching
def quiz_dashboard(request):
    submissions = UserSubmission.objects.all().select_related('quiz').order_by('-submitted_at')
    total_quizzes = Quiz.objects.count()
    total_submissions = submissions.count()
    unique_users = submissions.values('user_name').distinct().count()

    submissions_with_data = []
    for submission in submissions:
        total_questions = submission.quiz.questions.count()
        percentage = (submission.score / total_questions * 100) if total_questions > 0 else 0
        
        if percentage >= 70:
            score_class = "bg-green-100 text-green-800"
        elif percentage >= 50:
            score_class = "bg-yellow-100 text-yellow-800"
        else:
            score_class = "bg-red-100 text-red-800"
        
        submission.score_class = score_class
        submission.total_questions = total_questions
        submissions_with_data.append(submission)
    
    return render(request, "quizzes/quiz_dashboard.html", {
        "submissions": submissions_with_data,
        "total_quizzes": total_quizzes,
        "total_submissions": total_submissions,
        "unique_users": unique_users
    })

