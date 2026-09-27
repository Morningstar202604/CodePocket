#!/usr/bin/env python3
"""CodePocket 品牌化素材重制：驱动 mockup.html 生成全状态截图。
用法：python3 brand_shots.py
输出：design/screenshots/*.png（覆盖同名旧图）
"""
import os
from playwright.sync_api import sync_playwright

CHROME = "/opt/vm/preinstall/ms-playwright/chromium-1169/chrome-linux/chrome"
URL = "file:///home/user/Doubao/chats/38444434732973826/dev-terminal/design/mockup.html"
OUT = "/home/user/Doubao/chats/38444434732973826/dev-terminal/design/screenshots"

SHOTS = {}

def shot(page, name):
    dev = page.query_selector(".device")
    assert dev, f"{name}: .device not found"
    dev.screenshot(path=os.path.join(OUT, name))
    print("saved", name)

def click(page, sel, wait=500):
    page.evaluate("(s) => { const e = document.querySelector(s); if (e) e.click(); }", sel)
    page.wait_for_timeout(wait)

def send_input(page, value, wait=700):
    page.fill("#stdin", value)
    page.wait_for_timeout(350)
    page.click("#btnSend")
    page.wait_for_timeout(wait)

with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROME)

    def new_page(w=900, h=1200, dsf=2, onboard=False):
        page = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=dsf)
        page.goto(URL + ("?onboard=1" if onboard else ""), wait_until="domcontentloaded")
        page.wait_for_timeout(500)
        return page

    # 1. onboarding 引导页
    pg = new_page(onboard=True)
    shot(pg, "01-onboarding.png")
    pg.close()

    # 2. editor idle（进入编辑器）
    pg = new_page()
    shot(pg, "02-editor-idle.png")

    # 3. running（运行 main.py）
    click(pg, "#btnRun", 1800)
    shot(pg, "03-running.png")

    # 4. output done（猜数字完成）
    send_input(pg, "50")
    send_input(pg, "75")
    send_input(pg, "63", 900)
    shot(pg, "04-output-done.png")
    pg.close()

    # 5. error jump（utils.py 运行两次报错）
    pg = new_page()
    click(pg, '[data-tab="utils.py"]', 500)
    click(pg, "#btnRun", 1600)
    click(pg, "#btnRun", 2200)
    shot(pg, "05-error-jump.png")

    # 6. jump result（点报错行跳转）
    try:
        pg.evaluate("""() => { const j = document.querySelector('.out-body .l.jump'); if (j) j.click(); }""")
        pg.wait_for_timeout(900)
        shot(pg, "06-jump-result.png")
    except Exception as e:
        print("06-jump-result 失败:", e)
    pg.close()

    # 7. drawer files（文件抽屉）
    pg = new_page()
    click(pg, "#btnMenu", 600)
    shot(pg, "07-drawer-files.png")
    pg.close()

    # 8. java file（切 Main.java）
    pg = new_page()
    click(pg, '[data-tab="java-demo/Main.java"]', 600)
    shot(pg, "08-java-file.png")
    pg.close()

    # 9. global search（全局搜索）
    pg = new_page()
    click(pg, "#btnGsearch", 700)
    shot(pg, "09-global-search.png")
    pg.close()

    # 10. git（Git 弹窗）
    pg = new_page()
    click(pg, "#btnGit", 700)
    shot(pg, "10-git.png")
    pg.close()

    # 11. ai（AI 助手弹窗）
    pg = new_page()
    click(pg, "#btnAi", 700)
    shot(pg, "11-ai.png")
    pg.close()

    # 12. command palette（命令面板）
    pg = new_page()
    click(pg, "#btnCmd", 700)
    shot(pg, "12-command-palette.png")
    pg.close()

    # 13. landscape（横屏编辑器）
    pg = new_page(w=1100, h=600)
    shot(pg, "13-landscape.png")

    # 14. landscape output（横屏运行中）
    click(pg, "#btnRun", 1800)
    shot(pg, "14-landscape-output.png")
    pg.close()

    # 15. small screen（小屏编辑器）
    pg = new_page(w=420, h=800, dsf=2)
    shot(pg, "15-small-screen.png")
    pg.close()

    # 16. L1 editor light（浅色主题）
    pg = new_page()
    pg.evaluate("document.documentElement.setAttribute('data-theme','light')")
    pg.wait_for_timeout(400)
    shot(pg, "L1-editor-light.png")
    pg.close()

    b.close()
print("全部完成")
