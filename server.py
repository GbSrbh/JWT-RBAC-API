import uvicorn
import os

port = int(os.environ.get("PORT", "5000"))

if __name__ == '__main__':
    uvicorn.run("src:app", host="127.0.0.1", port=port, reload=True)
