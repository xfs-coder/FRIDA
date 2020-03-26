import frida
import sys


def on_message(message, data):
    print("[%s] = > %s" (message, data))


def start_hook():
    device = frida.get_usb_device(timeout=5)
    app_package_name = "com.ct.client"
    try:
        pid = device.spawn([app_package_name])
        session = device.attach(pid)
        device.resume(pid)
        print("[*] start hook")

        with open("telecom.js", "r", encoding="utf-8") as f:
            jscode = f.read()
        script = session.create_script(jscode)
        script.on('message', on_message)
        script.load()
        return script
    except Exception as e:
        print(e)


if __name__ == '__main__':
    start_hook()