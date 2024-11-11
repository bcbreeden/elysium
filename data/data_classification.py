import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def categorize_sentence(sentence):
    if isinstance(sentence, str):
        sentence = sentence.lower()
        chaotic_keywords = [
        "unrest", "crisis", "violence", "instability", "disaster", "turmoil", "clashes", "chaos", 
        "protests", "uprising", "panic", "emergency", "scandal", "conflict", "disruption", 
        "anarchy", "confusion", "escalation", "breakdown", "outrage", "catastrophe", "rebellion", 
        "collapse", "mayhem", "disorder", "strife", "shock", "havoc", "upheaval", "alarm", 
        "volatility", "riot", "rebellion", "revolt", "disturbance", "frenzy", "tumult", "lawlessness", 
        "chaotic", "devastation", "explosion", "storm", "desperation", "fear", "danger", 
        "incident", "accident", "trauma", "calamity", "insurgency", "tragedy", "violations", 
        "rupture", "siege", "eruption", "wreckage", "collision", "flood", "tornado", "earthquake", 
        "epidemic", "collapse", "burning", "bloodshed", "plague", "contagion", "blaze", "eruption", 
        "meltdown", "scare", "disarray", "agitation", "uncertainty", "paranoia", "feud", "siege", 
        "hostility", "misfortune", "rebuke", "intensity", "wreck", "chaotic", "confounding", 
        "collapse", "coup", "subversion", "displacement", "hazard", "rage", "climax", 
        "exodus", "scarcity", "deficiency", "crunch", "emergency", "tensions", "pressures", 
        "assault", "bombardment", "occupation", "violations", "casualties"
        ]

        lawful_keywords = [
        "order", "law", "structure", "regulation", "compliance", "rules", "governance", "authority", 
        "justice", "stability", "control", "peace", "legislation", "policy", "rights", "constitution", 
        "standard", "norms", "code", "system", "legal", "protocol", "approval", "sanction", "authorization", 
        "permissible", "jurisdiction", "enforcement", "procedure", "formality", "official", "mandate", 
        "discipline", "security", "oversight", "authorization", "permitted", "supervision", "legitimacy", 
        "due process", "harmony", "consent", "certification", "fairness", "reliability", "legality", 
        "agreement", "treaty", "pact", "orderliness", "conformity", "prescribed", "licensed", "constitutional", 
        "adherence", "ratified", "provision", "recognized", "accepted", "customary", "governing", "consistent", 
        "established", "safeguard", "authorized", "settlement", "resolution", "protection", "deterrent", 
        "defense", "consensus", "guidelines", "framework", "structure", "jurisprudence", "code of conduct", 
        "procedural", "moderation", "neutrality", "precedent", "civility", "propriety", "discretion", 
        "arrangement", "institutional", "rectitude", "rationality", "balance", "stewardship", "accountability", 
        "deliberation", "orderly", "rule-bound", "unbiased", "even-handed", "responsibility", "policing", 
        "validation", "approbation", "ratification", "cooperation", "integrity", "sanctioned", "prescriptive"
        ]
        chaotic_score = sum(1 for word in chaotic_keywords if word in sentence)
        lawful_score = sum(1 for word in lawful_keywords if word in sentence)
        sentiment_score = _sentiment_analysis(sentence)

        return {
            'chaotic_score': chaotic_score,
            'lawful_score': lawful_score,
            'sentiment_score': sentiment_score
        }
    # If sentence isn't a string, return zero for all scores.
    else:
        print('Classification request not of type string.')
        print('Type:', type(sentence))
        return {
            'chaotic_score': 0,
            'lawful_score': 0,
            'sentiment_score': 0.0
        }

def _sentiment_analysis(sentence):
    tokens = word_tokenize(sentence)
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]

    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    processed_text = ' '.join(lemmatized_tokens)

    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(processed_text)
    return score['compound']
