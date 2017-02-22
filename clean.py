from preprocess import preprocess as pre
import json
import pickle
path_in = r"D:\Dropbox\Instrutable_PA\Corpus\Android App\google_play_list\toplist+top600\3 [no game with crawl data but no cleaned] bestapps.json"
path_out = r"D:\Dropbox\Instrutable_PA\Corpus\Android App\google_play_list\toplist+top600\4 [cleaned no summary] bestapps.json"
content = json.load(open(path_in))

texts = [x["Description"] for x in content]
print len(content), len(texts)
cleaned_index = []
# for index, text in enumerate(texts):
for index in range(len(texts)):
    print index
    text = texts[index]
    text = pre.remove_html_tag(text)
    text = pre.remove_url(text)
    # text = pre.remove_unicode(text)
    text = pre.add_dot(text)
    text = pre.remove_redundant_whitespace(text)
    # remove short text
    if (len(text.split()) < 10):
        continue
    # remove none english text in the file
    if not (pre.judge_language(text, "en")):
        continue
    content[index]["CleanedDescriptionForSummary"] = text
    text = pre.to_lower(text)
    text = pre.remove_stop_words(text)
    text = pre.remove_single_alpha(text)
    text = pre.lemmatize(text)
    text = pre.remove_unicode(text)
    text = pre.remove_single_alpha(text)
    text = pre.remove_redundant_whitespace(text)
    content[index]["CleanedDescription"] = text
    cleaned_index.append(index)
    # print text

cleaned_content = []
for index in cleaned_index:
    cleaned_content.append(content[index])

print len(cleaned_content)
with open(path_out, "w") as f:
    f.write("[" + "\n")
    for item in cleaned_content[:-1]:
        json.dump(item, f)
        f.write(',\n')
    json.dump(cleaned_content[-1], f)
    f.write("\n")
    f.write("]")