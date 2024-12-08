from typing import List, Dict, Any

def search(items: List[Dict[str, Any]], query: Dict[str, str]) -> List[Dict[str, Any]]:
    results = items
    for key, value in query.items():
        if value:
            results = [item for item in results if value.lower() in str(item.get(key, '')).lower()]
    return results
