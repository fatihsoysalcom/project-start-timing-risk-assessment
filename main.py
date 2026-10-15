import datetime

def assess_project_start_readiness(day_of_week: str) -> str:
    """
    Assesses the readiness for starting a critical project based on the day of the week,
    drawing parallels to the 'don't order fish on Monday' and 'don't release on Friday'
    principles from the article.
    """
    day = day_of_week.lower()

    if day == "monday":
        # This illustrates the "Pazartesi balık sipariş etmeyin" (Don't order fish on Monday)
        # metaphor: Inputs (like fish) might not be fresh, or the team might not be fully
        # ramped up after the weekend, leading to higher risk for critical decisions.
        return (
            f"Risk Assessment for {day_of_week}: HIGH.\n"
            "Reason: Potential for stale inputs, lower team alertness after weekend, "
            "or critical decisions made without full context. "
            "Recommendation: Re-evaluate inputs, defer critical starts if possible."
        )
    elif day == "friday":
        # This illustrates the "Cuma günü sürüm çıkarmayın" (Don't release on Friday)
        # principle: Limited time for immediate issue resolution before the weekend,
        # increasing risk for critical software releases or project handovers.
        return (
            f"Risk Assessment for {day_of_week}: MEDIUM to HIGH.\n"
            "Reason: Limited time for immediate issue resolution before the weekend, "
            "potential for rushed decisions or lack of immediate support. "
            "Recommendation: Avoid starting critical tasks that require immediate follow-up "
            "or extensive support over the weekend."
        )
    elif day in ["saturday", "sunday"]:
        return (
            f"Risk Assessment for {day_of_week}: VERY HIGH.\n"
            "Reason: Weekend. Minimal team availability and support. "
            "Recommendation: Strongly advise against starting critical projects."
        )
    else:  # Tuesday, Wednesday, Thursday
        return (
            f"Risk Assessment for {day_of_week}: LOW.\n"
            "Reason: Optimal working days. Team is generally ramped up, "
            "and there's sufficient time for follow-up within the week. "
            "Recommendation: Good timing for critical project starts."
        )


if __name__ == "__main__":
    print("--- Project Start Readiness Assessment ---")
    print("This script simulates assessing the optimal timing for starting a critical project,")
    print("inspired by the 'Don't order fish on Monday' and 'Don't release on Friday' principles.")
    print("-" * 60)

    days_to_assess = [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ]

    for day in days_to_assess:
        print(f"\nAssessing: {day}")
        print(assess_project_start_readiness(day))
        print("-" * 30)

    print("\n--- Current Day Assessment ---")
    today = datetime.datetime.now().strftime("%A")
    print(f"Today is: {today}")
    print(assess_project_start_readiness(today))
    print("-" * 60)
