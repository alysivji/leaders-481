import pandas as pd

respondents = ['Vlad', 'Gordon', 'Jina', 'Zax', 'Ericka', 'Sean']


def read_scores(file):
    with open(file, 'r') as f:
        results = []
        answers = {}

        for line in f.readlines():
            if line.strip() in respondents:
                respondent = line.strip()
            elif line is '\n':
                answers[respondent] = results
                results = []
            else:
                results.append(float(line.split()[-1]))

    answers[respondent] = results  # one time for last result
    return answers


if __name__ == '__main__':
    result = read_scores('input.txt')
    df = pd.DataFrame(result, index=range(1,15))
