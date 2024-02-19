def calculate_score(scores) -> float:
    scores.remove(max(scores))
    scores.remove(min(scores))
    print(scores)
    average_score = sum(scores) / len(scores)
    return average_score

def main():
    n = int(input("Введіть кількість оцінок: "))
    scores = []
    for i in range(n):
        score = float(input(f"Введіть оцінку {i + 1}: "))
        scores.append(score)

    result_score = calculate_score(scores)

    print(f"Середнє арефметичне: {result_score}")

if __name__ == "__main__":
    main()
