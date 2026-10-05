import matplotlib.pyplot as plt

# Data
students = ['S1', 'S2', 'S3', 'S4', 'S5',
            'S6', 'S7', 'S8', 'S9', 'S10']

study_hours = [8, 10, 12, 15, 18, 20, 7, 14, 16, 22]
exam_scores = [65, 72, 75, 82, 88, 90, 60, 80, 85, 95]

# Create plots
plt.figure(figsize=(10, 8))

# Histogram of study hours
plt.subplot(2, 2, 1)
plt.hist(study_hours, bins=5, edgecolor='black')
plt.xlabel("Study Hours per Week")
plt.ylabel("Number of Students")
plt.title("Distribution of Study Hours")

# Histogram of exam scores
plt.subplot(2, 2, 2)
plt.hist(exam_scores, bins=5, edgecolor='black')
plt.xlabel("Exam Score")
plt.ylabel("Number of Students")
plt.title("Distribution of Exam Scores")

# Scatter plot
plt.subplot(2, 1, 2)
plt.scatter(study_hours, exam_scores, s=60)

# Add student labels
for i in range(len(students)):
    plt.annotate(students[i],
                 (study_hours[i], exam_scores[i]))

plt.xlabel("Study Hours per Week")
plt.ylabel("Exam Score")
plt.title("Relationship between Study Hours and Exam Scores")
plt.grid(True)

plt.tight_layout()
plt.show()