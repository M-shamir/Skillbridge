
import random
import string
from django.contrib.auth.models import User
from .models import BeneficiaryProfile
from core.utils import send_email

def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))

def approve_beneficiary(beneficiary_id):
    try:
        beneficiary = BeneficiaryProfile.objects.get(
            id=beneficiary_id, status="PENDING", is_deleted=False
        )
    except BeneficiaryProfile.DoesNotExist:
        print(f"No PENDING beneficiary with id={beneficiary_id}")
        return None, "Beneficiary not found or already processed"

    # Generate password
    password = generate_random_password()

    # Activate user
    user = beneficiary.user
    user.set_password(password)
    user.is_active = True
    user.save()

    # Update status
    beneficiary.status = "APPROVED"
    beneficiary.save()
    print(f"Beneficiary {beneficiary.id} approved, sending email to {user.email}")

    # Send email safely
    try:
        send_email(user.email, "Your Beneficiary Account is Approved",
                   f"Hello {user.username}, your account is approved.\nUsername: {user.username}\nPassword: {password}")
        print("Email sent successfully")
    except Exception as e:
        print("Failed to send email:", e)

    return beneficiary, password

