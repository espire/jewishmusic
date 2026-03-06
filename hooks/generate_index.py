import json
import os
import shutil

def on_config(config, **kwargs):
    # This hook runs exactly once per build/serve, before pre_build
    docs_dir = config.get('docs_dir', 'docs')

    data_path = os.path.join(docs_dir, 'data.json')
    welcome_path = os.path.join(docs_dir, 'welcome.md')
    index_path = os.path.join(docs_dir, 'index.md')

    with open(welcome_path, 'r', encoding='utf-8') as f:
        content = f.read()

    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for category in data.get('categories', []):
        content += f"\n\n## {category['name']}\n"

        for pair in category.get('pairs', []):
            content += "\n<table>\n"
            content += "  <tr>\n"
            content += f"    <th>{pair['jewish_song']}</th>\n"
            content += f"    <th>{pair['source_song']}</th>\n"
            content += "  </tr>\n"
            content += "  <tr>\n"
            content += f"    <td><iframe width=\"320\" height=\"180\" src=\"{pair['jewish_url']}\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe></td>\n"
            content += f"    <td><iframe width=\"320\" height=\"180\" src=\"{pair['source_url']}\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe></td>\n"
            content += "  </tr>\n"
            content += "</table>\n"

            if 'comment' in pair and pair['comment']:
                content += f"\n  {pair['comment']}\n"

    other_lists = data.get('other_lists', [])
    if other_lists:
        content += "\n## Other lists\n"
        for item in other_lists:
            content += f"* <{item}>\n"

    # Read old content
    old_content = ""
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            old_content = f.read()

    # Only write if it changed! This prevents the infinite reload loop in mkdocs serve.
    if content != old_content:
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
