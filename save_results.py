# src/save_results.py

import json
import pdfkit

def save_results(results, output_format, output_folder):
    if output_format == 'txt':
        with open(f'{output_folder}/analysis.txt', 'w') as f:
            for result in results:
                f.write(f"File: {result['file']}\nAnalysis: {result['analysis']}\n\n")
    elif output_format == 'json':
        with open(f'{output_folder}/analysis.json', 'w') as f:
            json.dump(results, f, indent=4)
    elif output_format == 'pdf':
        with open(f'{output_folder}/analysis.html', 'w') as f:
            for result in results:
                f.write(f"<h1>File: {result['file']}</h1><p>Analysis: {result['analysis']}</p><br>")
        pdfkit.from_file(f'{output_folder}/analysis.html', f'{output_folder}/analysis.pdf')
