import requests, os, re
from urllib.parse import urlparse

URLS = [
    "https://jiotv.edge-nexus.workers.dev?token=42e4f5-2d863b-3c37d8-7f3f51",
    "https://zee5.cloud-hatchh.workers.dev?token=42e4f5-2d413b-3c37d8-7f3f25",
    "https://jiocinema-live.cloud-hatchh.workers.dev?token=42e4f5-2d413b-3c37d8-5f3f45",
    "https://sonyliv.logic-lane.workers.dev?token=a13d9c-4b782a-6c90fd-9a1b84",
    "https://hotstarlive.delta-cloud.workers.dev?token=a13d9c-4b782a-6c90fd-9a1b84",
]

FIREFOX_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Accept": "*/*",
    "Cache-Control": "no-cache, no-store",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"
}

OKHTTP_HEADERS = {
    "User-Agent": "okhttp/4.12.0",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"
}

def pick_headers(url):
    return OKHTTP_HEADERS if urlparse(url).path.lower().endswith((".m3u", ".m3u8")) else FIREFOX_HEADERS

os.makedirs("debug_out", exist_ok=True)

print("\n=========== GITHUB ACTION DEBUG ===========\n")

for i, url in enumerate(URLS, 1):
    try:
        print("REQUEST:", repr(url))
        r = requests.get(url, headers=pick_headers(url), timeout=25, allow_redirects=True)

        print("STATUS:", r.status_code)
        print("TYPE  :", r.headers.get("Content-Type"))
        print("SERVER:", r.headers.get("Server"))
        print("CF-RAY:", r.headers.get("CF-RAY"))
        print("LEN   :", len(r.content))

        head = r.text[:300].replace("\n", "\\n")
        print("FIRST:", head)

        fname = f"debug_out/resp_{i}.txt"
        with open(fname, "wb") as f:
            f.write(r.content)

        print("SAVED:", fname)
        print("-" * 60)

    except Exception as e:
        print("ERROR:", e)

print("\n=========== DONE ===========\n")
