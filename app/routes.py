from flask import Blueprint, jsonify, render_template, request

from .palette import generate_palette, PALETTE_MODES

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html", palette_modes=list(PALETTE_MODES.keys()))


@main.route("/api/generate", methods=["POST"])
def api_generate():
    """Generate a color palette from a base color."""
    data = request.get_json()
    base_color = data.get("base_color", "#3498db") if data else "#3498db"
    mode = data.get("mode", "analogous") if data else "analogous"
    count = data.get("count", 5) if data else 5

    try:
        palette = generate_palette(base_color, mode=mode, count=count)
        return jsonify({"palette": palette, "success": True})
    except (ValueError, TypeError) as e:
        return jsonify({"error": str(e), "success": False}), 400
