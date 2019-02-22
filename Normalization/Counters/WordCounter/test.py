from preprocess import make_tokens, regex_clean


tweet = "#volcanowatch the a new a b m s 12343 #puna #Hawaii #goingwiththeflow 🌋🤙🖤🙏 @ Pahoa, Hawai"

data = [term for term in make_tokens(tweet)]

print(regex_clean(tweet))