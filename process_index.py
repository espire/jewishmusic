import re

with open('docs/index.md', 'r') as f:
    lines = f.readlines()

new_lines = []

# Map keyword to (Jewish Video ID, Source Video ID, Jewish Title, Source Title)
pairs = {
    "Maoz Tzur": ("2HdepdU5dZM", "nZ8oOHjsSxQ", "Maoz Tzur", "Nun Freut Euch, Liebe Christen, G'mein"),
    "Chayav Inish Livsumei": ("6R20yOx508Q", "mA-m6pE31DY", "Chayav Inish Livsumei", "this Hungarian tune"),
    "Mishenichnas Adar": ("0x9V59imR_U", "pd5ViH_5598", "Mishenichnas Adar", "Pick A Bale of Cotton"),
    "Umacha": ("-IfpQYFCo94", "RjBLGXhKMp8", "Yehuda!'s Umacha", "Chris de Burgh's Snows of New York"),
    "Yidden": ("l_aK9rM0mFk", "pzmI3vKIhqU", "MBD's Yidden", "Dschinghis Khan by Dschinghis Khan"),
    "Hashem Melech": ("eYk1s1A1Auo", "5dWeeUIZFgA", "Gad Elbaz's Hashem Melech", "C'est la vie by Khaled"),
    "A Boy Named Zlateh": ("2KFs9vXszzI", "eFQsC1DfyWc", "A Boy Named Zlateh", "A Boy Named Sue"),
    "Big Bad Moish": ("mP806v2CFGA", "ccMh8w-qsnI", "Big Bad Moish", "Big Bad John"),
    "Shacharis in the Morning": ("OhZ6S_zW2HU", "pIaWfLoHe8Y", "Shacharis in the Morning", "Sugartime by The McGuire Sisters"),
    "Torah Torah Torah": ("1V0NGThN5jg", "DUKNLlY0278", "Torah Torah Torah", "Let Us Sing Together"),
    "Hatikvah": ("4GfdKYuVK6g", "KK1Im3cvpz8", "Hatikvah", "La Mantovana by Giuseppe Cenci ca. 1600"),
    "Jerusalem of Gold": ("7nRNL-9NQpw", "ttuRcl1dK1M", "Jerusalem of Gold", "Pello Joxepe, a Basque lullaby"),
}

def generate_iframe(video_id):
    return f'<iframe width="320" height="180" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allowfullscreen></iframe>'

i = 0
while i < len(lines):
    line = lines[i]
    if line.startswith('* '):
        matched = False
        for key, (j_id, s_id, j_title, s_title) in pairs.items():
            if key in line:
                table = "<table>\n"
                table += "  <tr>\n"
                table += f"    <th>{j_title}</th>\n"
                table += f"    <th>{s_title}</th>\n"
                table += "  </tr>\n"
                table += "  <tr>\n"
                table += f"    <td>{generate_iframe(j_id)}</td>\n"
                table += f"    <td>{generate_iframe(s_id)}</td>\n"
                table += "  </tr>\n"
                table += "</table>\n\n"
                new_lines.append(table)

                # Check for sub-bullets
                j = i + 1
                while j < len(lines) and lines[j].startswith('  * '):
                    new_lines.append(lines[j])
                    j += 1
                i = j - 1
                matched = True
                break
        if not matched:
            new_lines.append(line)
    else:
        new_lines.append(line)
    i += 1

with open('docs/index.md', 'w') as f:
    f.writelines(new_lines)
