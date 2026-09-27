#!/usr/bin/env python3
"""CodePocket 浅色主题素材重制：生成 L2-L6 浅色系列截图。
用法：python3 light_shots.py
"""
import os
from playwright.sync_api import sync_playwright

CHROME = "/opt/vm/preinstall/ms-playwright/chromium-1169/chrome-linux/chrome"
URL = "file:///home/user/Doubao/chats/38444434732973826/dev-terminal/design/mockup.html"
OUT = "/home/user/Doubao/chats/38444434732973826/dev-terminal/design/screenshots"

def click(page, sel, wait=500):
    page.evaluate("(s) => { const e = document.querySelector(s); if (e) e.click(); }", sel)
    page.wait_for_timeout(wait)

def send_input(page, value, wait=700):
    page.fill("#stdin", value)
    page.wait_for_timeout(350)
    page.click("#btnSend")
    page.wait_for_timeout(wait)

def shot(page, name):
    dev = page.query_selector(".device")
    dev.screenshot(path=os.path.join(OUT, name))
    print("saved", name)

with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROME)

    def new_page(w=900, h=1200, dsf=2, onboard=False):
        page = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=dsf)
        page.goto(URL + ("?onboard=1" if onboard else ""), wait_until="domcontentloaded")
        page.wait_for_timeout(500)
        page.evaluate("document.documentElement.setAttribute('data-theme','light')")
        page.wait_for_timeout(400)
        return page

    # L3. 浅色引导页
    pg = new_page(onboard=True)
    shot(pg, "L3-onboard-light.png")
    pg.close()

    # L2. 浅色运行输出（猜数字完成）
    pg = new_page()
    click(pg, "#btnRun", 1800)
    send_input(pg, "50")
    send_input(pg, "75")
    send_input(pg, "63", 900)
    shot(pg, "L2-output-light.png")
    pg.close()

    # L6. 浅色错误跳转（utils.py 两次运行 + 点报错行）
    pg = new_page()
    click(pg, '[data-tab="utils.py"]', 500)
    click(pg, "#btnRun", 1600)
    click(pg, "#btnRun", 2200)
    try:
        pg.evaluate("""() => { const j = document.querySelector('.out-body .l.jump'); if (j) j.click(); }""")
        pg.wait_for_timeout(900)
    except Exception as e:
        print("L6 jump:", e)
    shot(pg, "L6-jump-light.png")
    pg.close()

    # L4. 浅色抽屉
    pg = new_page()
    click(pg, "#btnMenu", 600)
    shot(pg, "L4-drawer-light.png")
    pg.close()

    # L5. 浅色 Git 弹窗
    pg = new_page()
    click(pg, "#btnGit", 700)
    shot(pg, "L5-git-light.png")
    pg.close()

    b.close()
print("L 系列完成")
