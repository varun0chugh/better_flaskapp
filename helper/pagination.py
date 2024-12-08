from typing import List, Dict, Any

def paginate(items: List[Dict[str, Any]], page: int, per_page: int) -> Dict[str, Any]:
    
    total_items = len(items)
    start = (page - 1) * per_page
    end = start + per_page
    paginated_items = items[start:end]

    return {
        "data": paginated_items,
        "meta": {
            "page": page,
            "per_page": per_page,
            "total_pages": (total_items + per_page - 1) // per_page,
            "total_items": total_items,
        },
    }
