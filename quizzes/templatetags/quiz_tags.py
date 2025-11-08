from django import template

register = template.Library()

@register.filter
def get_correct_answer(answers):
    """
    Custom filter to return the correct answer text from a queryset of answers.
    Usage in template: {{ question.answers.all|get_correct_answer }}
    """
    correct = answers.filter(is_correct=True).first()
    return correct.text if correct else "No correct answer set"
