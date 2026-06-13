import os
from jinja2 import Environment, FileSystemLoader

def build_site():
    env = Environment(loader=FileSystemLoader('templates'))
    
    # Define a mapping of (Template File -> Final Output Path)
    # TODO: Update when more pages are added
    pages = {
        'index.html': 'index.html',
        'projects.html': 'Projects/index.html',
        'services.html': 'Services/index.html'
    }
    
    for template_name, output_path in pages.items():
        # Get target directory path and ensure it exists
        dir_name = os.path.dirname(output_path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
            
        # Compile via Jinja2
        template = env.get_template(template_name)
        rendered_html = template.render()
        
        # Write out raw index.html target
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(rendered_html)
            
    print("🚀 All templates compiled cleanly into their subdirectories!")

if __name__ == '__main__':
    build_site()
