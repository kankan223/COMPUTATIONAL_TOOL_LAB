import plotly.express as px

# Data
students = ['S1', 'S2', 'S3', 'S4', 'S5',
            'S6', 'S7', 'S8', 'S9', 'S10']

math_marks = [78, 85, 67, 90, 73, 81, 69, 94, 76, 88]

# Create interactive bar chart
fig = px.bar(
    x=students,
    y=math_marks,
    labels={
        'x': 'Student',
        'y': 'Mathematics Marks'
    },
    title='Mathematics Marks of Students'
)

# Display chart
fig.show()