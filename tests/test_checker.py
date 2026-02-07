import os
import shutil
import tempfile
import pytest
from unittest.mock import patch, MagicMock
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

@patch('subprocess.run')
def test_checker_report_php_old(mock_subprocess, mock_wp_site):
    # Simulate PHP 7.3
    mock_subprocess.return_value = MagicMock(stdout="PHP 7.3.33 (cli) (built: Nov 19 2021 10:00:00) ( NTS )")
    
    checker = WP7ReadinessChecker(mock_wp_site)
    results = checker.run()
    
    # Verify Critical Blocker
    php_issues = [r for r in results if r['component'] == 'PHP Version']
    assert len(php_issues) == 1
    assert php_issues[0]['status'] == 'CRITICAL BLOCKER'
    assert 'PHP 7.3.33' in php_issues[0]['message']

@patch('subprocess.run')
def test_checker_report_php_modern(mock_subprocess, mock_wp_site):
    # Simulate PHP 8.2
    mock_subprocess.return_value = MagicMock(stdout="PHP 8.2.1 (cli) (built: Jan 13 2023 10:00:00) ( NTS )")
    
    checker = WP7ReadinessChecker(mock_wp_site)
    results = checker.run()
    
    # Verify Pass
    php_issues = [r for r in results if r['component'] == 'PHP Version']
    assert len(php_issues) == 1
    assert php_issues[0]['status'] == 'Pass'

@patch('subprocess.run')
def test_checker_report_php_missing(mock_subprocess, mock_wp_site):
    # Simulate missing PHP
    mock_subprocess.side_effect = FileNotFoundError
    
    checker = WP7ReadinessChecker(mock_wp_site)
    results = checker.run()
    
    # Verify Warning
    php_issues = [r for r in results if r['component'] == 'PHP Version']
    assert len(php_issues) == 1
    assert php_issues[0]['status'] == 'Warning'
    assert 'not found' in php_issues[0]['message']

@patch('subprocess.run')
def test_theme_check(mock_subprocess, mock_wp_site):
    # Just to pass the PHP check quietly
    mock_subprocess.return_value = MagicMock(stdout="PHP 8.2.0")

    checker = WP7ReadinessChecker(mock_wp_site)
    results = checker.run()

    # Should have a notice about the classic theme
    assert any('Theme: classic-theme' in r['component'] for r in results)
    # Block theme should not have a notice
    assert not any('Theme: block-theme' in r['component'] for r in results)