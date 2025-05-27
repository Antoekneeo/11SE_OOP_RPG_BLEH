"""
Tests for the save_game module.
"""
import os
import json
import pytest
import tempfile
from pathlib import Path
from unittest.mock import patch, mock_open

# Import the module to test
import rpg_game.save_game as save_game_module
from rpg_game.save_game import save_game, load_game, delete_save, set_save_paths

@pytest.fixture
def temp_save_file(tmp_path):
    """Fixture to create a temporary save file for testing."""
    # Create a temporary save directory
    temp_save_dir = tmp_path / "saves"
    temp_save_dir.mkdir()
    temp_save_file = temp_save_dir / "save.json"
    
    # Set the save paths for testing
    set_save_paths(str(temp_save_dir), str(temp_save_file))
    
    yield temp_save_file

class TestSaveGame:
    """Test cases for the save_game module."""
    
    def test_save_dir_creation(self, tmp_path):
        """Test that save directory is created if it doesn't exist."""
        # Set up test paths
        temp_save_dir = tmp_path / "test_saves"
        temp_save_file = temp_save_dir / "save.json"
        
        # Ensure directory doesn't exist initially
        assert not temp_save_dir.exists()
        
        # Set the save paths for testing
        set_save_paths(str(temp_save_dir), str(temp_save_file))
        
        # This should create the directory
        save_game({})
        
        # Check directory was created
        assert temp_save_dir.exists()
        assert temp_save_file.exists()

    def test_save_game(self, temp_save_file):
        """Test saving game state to file."""
        test_data = {
            "player": {"name": "TestPlayer", "health": 100, "level": 1},
            "bosses": [{"name": "TestBoss", "health": 50}]
        }
        
        # Save the game
        result = save_game(test_data)
        
        # Check if file was created
        assert result is True
        assert temp_save_file.exists()
        
        # Verify file content
        with open(temp_save_file, 'r') as f:
            saved_data = json.load(f)
            
        assert saved_data == test_data
        
    def test_save_game_error(self, monkeypatch):
        """Test error handling when saving game fails."""
        # Mock open to raise an IOError
        def mock_open_raise(*args, **kwargs):
            raise IOError("Mocked IOError")
            
        monkeypatch.setattr('builtins.open', mock_open_raise)
        
        test_data = {"test": "data"}
        result = save_game(test_data)
        assert result is False
    
    def test_load_game(self, temp_save_file):
        """Test loading game state from file."""
        test_data = {
            "player": {"name": "TestPlayer", "health": 100, "level": 1},
            "bosses": [{"name": "TestBoss", "health": 50}]
        }
        
        # Create a save file
        with open(temp_save_file, 'w') as f:
            json.dump(test_data, f)
        
        # Load the game
        loaded_data = load_game()
        
        # Verify loaded data
        assert loaded_data == test_data
        
    def test_load_game_file_not_found(self, temp_save_file):
        """Test loading when save file doesn't exist."""
        # Ensure file doesn't exist
        if temp_save_file.exists():
            temp_save_file.unlink()
            
        loaded_data = load_game()
        assert loaded_data is None
        
    def test_load_game_json_error(self, temp_save_file, monkeypatch):
        """Test loading when save file contains invalid JSON."""
        # Create a file with invalid JSON
        with open(temp_save_file, 'w') as f:
            f.write("invalid json")
            
        loaded_data = load_game()
        assert loaded_data is None
    
    def test_delete_save(self, temp_save_file):
        """Test deleting a save file."""
        # Create a save file first
        test_data = {"test": "data"}
        with open(temp_save_file, 'w') as f:
            json.dump(test_data, f)
            
        # Delete the save
        result = delete_save()
        
        # Verify file was deleted
        assert result is True
        assert not temp_save_file.exists()
        
    def test_delete_nonexistent_save(self, temp_save_file):
        """Test deleting a non-existent save file."""
        # Ensure file doesn't exist
        if temp_save_file.exists():
            temp_save_file.unlink()
            
        # Should return True even if file didn't exist
        assert delete_save() is True
    
    def test_delete_save_error(self, tmp_path, monkeypatch):
        """Test error handling when deleting save file fails."""
        # Create a temporary file that will cause the mock to be used
        temp_dir = tmp_path / "test_saves"
        temp_dir.mkdir()
        temp_file = temp_dir / "save.json"
        temp_file.write_text("test")
        
        # Set the save paths for testing
        set_save_paths(str(temp_dir), str(temp_file))
        
        # Mock os.remove to raise an OSError
        def mock_remove(*args, **kwargs):
            raise OSError("Mocked OSError")
            
        monkeypatch.setattr('os.remove', mock_remove)
        
        # This should call our mock and return False due to the error
        assert delete_save() is False
