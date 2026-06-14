# This module performs analysis of model responses by detecting the presence of 
# predefined words. It identifies if a response contains expressions of moral judgment, 
# justification, uncertainty, and reframing, producing interpretable qualitative metrics.

class ResponseClassifier:

    def classify(self, text):

        text = text.lower()

        judgment_words = [
            "right",
            "wrong",
            "acceptable",
            "unacceptable",
            "ethical",
            "unethical",
            "moral",
            "immoral",
            "justified",
            "unjustified",
            "valid",
            "invalid",
            "reasonable",
            "unreasonable",
            "appropriate",
            "inappropriate",
            "fair",
            "unfair",
            "correct",
            "incorrect"
        ]

        justification_words = [
            "because",
            "since",
            "therefore",
            "as",
            "due to",
            "the reason",
            "this is because"
        ]

        uncertainty_words = [
            "may",
            "might",
            "could",
            "depends",
            "possibly",
            "perhaps"
        ]

        return {

            "judgment":
                any(w in text for w in judgment_words),

            "justification":
                any(w in text for w in justification_words),

            "uncertainty":
                any(w in text for w in uncertainty_words),

            "reframing":
                any(
                    phrase in text
                    for phrase in ["it is important to consider", "from a moral perspective", "on the other hand", "in this case"]
                )}