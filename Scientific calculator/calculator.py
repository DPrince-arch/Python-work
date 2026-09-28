import evaluator as expr

def main():
    print("WELCOME")
    last_result = None

    while True:
        try:
            raw = input(">>> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not raw:
            continue

        lowered = raw.lower()
        if lowered in ("exit", "quit"):
            print("Goodbye!")
            break
        
        try:
            result = expr.evaluate(raw, ans=last_result)
          
        except ZeroDivisionError as e:
            print(f"Error: {e}")
            continue
        except (ValueError, TypeError, SyntaxError) as e:
            print(f"Error: {e}")
            continue
        except OverflowError:
            print("Error: Result too large to compute.")
            continue

        last_result = result
        print(result)


if __name__ == "__main__":
    main()