"""
Game class for the RPG game.

This module defines the main Game class that manages the game flow and state.
"""

from typing import List, Optional, Dict, Any, Tuple
import random
from console_utils import clear_screen, press_enter, print_border
from character import Character
from boss import Boss
from game_logger import GameLogger


class Game:
    """
    Manages the main game loop and state.
    
    This class coordinates all game components and handles the game flow.
    """
    
    def __init__(self) -> None:
        """Initialize a new game instance."""
        self.player: Optional[Character] = None
        self.bosses: List[Boss] = []
        self.logger: GameLogger = GameLogger()
    
    def show_intro(self) -> None:
        """Display the game introduction and setup the game."""
        clear_screen()
        print("Welcome to the RPG Adventure!")
        print("In a world where darkness looms, you are the chosen hero "
              "destined to defeat the evil bosses and restore peace.")
        player_name = input("Enter your character's name: ").capitalize()
        self.setup_game(player_name)
    
    def setup_game(self, name: str) -> None:
        """
        Set up the game with the player character and bosses.
        
        Args:
            name: The player's character name
        """
        weapon_name, weapon_damage = self.choose_weapon()
        self.player = Character(name, 110, 10, weapon_name, weapon_damage)
        self.player.display()
        press_enter()
        
        # Create boss enemies
        self.bosses = [
            Boss("Goblin King", 50, 8),
            Boss("Dark Sorcerer", 60, 9)
        ]
    
    def choose_weapon(self) -> Tuple[str, int]:
        """
        Let the player choose a weapon.
        
        Returns:
            A tuple of (weapon_name, weapon_damage)
        """
        weapons = [
            {"name": "Rock", "damage_bonus": 2},
            {"name": "Paper", "damage_bonus": 3},
            {"name": "Scissors", "damage_bonus": 4}
        ]
        
        print("\nChoose your weapon:")
        for i, weapon in enumerate(weapons, 1):
            print(f"{i}. {weapon['name']} (+{weapon['damage_bonus']} damage)")
        
        while True:
            try:
                choice = int(input("\nEnter your choice (1-3): "))
                if 1 <= choice <= len(weapons):
                    weapon = weapons[choice - 1]
                    return weapon["name"], weapon["damage_bonus"]
                print(f"Please enter a number between 1 and {len(weapons)}")
            except ValueError:
                print("Please enter a valid number.")
    
    def combat(self, player: Character, enemy: Boss) -> bool:
        """
        Handle combat between the player and an enemy.
        
        Args:
            player: The player character
            enemy: The enemy to fight
            
        Returns:
            bool: True if player wins, False if player loses
        """
        while player.health > 0 and enemy.health > 0:
            self.display_combat_status(player, enemy)
            
            # Player's turn
            damage_dealt = player.attack(enemy, self.logger)
            print(f"You dealt {damage_dealt} damage to {enemy.name}.")
            
            if enemy.health <= 0:
                self.print_victory_message(enemy)
                return True
            
            # Enemy's turn
            damage_received = enemy.attack(player, self.logger)
            print(f"{enemy.name} dealt {damage_received} damage to you.")
            
            if player.health <= 0:
                self.print_defeat_message(enemy)
                return False
                
            press_enter()
        
        return False  # Shouldn't reach here
    
    def display_combat_status(self, player: Character, enemy: Boss) -> None:
        """
        Display the current status of combat.
        
        Args:
            player: The player character
            enemy: The current enemy
        """
        clear_screen()
        level = "LEVEL 1" if enemy.name == "Goblin King" else "LEVEL 2"
        print(f"\n{'='*15}> {level}: {enemy.name} <{'='*15}")
        player.display()
        print("-" * 30)
        enemy.display()
        print("-" * 30)
    
    def handle_boss_battles(self) -> None:
        """Handle the sequence of boss battles."""
        for boss in self.bosses:
            self.introduce_boss(boss)
            if not self.combat(self.player, boss):
                self.end_game(False)
                return
        self.end_game(True)
    
    def introduce_boss(self, boss: Boss) -> None:
        """
        Display the boss introduction.
        
        Args:
            boss: The boss being introduced
        """
        clear_screen()
        intro_messages = {
            "Goblin King": (
                f"Level 1 - You have entered the lair of the Goblin King. "
                f"He is known for his strength and brutality. Prepare for battle, {self.player.name}!"
            ),
            "Dark Sorcerer": (
                f"Level 2 - You have defeated the Goblin King! Now, you face the Dark Sorcerer, "
                f"a master of dark magic. Good luck, {self.player.name}!"
            )
        }
        print(intro_messages.get(boss.name, "A new boss appears!"))
        press_enter()
    
    def print_victory_message(self, enemy: Boss) -> None:
        """
        Print the victory message after defeating an enemy.
        
        Args:
            enemy: The defeated enemy
        """
        print_border()
        print(f"Victory! You defeated {enemy.name}.")
        press_enter()
    
    def print_defeat_message(self, enemy: Boss) -> None:
        """
        Print the defeat message after losing to an enemy.
        
        Args:
            enemy: The enemy that defeated the player
        """
        print_border()
        print(f"Defeat! You were defeated by {enemy.name}.")
        press_enter()
    
    def end_game(self, player_won: bool) -> None:
        """
        End the game and display the appropriate message.
        
        Args:
            player_won: Whether the player won the game
        """
        print_border()
        if player_won:
            print("Congratulations! You have defeated all the bosses and saved the kingdom!")
        else:
            print("Game Over! The forces of darkness have prevailed...")
        print("\nThanks for playing!")
    
    def run(self) -> None:
        """Run the main game loop."""
        self.show_intro()
        self.handle_boss_battles()
