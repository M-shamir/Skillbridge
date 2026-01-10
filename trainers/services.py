# trainers/services.py
import random
import string
from core.utils import send_email
from .models import TrainerProfile

def generate_password(length=8):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))

def approve_trainer(trainer_id):
    try:
        trainer = TrainerProfile.objects.get(
            id=trainer_id,
            status="PENDING",
            is_deleted=False
        )
    except TrainerProfile.DoesNotExist:
        return None, "Trainer not found or already processed"

    password = generate_password()

    user = trainer.user
    user.set_password(password)
    user.is_active = True
    user.save()

    trainer.status = "APPROVED"
    trainer.save()

    send_email(
        user.email,
        "Trainer Account Approved",
        f"""
Hello {user.username},

Your trainer account has been approved.

Username: {user.username}
Password: {password}

Please login and change your password.
"""
    )

    return trainer, password
