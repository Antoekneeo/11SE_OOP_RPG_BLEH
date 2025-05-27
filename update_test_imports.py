"""Script to update test imports to use absolute imports."""
import os

def update_file(file_path):
    """Update imports in a single file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace relative imports with absolute imports
    replacements = [
        ('from character import', 'from rpg_game.character import'),
        ('from boss import', 'from rpg_game.boss import'),
        ('from weapon import', 'from rpg_game.weapon import'),
        ('from game import', 'from rpg_game.game import'),
        ('from game_logger import', 'from rpg_game.game_logger import'),
        ('from save_game import', 'from rpg_game.save_game import'),
        ('from console_utils import', 'from rpg_game.console_utils import'),
        ('import character', 'import rpg_game.character as character'),
        ('import boss', 'import rpg_game.boss as boss'),
        ('import weapon', 'import rpg_game.weapon as weapon'),
        ('import game', 'import rpg_game.game as game')
    ]
    
    updated = False
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            updated = True
    
    if updated:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {file_path}")

def main():
    """Update imports in all test files."""
    test_dir = os.path.join(os.path.dirname(__file__), 'tests')
    for root, _, files in os.walk(test_dir):
        for file in files:
            if file.startswith('test_') and file.endswith('.py'):
                update_file(os.path.join(root, file))
    # Also update conftest.py
    update_file(os.path.join(test_dir, 'conftest.py'))

if __name__ == '__main__':
    main()
