from operator import itemgetter
from src.min_dis import levenshtein_distance
import pytrec_eval as pt
import nltk

# Download required NLTK resources
nltk.download('wordnet',  quiet=True)
nltk.download('omw-1.4',  quiet=True)
from nltk.corpus import wordnet
# nltk.download('omw-1.4') # to remove Look up error Resource omw-1.4 not found.
if 'omw-1.4' not in nltk.corpus.wordnet.fileids():
    # If not, download it
    nltk.download('omw-1.4',  quiet=True)

def success_top_k(top_result):
    success_dict = {}
    for item in top_result:
        correct_item = item['correct']
        incorrect_item = item['incorrect']
        top1 = item['most_similar_1']
        top5 = item['most_similar_5']
        top10 = item['most_similar_10']
        combine_dict = {
            'success_at_1': 1 if correct_item in top1 else 0,
            'success_at_5': 1 if correct_item in top5 else 0,
            'success_at_10': 1 if correct_item in top10 else 0
        }
        success_dict[incorrect_item] = combine_dict
    return success_dict

def calculate_top_words(row):
    # random_words = [''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 8))) for _ in range(100)]
    distances = {}
    wn_result = {}
    d = set(wordnet.words(lang='eng'))
    result = {
        'correct': row[0],
        'incorrect': row[1]
    }
    for word in d:
        if len(word) > 1 and word.isalpha():
            # transformed_word = word.upper()
            edit_distance = levenshtein_distance(row[1], word)
            distances[word] = edit_distance

    top_k = [1, 5, 10]
    for k in top_k:
        top_k_words = [word for word, _ in sorted(distances.items(), key=lambda item: item[1])[:k]]
        result['most_similar_{}'.format(k)] = top_k_words

    return result

def average_success_top_k(success_data):
    avg_dict = {}
    first_key = list(success_data.keys())[0]
    for k_success in success_data[first_key].keys():
        aggregated_measure = pt.compute_aggregated_measure(
            k_success, [val[k_success] for val in success_data.values()])
        avg_dict[k_success] = aggregated_measure
    return avg_dict