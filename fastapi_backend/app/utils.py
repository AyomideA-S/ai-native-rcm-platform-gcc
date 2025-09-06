from fastapi.routing import APIRoute


def simple_generate_unique_route_id(route: APIRoute) -> str:
    """Generate a unique route ID based on the route's tag and name.

    Args:
        route (APIRoute): The API route for which to generate the ID.

    Returns:
        str: A unique identifier for the route.
    """
    tag = route.tags[0] if route.tags else "default"
    return f"{tag}-{route.name}"
