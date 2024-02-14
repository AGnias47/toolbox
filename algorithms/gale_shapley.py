#!/usr/bin/env python
#
# References:
# - https://github.com/shubh11220/The-Stable-Matching-Algorithm/blob/master/Stable_Matching.py
# - https://towardsdatascience.com/gale-shapley-algorithm-simply-explained-caa344e643c2


class GaleShapley:
    def __init__(self, men_preferences, women_preferences):
        self.men_preferences = men_preferences
        self.women_preferences = women_preferences
        self.free_men = set(men_preferences.keys())
        self.free_women = set(women_preferences.keys())
        self.validate()
        self.matches = {}

    def validate(self):
        if len(self.free_men) != len(self.free_women):
            raise ValueError("Number of men and women must be equal")
        for m, prefs in self.men_preferences.items():
            try:
                assert set(prefs) == self.free_women
            except AssertionError:
                raise ValueError(f"Preferences for {m} must include all women")
        for w, prefs in self.women_preferences.items():
            try:
                assert set(prefs) == self.free_men
            except AssertionError:
                raise ValueError(f"Preferences for {w} must include all men")

    def run(self):
        while self.free_men:
            m = self.free_men.pop()
            self.propose(m)
        for w in self.women_preferences.keys():
            self.matches.pop(w)
        return self.matches

    def propose(self, m):
        for w in self.men_preferences[m]:
            if w in self.free_women:
                self.get_engaged(m, w)
                self.free_women.remove(w)
                break
            else:
                w_current = self.matches[w]
                if self.leave_for_new_match(m, w, w_current):
                    self.get_engaged(m, w)
                    self.free_men.add(w_current)
                    break

    def get_engaged(self, m, w):
        self.matches[m] = w
        self.matches[w] = m

    def leave_for_new_match(self, m, w, w_current):
        w_current_rank = self.women_preferences[w].index(w_current)
        w_new_rank = self.women_preferences[w].index(m)
        return w_new_rank < w_current_rank


if __name__ == "__main__":
    men_pref = {"A": ["D", "E", "F"], "B": ["E", "D", "F"], "C": ["D", "E", "F"]}
    women_pref = {"D": ["A", "B", "C"], "E": ["A", "B", "C"], "F": ["A", "B", "C"]}
    gale_shapley = GaleShapley(men_pref, women_pref)
    print(gale_shapley.run())
