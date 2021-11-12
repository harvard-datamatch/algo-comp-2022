import numpy as np
from typing import List, Tuple
from models import Person

def run_matching(scores: List[List], gender_id: List, gender_pref: List) -> List[Tuple]:
    """
    TODO: Implement Gale-Shapley stable matching!
    :param scores: raw N x N matrix of compatibility scores. Use this to derive a preference rankings.
    :param gender_id: list of N gender identities (Male, Female, Non-binary) corresponding to each user
    :param gender_pref: list of N gender preferences (Men, Women, Bisexual) corresponding to each user
    :return: `matches`, a List of (Proposer, Acceptor) Tuples representing monogamous matches

    Some Guiding Questions/Hints:
        - This is not the standard Men proposing & Women receiving scheme Gale-Shapley is introduced as
        - Instead, to account for various gender identity/preference combinations, it would be better to choose a random half of users to act as "Men" (proposers) and the other half as "Women" (receivers)
            - From there, you can construct your two preferences lists (as seen in the canonical Gale-Shapley algorithm; one for each half of users
        - Before doing so, it is worth addressing incompatible gender identity/preference combinations (e.g. gay men should not be matched with straight men).
            - One easy way of doing this is setting the scores of such combinations to be 0
            - Think carefully of all the various (Proposer-Preference:Receiver-Gender) combinations and whether they make sense as a match
        - How will you keep track of the Proposers who get "freed" up from matches?
        - We know that Receivers never become unmatched in the algorithm.
            - What data structure can you use to take advantage of this fact when forming your matches?
        - This is by no means an exhaustive list, feel free to reach out to us for more help!
    """
    N = len(gender_id)
    proposers = []
    receivers = []
    proposer_proposals = {}
    receiver_proposals = {}
    matches = []
    
    # populate an array of proposers with gender_id, gender_pref, and list of scores
    for i in range(int(N/2)):
        person = Person()
        person.index = i
        person.gender_id = gender_id[i]
        person.gender_pref = gender_pref[i]
        for j in range(int(N/2), N):
            person.scores[j] = scores[i][j]
        proposers.append(person)
        proposer_proposals[i] = []
    
    # populate an array of receivers with gender_id, gender_pref, and list of scores
    for i in range(int(N/2), N):
        person = Person()
        person.index = i
        person.gender_id = gender_id[i]
        person.gender_pref = gender_pref[i]
        for j in range(int(N/2)):
            person.scores[j] = scores[i][j]
        receivers.append(person)
        receiver_proposals[i] = -1
    
    # adjust scores based on gender preferences 
    for proposer in proposers:
        for receiver in receivers:
            if proposer.gender_pref != "Bisexual":
                if (proposer.gender_id == "Male" and receiver.gender_pref != "Men") or (receiver.gender_id == "Male" and proposer.gender_pref != "Men"):
                    proposer.scores[receiver.index] = 0
                    receiver.scores[proposer.index] = 0
                if (proposer.gender_id == "Female" and receiver.gender_pref != "Women") or (receiver.gender_id == "Female" and proposer.gender_pref != "Women"):
                    proposer.scores[receiver.index] = 0
                    receiver.scores[proposer.index] = 0
 
    # implement gale-shapley algorithm
    while(-1 in receiver_proposals.values()):
        for proposer in proposers:
            if proposer.index not in receiver_proposals.values():
                # dict of receivers unproposed by proposer
                unproposed = {}
                for receiver in receivers:
                    if receiver.index not in proposer_proposals[proposer.index]:
                        unproposed[receiver.index] = proposer.scores[receiver.index]
                # find unproposed receiver with highest score
                while(True):
                    highscore = sorted(unproposed.values())[len(unproposed.keys())-1]
                    best_match = 0
                    for receiver_index, score in proposer.scores.items():
                        if score == highscore and receiver_index in unproposed.keys():
                            best_match = receiver_index
                    # matches receiver and proposer if receiver is not matched yet
                    if receiver_proposals[best_match] < 0:
                        receiver_proposals[best_match] = proposer.index
                        proposer_proposals[proposer.index].append(best_match)
                        break
                    # otherwise, checks if receiver prefers proposer over current match
                    elif scores[proposer.index][best_match] > scores[receiver_proposals[best_match]][best_match]:
                        receiver_proposals[best_match] = proposer.index
                        proposer_proposals[proposer.index].append(best_match)
                        break
                    # receiver reject proposer
                    else:
                        unproposed = {i :unproposed[i] for i in unproposed if i!=best_match}
                
    # add stable matches to list
    for receiver in receiver_proposals.keys():
        matches.append((receiver_proposals[receiver], receiver))

    print(matches)
    return matches


if __name__ == "__main__":
    raw_scores = np.loadtxt('raw_scores.txt').tolist()
    genders = []
    with open('genders.txt', 'r') as file:
        for line in file:
            curr = line[:-1]
            genders.append(curr)

    gender_preferences = []
    with open('gender_preferences.txt', 'r') as file:
        for line in file:
            curr = line[:-1]
            gender_preferences.append(curr)

    gs_matches = run_matching(raw_scores, genders, gender_preferences)
