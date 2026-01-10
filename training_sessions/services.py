from core.utils import send_email
from beneficiaries.models import BeneficiaryProfile
from django.contrib.auth.models import User

def notify_training_session(session):
    """
    Notify trainer and all beneficiaries about a newly created session.
    """
    
    trainer_email = session.trainer.email
    subject = f"New Training Session Assigned: {session.topic}"
    message = f"""
Hello {session.trainer.username},

You have been assigned to deliver a new training session.

Topic: {session.topic}
Date: {session.date}
Start Time: {session.start_time}
End Time: {session.end_time}
Category: {session.category.name}
Description: {session.description}

Thank you.
"""
    send_email(trainer_email, subject, message)

    # Notify beneficiaries
    beneficiaries = BeneficiaryProfile.objects.filter(
        category=session.category,
        status="APPROVED",
        is_deleted=False
    )

    for b in beneficiaries:
        subject = f"New Training Session Scheduled: {session.topic}"
        message = f"""
Hello {b.user.username},

A new training session has been scheduled for your category: {session.category.name}.

Topic: {session.topic}
Date: {session.date}
Start Time: {session.start_time}
End Time: {session.end_time}
Trainer: {session.trainer.username}
Description: {session.description}

Please mark your calendar.
"""
        send_email(b.user.email, subject, message)
