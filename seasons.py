from datetime import datetime
import inflect

p = inflect.engine()

class Date:
    @staticmethod
    def age_in_minutes(birthdate: str):
        birthdate = birthdate.replace("/", "-")

        try:
            dob = datetime.strptime(birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

        today = datetime.now()

        diff = today - dob
        minutes = diff.days * 24 * 60 + diff.seconds // 60

        return minutes

def main():
    birth_input = input("Enter your date of birth (YYYY-MM-DD): ")\

    try:
        minutes = Date.age_in_minutes(birth_input)
        minutes_in_words = p.number_to_words(minutes)
        word_to_remove = " and"
        answer = minutes_in_words.replace(word_to_remove, "")
        print(f"\nYou are approximately {answer} minutes old.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
