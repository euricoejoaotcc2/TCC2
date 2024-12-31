import json

# Load the JSON data
file_path = '/Users/eurico/Downloads/reaction-horusec.json'
with open(file_path, 'r') as file:
    data = json.load(file)

# Extract vulnerabilities' "details" and add vulnX labels
vulnerabilities = data.get("analysisVulnerabilities", [])
details_output = {}

for index, item in enumerate(vulnerabilities, start=1):
    vuln = item.get("vulnerabilities", {})
    details = vuln.get("details", "")
    if details:
        label = f"vuln{index:02d}"
        details_output[label] = details

# Generate the formatted output
formatted_output = ""
for label, details in details_output.items():
    formatted_output += f'{label}: "details": "{details}"\n'

# Save or return the result
output_file_path = '/Users/eurico/UNB/TCC2/classificar_vulns_owasp/output-horusec.json'
with open(output_file_path, 'w') as output_file:
    output_file.write(formatted_output)

print(f"Details extracted and saved to {output_file_path}")
