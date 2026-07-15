import os
from jinja2 import Environment, FileSystemLoader

def build_site():
    env = Environment(loader=FileSystemLoader('templates'))
    
    # TODO: Either automate it or manually add new pages whenever they are created.
    pages = {
        'index.html': 'index.html',
        'projects.html': 'Projects/index.html',
        'blog.html': 'Blog/index.html'
    }
    
    for template_name, output_path in pages.items():
        # Handle subfolder generation safely
        dir_name = os.path.dirname(output_path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
            
        # Calculate folder depth to find the asset directory path
        # For index.html -> path_base is "./"
        # For Projects/index.html -> path_base is "../"
        path_base = "./" if not dir_name else "../" * len(dir_name.split(os.sep))

        template = env.get_template(template_name)
        
        # Inject the path baseline context directly into Jinja2
        rendered_html = template.render(path_base=path_base)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(rendered_html)
            
    print("🚀 All templates compiled cleanly with relative asset tracking!")

if __name__ == '__main__':
    build_site()
