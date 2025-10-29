#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Google Maps Forensic Extractor
# Extracts records from gmm_myplaces.db → sync_item table

import sqlite3
import json
import binascii
from datetime import datetime

# === CONFIG ===
DB_PATH = "gmm_myplaces.db"           # Path to your database file
OUTPUT_PATH = "myplaces_sync_items.csv"

def convert_timestamp(ts):
    """Convert milliseconds since epoch to human-readable UTC time."""
    try:
        ts = int(ts)
        return datetime.utcfromtimestamp(ts / 1000).strftime("%Y-%m-%d %H:%M:%S UTC")
    except Exception:
        return ""

def decode_blob(blob):
    """Attempt to decode the sync_item BLOB into readable text or preview."""
    if blob is None:
        return ""
    try:
        # Try UTF-8 decoding
        text = blob.decode("utf-8", errors="ignore")
        if text.strip():
            return text[:500]
    except Exception:
        pass
    # Fallback: return hex preview if binary
    return binascii.hexlify(blob[:50]).decode("utf-8") + "..."

# === MAIN EXTRACTION ===
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

try:
    cur.execute("SELECT corpus, key_string, timestamp, latitude, longitude, is_local, sync_item FROM sync_item;")
    rows = cur.fetchall()
finally:
    conn.close()

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write("corpus,key_string,timestamp,utc_time,latitude,longitude,is_local,sync_item_preview\n")
    for corpus, key, ts, lat, lon, local, blob in rows:
        try:
            lat_deg = float(lat) / 1e6 if lat else ""
            lon_deg = float(lon) / 1e6 if lon else ""
        except Exception:
            lat_deg, lon_deg = "", ""
        f.write(f"{corpus},{key},{ts},{convert_timestamp(ts)},{lat_deg},{lon_deg},{local},\"{decode_blob(blob)}\"\n")

print(f"[+] Extracted {len(rows)} records from sync_item")
print(f"[+] Output saved to {OUTPUT_PATH}")
