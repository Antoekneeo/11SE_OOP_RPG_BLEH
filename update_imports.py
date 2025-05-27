"""Script to update imports in source files to use absolute imports."""
import os

def update_file(file_path):
    """Update imports in a single file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace relative imports with absolute imports
    replacements = [
        ('from weapon import', 'from rpg_game.weapon import'),
        ('from character import', 'from rpg_game.character import'),
        ('from boss import', 'from rpg_game.boss import'),
        ('from game import', 'from rpg_game.game import'),
        ('from game_logger import', 'from rpg_game.game_logger import'),
        ('from save_game import', 'from rpg_game.save_game import'),
        ('from console_utils import', 'from rpg_game.console_utils import'),
        ('import weapon', 'import rpg_game.weapon as weapon'),
        ('import character', 'import rpg_game.character as character'),
        ('import boss', 'import rpg_game.boss as boss'),
        ('import game', 'import rpg_game.game as game'),
        ('import game_logger', 'import rpg_game.game_logger as game_logger'),
        ('import save_game', 'import rpg_game.save_game as save_game'),
        ('import console_utils', 'import rpg_game.console_utils as console_utils')
    ]
    
    updated = False
    for old, new in replacements:
        if old in content and not content.strip().startswith('#'):
            content = content.replace(old, new)
            updated = True
    
    if updated:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {file_path}")

def main():
    """Update imports in all Python files."""
    src_dir = os.path.join(os.path.dirname(__file__), 'src', 'rpg_game')
    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.py'):
                update_file(os.path.join(root, file))

if __name__ == '__main__':
    main()
