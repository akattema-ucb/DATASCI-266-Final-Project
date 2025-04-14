import json

# Load the data
issues_list = []
issues_list_file = "data/dataset_rebalanced_train.json" 
with open(issues_list_file, "r", encoding="utf-8") as f:
    issues_list = json.load(f)

lab_order = [
    "accessibility",
    "release",
    "dependency",
    "good_first_issue",
    "webview",
    "oslinux",
    "revert",
    "bug",
    "documentation",
    "featurerequest",
    "feature",
    "help_wanted",
    "test",
    "ui",
    "api",
    "enhancement",
    "regression",
    "security"
]

def clean_text(text):
    """
    Cleans the input text by stripping extra whitespace and newlines.
    """
    return " ".join(text.split())

def format_issue(title, body, comments):
    # Ensure each part is a string and clean up any extra whitespace
    title = clean_text(str(title).strip())
    body = clean_text(str(body).strip())
    comments = clean_text(str(comments).strip())
    
    # Create a structured input string with clear delimiters
    formatted_text = f"Title: {title} [SEP] Body: {body} [SEP] Comments: {comments}"
    return formatted_text

formatted_issues = []

for iss in issues_list:
    fmt_iss_text = format_issue(
        title=iss.get("title", ""),
        body=iss.get("body", ""),
        comments=iss.get("comments", "")
    )

    iss_labs = [
        1.0 if iss.get(lab, False) else 0.0 for lab in lab_order
    ]

    fmt_iss = {
        "text": fmt_iss_text,
        "labels": iss_labs
    }

    formatted_issues.append(fmt_iss)

fmt_dataset_file = "data/dataset_rebalanced_reformatted_train.json" 
with open(fmt_dataset_file, "w") as f:
    json.dump(formatted_issues, f, indent=4)