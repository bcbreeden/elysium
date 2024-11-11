import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def categorize_sentence(sentence):
    if isinstance(sentence, str):
        sentence = sentence.lower()
        processed_text = _process_text(sentence)

        chaotic_keywords = [
            "anarchy", "turmoil", "havoc", "disarray", "confusion", "pandemonium", "uproar", "mayhem", "bedlam", "unrest",
            "riot", "rebellion", "uprising", "insurgency", "disruption", "dysfunction", "tumult", "frenzy", "commotion",
            "turbulence", "instability", "agitation", "chaos", "disorder", "conflict", "confound", "disturbance", "madness",
            "rampage", "chaotic", "disorganize", "shamble", "scramble", "clutter", "derange", "falter", "distrust", "schism",
            "disorientation", "bedraggled", "maelstrom", "tempest", "cacophony", "anarchic", "disrupt", "overturn",
            "subversion", "jumbled", "tangle", "irregular", "fluctuation", "frenetic", "ruin", "muddle", "messy",
            "disjointed", "scatter", "antagonism", "violence", "disband", "disobedience", "incoherent", "discord",
            "rebellious", "unruly", "clash", "unpredictable", "haphazard", "volatile", "wreckage", "frantic", "negligent",
            "hazardous", "unsound", "upheaval", "misrule", "mutiny", "insurrection", "fractious", "reckless", "ruthless",
            "destruction", "hostility", "fallout", "wrath", "fury", "vexation", "unlawful", "catastrophic", "upset",
            "rupture", "corrupt", "mismanagement", "disheveled", "fragmented", "transgress", "lawlessness", "disruptive",
            "irreversible", "erratic", "discordance", "sabotage", "peril", "atrocious", "ramshackle", "discontent",
            "antipathy", "rampant", "explosive", "interruption", "subdue", "domination", "treachery", "betrayal",
            "indignation", "nuisance", "antagonist", "deform", "quagmire", "detonate", "fracture", "fissure", "brawl",
            "carnage", "unleash", "erupt", "eruption", "combust", "uproarious", "shockwave", "collide", "abrasion",
            "atrophy", "insubordination", "instigate", "riotous", "protest", "cluttered", "distort", "mishap", "clumsy",
            "pillage", "outburst", "implode", "explode", "retribution", "unsettle", "apocalyptic", "abrasive", "hostile",
            "vandalism", "desecration", "disillusion", "disharmony", "wreck", "brash", "violate", "transgression",
            "clamorous", "menace", "feud", "revulsion", "unease", "alarm", "alarmist", "fiasco", "deception", "misconduct",
            "hypocrisy", "tension", "warlike", "treason", "ramble", "perilous", "confront", "intimidate", "unhinged",
            "belligerent", "affliction", "menacing", "strife", "conflicting", "grievance", "betray", "defiance", "dissent",
            "provocation", "distress", "controversy", "hysteria", "derail", "incitement", "instability", "flawed",
            "discordant", "fracture", "antagonize", "chaotically", "subversive", "unravel", "ravage", "discordance",
            "animosity", "agitate", "aggravation", "relapse", "paranoia", "recklessness", "shock", "abnormal", "confusing",
            "perplex", "imbalance", "misunderstanding", "critique", "tumultuous", "struggle", "rivalry", "tribulation",
            "friction", "lawless", "outlaw", "turmoil", "abrasive", "dispute", "overwhelm", "exasperation", "sabotage",
            "defy", "opposition", "collapse", "shock", "breakdown", "disrepair", "disperse", "affliction", "provoke",
            "infraction", "ruinous", "falter", "confrontation", "havoc", "unorganized", "violator", "imperfection",
            "incomprehension", "aberration", "misfit", "overload", "panic", "assault", "fragmentation", "grievous",
            "bizarre", "fatal", "infuriate", "revolt", "outrage", "injustice", "shake", "demolition", "irregularity",
            "dismay", "discordant", "mutiny", "treacherous", "disloyalty", "transgression", "irate", "unforeseen",
            "disproportion", "fallible", "fractious", "reckless", "breakup", "nonconform", "displease", "ungoverned",
            "disorganized", "scatter", "war", "danger", "kill", "murder"
            ]

        lawful_keywords = [
            "law", "order", "stability", "peace", "justice", "authority", "regulation", "discipline", "structure",
            "harmony", "control", "governance", "security", "protection", "consistency", "rule", "legitimacy", "balance",
            "fairness", "clarity", "predictability", "certainty", "compliance", "obedience", "legal", "system", "principle",
            "right", "responsibility", "morality", "upright", "civility", "ethic", "sanction", "safeguard", "guideline",
            "standard", "orderly", "respect", "safety", "accountability", "reliability", "uniformity", "command", "custom",
            "honesty", "integrity", "propriety", "rectitude", "prudence", "decency", "cohesion", "unity", "fidelity",
            "honor", "regularity", "process", "consensus", "jurisdiction", "enforcement", "provision", "welfare", "peaceful",
            "regulate", "restraint", "prevention", "supervision", "guardian", "arbitration", "decision", "precedent",
            "composure", "tranquility", "obedient", "statute", "codify", "charter", "foundation", "constitution", "counsel",
            "trustworthy", "permanence", "government", "civil", "soundness", "consent", "legalize", "authorize", "precept",
            "edict", "mandate", "validity", "authorization", "clarification", "certification", "protocol", "ordinance",
            "legislation", "firmness", "settlement", "cooperation", "peacekeeping", "deterrence", "loyalty", "resolution",
            "pact", "accord", "council", "truce", "respectability", "policy", "validation", "organization", "procedural",
            "settle", "deterrent", "restoration", "obligation", "uniform", "regulated", "governed", "strength", "supervise",
            "sanctioned", "abidance", "concord", "submission", "orthodoxy", "consensual", "docility", "conservative",
            "acceptable", "grounded", "foundation", "civilization", "normative", "just", "adherence", "faithfulness",
            "safeguard", "sanctity", "repose", "serenity", "defense", "support", "corroborate", "regularize",
            "authorization", "organized", "align", "endorse", "adhere", "justified", "discipline", "docile", "warrant",
            "legitimize", "confirm", "valid", "official", "backing", "anchored", "ground", "legitimate", "ratified",
            "constitution", "bona fide", "back", "reliable", "binding", "protected", "defined", "solidified", "licensed",
            "trusted", "rest", "goodwill", "guardianship", "backup", "protection", "repute", "standing", "strengthened",
            "authority", "fundamental", "root", "persistence", "continuity", "perseverance", "tenacity", "unification",
            "precedent", "inviolable", "true", "unchanged", "permanent", "durable", "robust", "immovable", "immutable",
            "lawful", "customary", "preservation", "calm", "informed", "civilize", "consistent", "entrench", "immovable",
            "agreement", "statutory", "preserve", "sustain", "justness", "conform", "uprightness", "systematize", "duty",
            "civilian", "dignity", "mandated", "veracity", "certify", "respectful", "constant", "resolve", "dependable",
            "foundation", "genuine", "responsible", "guarantee", "incorruptible", "settle", "reassurance", "solidify",
            "compliant", "proven", "admissible", "codified", "status", "reputable", "regular", "underpin", "perpetuate",
            "organized", "peacekeeper", "procedural", "validation", "legality", "balanced", "protect", "plausible",
            "sound", "neutralize", "systemic", "approved", "ethical", "verified", "truth", "coherent", "neutral",
            "affirm", "established", "soundly", "unified", "stabilize", "licensed", "legalism", "patriotism", "morale",
            "authority", "guaranteed", "regulate", "truthful", "rational", "restoration", "documented", "credible",
            "formalize", "policy", "absolute", "monitored", "ensure", "community", "secure"
            ]


        chaotic_score = sum(1 for word in chaotic_keywords if word in processed_text)
        lawful_score = sum(1 for word in lawful_keywords if word in processed_text)
        sentiment_score = _sentiment_analysis(processed_text)

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

def _sentiment_analysis(processed_text):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(processed_text)
    return score['compound']

def _process_text(text):
    tokens = word_tokenize(text)
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]

    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    processed_text = ' '.join(lemmatized_tokens)
    return processed_text