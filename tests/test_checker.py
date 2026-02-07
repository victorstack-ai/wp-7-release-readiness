import os
import shutil
import tempfile
import pytest
from wp_7_readiness.checker import WP7ReadinessChecker

@pytest.fixture
def mock_wp_site():
    temp_dir = tempfile.mkdtemp()
    wp_content = os.path.join(temp_dir, "wp-content")
    themes_path = os.path.join(wp_content, "themes")
    os.makedirs(themes_path)
    
    # Create a classic theme
    classic_theme = os.path.join(themes_path, "classic-theme")
    os.makedirs(classic_theme)
    with open(os.path.join(classic_theme, "index.php"), "w") as f:
        f.write("<?php // classic")
        
    # Create a block theme
    block_theme = os.path.join(themes_path, "block-theme")
    os.makedirs(os.path.join(block_theme, "templates"))
    with open(os.path.join(block_theme, "style.css"), "w") as f:
        f.write("/* block */")

    yield temp_dir
    shutil.rmtree(temp_dir)

def test_checker_report(mock_wp_site):
    checker = WP7ReadinessChecker(mock_wp_site)
    results = checker.run()
    
    assert len(results) >= 2
    # Should have a PHP warning
    assert any(r['component'] == 'PHP' for r in results)
    # Should have a notice about the classic theme
    assert any('Theme: classic-theme' in r['component'] for r in results)
    # Block theme should not have a notice (currently)
    assert not any('Theme: block-theme' in r['component'] for r in results)
