import os
import re

ROUTES_DIR = "src/routes"

def scan_routes(directory):
    print(f"Scanning routes in {directory}...")
    routes = []
    # Regex to capture router.method('path', ...)
    # Handles router.get, router.post, etc.
    # Handles: router.get('/path',
    # Handles: router.post("/path",
    pattern = re.compile(r"router\.(get|post|put|delete|patch|use)\s*\(\s*['\"]([^'\"]+)['\"]")

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".ts") or file.endswith(".js"):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    matches = pattern.findall(content)
                    for method, route_path in matches:
                        routes.append({
                            "file": file,
                            "method": method.upper(),
                            "path": route_path
                        })
    return routes

def main():
    if not os.path.exists(ROUTES_DIR):
        print(f"Directory {ROUTES_DIR} not found.")
        return

    routes = scan_routes(ROUTES_DIR)
    
    print(f"\nFound {len(routes)} routes:")
    print("-" * 50)
    print(f"{'METHOD':<10} {'PATH':<40} {'FILE'}")
    print("-" * 50)
    
    for r in sorted(routes, key=lambda x: (x['path'], x['method'])):
        print(f"{r['method']:<10} {r['path']:<40} {r['file']}")
    
    print("-" * 50)
    print("TODO: Compare against openapi.yaml when available.")

if __name__ == "__main__":
    main()
