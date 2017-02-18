from preprocess import preprocess as pre

texts = pre.open_without_final_line("path_to_your_text")
cleaned_texts = []
for index, text in enumerate(texts):
    print index
    if not (pre.judge_language(text, "ENGLISH")):
        continue
    text = pre.remove_html_tag(text)
    text = pre.remove_url(text)
    text = pre.to_lower(text)
    text = pre.remove_stop_words(text)
    text = pre.lemmatize(text)
    text = pre.remove_unicode(text)
    text = pre.remove_redundant_whitespace(text)
