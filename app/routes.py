from flask import Blueprint, jsonify
import os
from .db import check_db

bp = Blueprint("routes", __name__)

@bp.get("/healthz")
def healthz():
    return jsonify({"status": "ok"}), 200

@bp.get("/readyz")
def readyz():
    # In-memory ready by default; if DB_CHECK=true, verify DB connectivity.
    if os.getenv("DB_CHECK", "false").lower() == "true":
        if not check_db():
            return jsonify({"status": "not-ready", "reason": "db"}), 503
    return jsonify({"status": "ready"}), 200
