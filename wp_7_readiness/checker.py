import os
import sys
import argparse
from typing import List, Dict

class WP7ReadinessChecker:
    def __init__(self, wp_path: str):
        self.wp_path = wp_path
        self.issues = []

    def check_php_version(self):
        import subprocess
        import re

        try:
            result = subprocess.run(["php", "-v"], capture_output=True, text=True, check=True)
            output = result.stdout
            # Match "PHP 7.4.3" or "PHP 8.2.0"
            match = re.search(r"PHP (\d+\.\d+\.\d+)", output)
            if match:
                version_str = match.group(1)
                major, minor, patch = map(int, version_str.split('.'))
                
                # Logic: Block < 7.4
                if major < 7 or (major == 7 and minor < 4):
                    self.issues.append({
                        "component": "PHP Version",
                        "status": "CRITICAL BLOCKER",
                        "message": f"Detected PHP {version_str}. WordPress 7.0 upgrade will be BLOCKED. You MUST upgrade to PHP 7.4+ (8.2+ recommended)."
                    })
                elif (major == 7 and minor >= 4) or (major == 8 and minor < 2):
                     self.issues.append({
                        "component": "PHP Version",
                        "status": "Warning",
                        "message": f"Detected PHP {version_str}. Upgrade allowed, but PHP 8.2+ is highly recommended for WordPress 7.0 features."
                    })
                else:
                    self.issues.append({
                        "component": "PHP Version",
                        "status": "Pass",
                        "message": f"Detected PHP {version_str}. Ready for WordPress 7.0."
                    })
            else:
                 self.issues.append({
                    "component": "PHP Version",
                    "status": "Unknown",
                    "message": "Could not parse 'php -v' output. Ensure PHP 7.4+ is installed."
                })

        except (FileNotFoundError, subprocess.CalledProcessError):
            self.issues.append({
                "component": "PHP Version",
                "status": "Warning",
                "message": "PHP executable not found in PATH. Cannot verify version compatibility (Requires PHP 7.4+)."
            })

    def check_plugins(self):
        plugins_path = os.path.join(self.wp_path, "wp-content", "plugins")
        if not os.path.exists(plugins_path):
            return

        multilingual_plugins = ['sitepress-multilingual-cms', 'polylang', 'qtranslate-xt']
        collaboration_plugins = ['edit-flow', 'oasis-workflow', 'co-authors-plus']

        for plugin in os.listdir(plugins_path):
            if plugin in multilingual_plugins:
                self.issues.append({
                    "component": f"Plugin: {plugin}",
                    "status": "Info",
                    "message": "Multilingual plugin detected. WordPress 7.0 (Phase 4) will introduce native multilingual support. Plan for potential migration."
                })
            if plugin in collaboration_plugins:
                self.issues.append({
                    "component": f"Plugin: {plugin}",
                    "status": "Info",
                    "message": "Collaboration plugin detected. WordPress 7.0 (Phase 3) enhances native collaboration features."
                })

    def check_theme_type(self):
        themes_path = os.path.join(self.wp_path, "wp-content", "themes")
        if not os.path.exists(themes_path):
            return

        for theme in os.listdir(themes_path):
            theme_dir = os.path.join(themes_path, theme)
            if os.path.isdir(theme_dir):
                if os.path.exists(os.path.join(theme_dir, "templates")):
                    # Likely a block theme
                    continue
                else:
                    self.issues.append({
                        "component": f"Theme: {theme}",
                        "status": "Notice",
                        "message": "Classic theme detected. WP 7.0 will further prioritize Block themes."
                    })

    def run(self) -> List[Dict]:
        if not os.path.exists(self.wp_path):
            print(f"Error: Path {self.wp_path} does not exist.")
            sys.exit(1)
        
        self.check_php_version()
        self.check_plugins()
        self.check_theme_type()
        return self.issues

def main():
    parser = argparse.ArgumentParser(description="WP 7.0 Readiness Checker")
    parser.add_argument("path", help="Path to WordPress root directory")
    args = parser.parse_args()

    checker = WP7ReadinessChecker(args.path)
    results = checker.run()

    print("\n--- WordPress 7.0 Release Squad Readiness Report ---")
    for issue in results:
        print(f"[{issue['status']}] {issue['component']}: {issue['message']}")
    print("----------------------------------------------------\n")

if __name__ == "__main__":
    main()
