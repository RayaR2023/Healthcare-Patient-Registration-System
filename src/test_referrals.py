from src.services.patient_service import get_patient_referrals

referrals = get_patient_referrals(1001)

for referral in referrals:
    print("----------------------")
    print(referral.referring_clinic)
    print(referral.referral_date)
    print(referral.status)