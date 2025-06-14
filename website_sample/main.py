import sqlite3
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn

from mount_fastapi import fastapi_app_config
from home import get_home_component
from members import get_members_component
from devices import get_devices_component
from myprofile import get_profile_component
from about import get_about_component


def check_up(username, password):
    conn = sqlite3.connect("website_sample.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username=?", (username,))
    record = cursor.fetchone()
    cursor.close()
    conn.close()
    if not record:
        return False
    password_in_db = record[0]
    return password == password_in_db


app = FastAPI()

home_app = get_home_component()
members_app = get_members_component()
devices_app = get_devices_component()
profile_app = get_profile_component()
about_app = get_about_component()

fastapi_app_config(app,
                   {"/home": home_app,
                    "/members": members_app,
                    "/devices": devices_app,
                    "/profile": profile_app,
                    "/about": about_app},
                   auth=check_up)


@app.get("/")
async def read_root():
    return RedirectResponse(url="/home")


def init_db():
    # 创建sqlite数据库，并创建users表，插入admin用户，默认密码为admin
    # users表包含3个字段：username, description, password
    conn = sqlite3.connect("website_sample.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, description TEXT, password TEXT)")
    cursor.execute("INSERT OR IGNORE INTO users (username, description, password) VALUES ('admin', '', 'admin')")
    conn.commit()
    cursor.close()
    conn.close()


init_db()

uvicorn.run(app=app)
