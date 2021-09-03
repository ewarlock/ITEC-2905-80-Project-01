""" This program offers the user a quiz. The quiz can be selected based on several different categories. At the end of the quiz, the user is scored based on how many questions they got right. They receive a special message if they got all of the questions right."""

#quiz questions and answers sorted by category
categories = [
    {
        'id': '1',
        'Name':'Art',
        'Questions':[
            {'Question':'Who painted the Mona Lisa?', 'Answer':'Leonardo Da Vinci'},
            {'Question':'What precious stone is used to make the artist\'s pigment ultramarine?', 'Answer':'Lapiz Lazuli' },
            {'Question':'Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?', 'Answer':'Chicago'},
            {'Question':'Which kid\'s TV characters are named after Renaissance artists?', 'Answer':'Teenage Mutant Ninja Turtles'},
            {'Question':'The graphite in an artist\'s pencil is made of what chemical element?', 'Answer':'Carbon'}
        ]
    },
    {   
        'id': '2',
        'Name':'Space',
        'Questions':[
            {'Question':'Which planet is closest to the sun?', 'Answer':'Mercury'},
            {'Question':'Which planet spins in the opposite direction to all the others in the solar system?', 'Answer':'Venus' },
            {'Question':'How many moons does Mars have? Please enter a numeral (for example, 5)', 'Answer':'2'},
            {'Question':'What was the first human-made object to leave the solar system?', 'Answer':'Voyager 1'},
            {'Question':'When an asteroid enters the Earth\'s atmosphere and burns up, it is known as what?', 'Answer':'Meteor'}
        ]
    },
    {
        'id':'3',
        'Name':'Sports',
        'Questions':[
            {'Question':'Which gymnast is the "triple-twisting double-tucked salto backwards" skill named after?', 'Answer':'Simone Biles'},
            {'Question':'Which country has won the soccer world cup the most times?', 'Answer':'Brasil'},
            {'Question':'What does MLB stand for?', 'Answer':'Major League Baseball'}
        ]
    }
]


def score_question(user_answer, quiz_answer):
    #score user answers to each question
    score = 0

    #convert to upper for comparison so case doesn't matter
    if user_answer.upper() == quiz_answer.upper():
        print(f'{quiz_answer} is correct!')
        score = 1
    else:
        print(f'Sorry, the answer is {quiz_answer}, not {user_answer}')
    
    return score


def run_quiz(category):
    #runs the quiz based on category selected
    score = 0
    total_questions = len(category['Questions']) #count how many questions in category
    category_name = category['Name']

    #tell user what category they selected
    print(f'You have selected {category_name}.')

    #print the questions per category and let the user answer them
    for question in category['Questions']:
        quiz_question = question['Question']
        quiz_answer = question['Answer']
        
        #asks the user questions
        print(quiz_question)
        user_answer = input('Enter your answer: ')

        #score answer and add to score
        score += score_question(user_answer, quiz_answer)

    print(f'Your total score on {category_name} questions is {score} out of {total_questions}.')

    if score == total_questions:
        print('You got all the answers correct!')



def validate_category(category_selection):
    #make list of category ids for user input validation
    category_ids = []
    for category in categories:
        category_ids.append(category['id'])

    total_categories = len(category_ids)

    #user is prompted to re enter category id until they enter something valid
    while category_selection not in category_ids:
        print(f'Invalid selection. Please select a number within the range 1 through {total_categories}.')
        category_selection = input('Please type the number of the category you want to be quizzed on: ')

    return category_selection



def select_category():
    #prompt user to select a category and pass that selection to get_questions function
    
    #print all of the categories alongside IDs for user to select from
    for category in categories:
        category_id = category['id']
        category_name = category['Name']
        print(f'{category_id}. {category_name}')

    category_selection = input('Please type the number of the category you want to be quizzed on: ')

    category_selection = validate_category(category_selection)

    #select category based on id entered by user
    for category in categories:
        if category['id'] == category_selection:
            category_selection = category

    return category_selection



def main():
    print('Welcome to the Quiz Program. The categories are:')

    category = select_category()

    run_quiz(category)

    print('Thanks for using this Quiz Program!')

#call main to start program
if __name__ == '__main__':
    main()