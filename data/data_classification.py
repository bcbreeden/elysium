def categorize_sentence(sentence):
    
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

    good_keywords = [
    "kindness", "compassion", "empathy", "generosity", "charity", "honesty", "integrity", 
    "justice", "forgiveness", "peace", "hope", "love", "joy", "altruism", "benevolence", 
    "morality", "trust", "loyalty", "respect", "virtue", "honor", "grace", "mercy", 
    "harmony", "faithfulness", "selflessness", "gentleness", "fairness", "responsibility", 
    "goodwill", "humility", "modesty", "patience", "tolerance", "courage", "sincerity", 
    "understanding", "upliftment", "truthfulness", "compassionate", "friendship", "care", 
    "dedication", "helpfulness", "encouragement", "protection", "support", "nurturing", 
    "wisdom", "gratitude", "hopefulness", "generous", "mindfulness", "positivity", 
    "trustworthy", "devotion", "bravery", "reliability", "acceptance", "peaceful", 
    "caring", "thoughtfulness", "uplifting", "faith", "charitable", "fidelity", "sympathy", 
    "warmth", "nobility", "compassionate", "kind", "servitude", "truth", "responsiveness", 
    "open-mindedness", "balance", "helpful", "innocence", "loyal", "encouraging", "uplifting", 
    "benevolent", "courageous", "persistence", "redeeming", "optimism", "forbearing", 
    "moral", "dignity", "equity", "inspiration", "redemption", "self-respect", "consideration", 
    "trustworthiness", "inclusiveness", "faithful", "good-hearted", "uplifting", "steadfastness", 
    "patriotism", "decency", "sacrificial", "well-being"
    ]

    evil_keywords = [
    "hatred", "cruelty", "violence", "malice", "betrayal", "deception", "greed", "corruption", 
    "oppression", "injustice", "manipulation", "selfishness", "intolerance", "harm", "destruction", 
    "tyranny", "abuse", "dishonesty", "exploitation", "dishonor", "wrath", "revenge", "vengeance", 
    "aggression", "domination", "hostility", "corrupt", "chaos", "fear", "terror", "brutality", 
    "infamy", "deceit", "immorality", "sadism", "prejudice", "bigotry", "animosity", "vindictiveness", 
    "ruthlessness", "subjugation", "hypocrisy", "envy", "spite", "despair", "pessimism", "malevolence", 
    "wickedness", "murder", "crime", "betrayal", "darkness", "oppression", "fraud", "despotism", 
    "manipulative", "heartless", "suffering", "paranoia", "disharmony", "sinister", "atrocity", 
    "threat", "invasion", "theft", "defilement", "obsession", "injustice", "slander", "persecution", 
    "disregard", "torment", "pain", "enslavement", "fearmongering", "distress", "malignant", "fiendish", 
    "dread", "antagonism", "resentment", "bullying", "unforgiving", "scorn", "predator", "depravity", 
    "infliction", "violator", "inhumanity", "merciless", "barbaric", "exploitative", "doom", 
    "despicable", "retribution", "insidious", "oppressive", "sadistic", "vindictive", "villainy", 
    "predatory", "treachery", "manipulative"
    ]

    chaotic_score = sum(1 for word in chaotic_keywords if word in sentence.lower())
    lawful_score = sum(1 for word in lawful_keywords if word in sentence.lower())
    good_score = sum(1 for word in good_keywords if word in sentence.lower())
    evil_score = sum(1 for word in evil_keywords if word in sentence.lower())

    score = {
        'chaotic_score': chaotic_score,
        'lawful_score': lawful_score,
        'good_score': good_score,
        'evil_score': evil_score
    }

    return score
